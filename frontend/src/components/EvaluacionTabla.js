import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "../styles/EvaluacionTabla.css";
import preguntas from "../data/preguntas.json";
import Navbar from "./Navbar";
import Footer from "./Footer";
import { obtenerPreguntasPorNormaYCriterio } from "../utils/utils";

const EvaluacionTabla = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { tipoSoftware = "Desconocido", norma = "Desconocida", criterios = [] } = location.state || {};

  const preguntasSeleccionadas = obtenerPreguntasPorNormaYCriterio(
    norma,
    criterios.map((c) => c.criterio),
    preguntas
  );

  const [valores, setValores] = useState({});
  const [observaciones, setObservaciones] = useState({});
  const [resultados, setResultados] = useState(null);

  const handleValorChange = (pregunta, value) => {
    setValores((prev) => ({
      ...prev,
      [pregunta]: value,
    }));
  };

  const handleObservacionesChange = (pregunta, value) => {
    setObservaciones((prev) => ({
      ...prev,
      [pregunta]: value,
    }));
  };

  const calcularResultados = () => {
    const resultadosPorCriterio = criterios.map((criterio) => {
      const preguntasCriterio = preguntasSeleccionadas.filter(
        (pregunta) => pregunta.item === criterio.criterio
      );

      const totalPreguntas = preguntasCriterio.length;
      const sumaValores = preguntasCriterio.reduce(
        (suma, pregunta) => suma + (parseFloat(valores[pregunta.descripcion]) || 0),
        0
      );

      const porcentaje = totalPreguntas > 0 ? (sumaValores / (totalPreguntas * 5)) * 100 : 0;

      return {
        criterio: criterio.criterio,
        porcentaje: porcentaje.toFixed(2),
      };
    });

    return resultadosPorCriterio;
  };

  const handleVerResultados = async () => {
    // Calcula los resultados
    const resultadosCalculados = calcularResultados();

    // Simula el guardado en la base de datos (puedes reemplazarlo con una API real)
    console.log("Guardando en la base de datos:", {
      tipoSoftware,
      norma,
      resultadosCalculados,
    });

    // Actualiza el estado para mostrar los resultados
    setResultados(resultadosCalculados);
  };

  const handleMatrizRiesgos = () => {
    navigate("/matriz-riesgos");
  };

  const handleVolverInicio = () => {
    navigate("/UserHome");
  };

  return (
    <div className="evaluacion-tabla-page">
      <Navbar /> 
        <div className="evaluacion-tabla-container">
          <h1>Evaluación de {norma}</h1>
          <h2>Software: {tipoSoftware}</h2>
          <table className="evaluacion-tabla">
            <thead>
              <tr>
                <th>Ítem</th>
                <th>Criterio</th>
                <th>Descripción</th>
                <th>Valor</th>
                <th>Observaciones</th>
              </tr>
            </thead>
            <tbody>
              {preguntasSeleccionadas.map((pregunta, index) => (
                <tr key={index}>
                  <td>{index + 1}</td>
                  <td>{pregunta.item}</td>
                  <td>{pregunta.descripcion}</td>
                  <td>
                    <input
                      type="number"
                      min="1"
                      max="5"
                      value={valores[pregunta.descripcion] || ""}
                      onChange={(e) =>
                        handleValorChange(pregunta.descripcion, e.target.value)
                      }
                    />
                  </td>
                  <td>
                    <input
                      type="text"
                      value={observaciones[pregunta.descripcion] || ""}
                      onChange={(e) =>
                        handleObservacionesChange(pregunta.descripcion, e.target.value)
                      }
                    />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <button onClick={handleVerResultados} className="guardar-btn-riesgos">
            Ver Resultados Evaluación
          </button>

          {resultados && (
            <div className="resultados-container">
              <h2>Resultados de la Evaluación</h2>
              <table className="resultados-tabla">
                <thead>
                  <tr>
                    <th>Criterio</th>
                    <th>Porcentaje Total</th>
                  </tr>
                </thead>
                <tbody>
                  {resultados.map((resultado, index) => (
                    <tr key={index}>
                      <td>{resultado.criterio}</td>
                      <td>{resultado.porcentaje}%</td>
                    </tr>
                  ))}
                </tbody>
              </table>
              <div className="botones-acciones">
                <button onClick={handleMatrizRiesgos} className="matriz-btn">
                  Realizar Matriz de Riesgos
                </button>
                <button onClick={handleVolverInicio} className="inicio-btn">
                  Volver al Inicio
                </button>
              </div>
            </div>
          )}
        </div>
        <Footer />
      </div>
  );
};

export default EvaluacionTabla;
