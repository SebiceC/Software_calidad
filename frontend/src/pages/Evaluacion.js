import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Importa useNavigate
import "../styles/Evaluacion.css";
import preguntas from "../data/preguntas.json"; // Importa el banco de preguntas
import { obtenerPreguntasPorNormaYCriterio } from "../utils/utils"; // Importa la función utilitaria

const EvaluacionFlujo = () => {
  const [paso, setPaso] = useState(1);
  const [tipoSoftware, setTipoSoftware] = useState("");
  const [norma, setNorma] = useState("");
  const [criterios, setCriterios] = useState([]);
  const navigate = useNavigate(); // Inicializa navigate

  const criteriosPorNorma = {
    "Software Bancario": {
      FURPS: [
        { criterio: "Funcionalidad", porcentaje: 40 },
        { criterio: "Usabilidad", porcentaje: 25 },
        { criterio: "Confiabilidad", porcentaje: 20 },
        { criterio: "Rendimiento", porcentaje: 10 },
        { criterio: "Soportabilidad", porcentaje: 5 },
      ],
      McCall: [
        { criterio: "Corrección", porcentaje: 35 },
        { criterio: "Fiabilidad", porcentaje: 25 },
        { criterio: "Eficiencia", porcentaje: 20 },
        { criterio: "Integridad", porcentaje: 10 },
        { criterio: "Facilidad de Uso", porcentaje: 10 },
      ],
      "ISO 25000": [
        { criterio: "Adecuación Funcional", porcentaje: 30 },
        { criterio: "Eficiencia de Desempeño", porcentaje: 20 },
        { criterio: "Compatibilidad", porcentaje: 15 },
        { criterio: "Capacidad de Interacción", porcentaje: 15 },
        { criterio: "Fiabilidad", porcentaje: 10 },
        { criterio: "Seguridad", porcentaje: 10 },
      ],
      IEEE: [
        { criterio: "Funcionalidad", porcentaje: 35 },
        { criterio: "Confiabilidad", porcentaje: 25 },
        { criterio: "Mantenibilidad", porcentaje: 20 },
        { criterio: "Portabilidad", porcentaje: 10 },
        { criterio: "Rendimiento", porcentaje: 10 },
      ],
    },
    "Software Académico": {
      FURPS: [
        { criterio: "Funcionalidad", porcentaje: 30 },
        { criterio: "Usabilidad", porcentaje: 30 },
        { criterio: "Confiabilidad", porcentaje: 20 },
        { criterio: "Rendimiento", porcentaje: 10 },
        { criterio: "Soportabilidad", porcentaje: 10 },
      ],
      McCall: [
        { criterio: "Portabilidad", porcentaje: 30 },
        { criterio: "Flexibilidad", porcentaje: 25 },
        { criterio: "Facilidad de Uso", porcentaje: 20 },
        { criterio: "Mantenibilidad", porcentaje: 15 },
        { criterio: "Corrección", porcentaje: 10 },
      ],
      "ISO 25000": [
        { criterio: "Adecuación Funcional", porcentaje: 30 },
        { criterio: "Fiabilidad", porcentaje: 20 },
        { criterio: "Seguridad", porcentaje: 15 },
        { criterio: "Mantenibilidad", porcentaje: 20 },
        { criterio: "Protección", porcentaje: 15 },
      ],
      IEEE: [
        { criterio: "Funcionalidad", porcentaje: 30 },
        { criterio: "Portabilidad", porcentaje: 20 },
        { criterio: "Confiabilidad", porcentaje: 30 },
        { criterio: "Rendimiento", porcentaje: 10 },
        { criterio: "Mantenibilidad", porcentaje: 10 },
      ],
    },
  };

  const handleSelectSoftware = (e) => {
    setTipoSoftware(e.target.value);
    setNorma("");
    setCriterios([]);
  };

  const handleSelectNorma = (e) => {
    setNorma(e.target.value);
    setCriterios(criteriosPorNorma[tipoSoftware][e.target.value] || []);
  };

  const handleSubmitSoftware = (e) => {
    e.preventDefault();
    if (tipoSoftware) {
      setPaso(2);
    } else {
      alert("Por favor selecciona un tipo de software.");
    }
  };

  const handleSubmitNorma = (e) => {
    e.preventDefault();
    if (norma) {
      setPaso(3);
    } else {
      alert("Por favor selecciona una norma.");
    }
  };

  const handleSubmitEvaluacion = (e) => {
    e.preventDefault();

    const criteriosSeleccionados = criterios.map((criterio) => criterio.criterio);
    const preguntasEvaluacion = obtenerPreguntasPorNormaYCriterio(norma, criteriosSeleccionados, preguntas);

    const datosEvaluacion = {
      tipoSoftware,
      norma,
      criterios,
      preguntas: preguntasEvaluacion,
    };
    navigate("/evaluacionTabla", { state: datosEvaluacion }); // Redirige con datos
  };

  return (
    <div className="evaluacion-flujo">
      <h1>Realizar Evaluación</h1>

      {paso === 1 && (
        <form className="seleccionar-tipo-software" onSubmit={handleSubmitSoftware}>
          <label>Selecciona el Tipo de Software:</label>
          <select className="selector-tipo-software" value={tipoSoftware} onChange={handleSelectSoftware}>
            <option value="">Seleccione un tipo</option>
            <option value="Software Bancario">Software Bancario</option>
            <option value="Software Académico">Software Académico</option>
          </select>
          <button type="submit">Continuar</button>
        </form>
      )}

      {paso === 2 && (
        <form onSubmit={handleSubmitNorma}>
          <label>Selecciona la Norma:</label>
          <div className="normas">
            {["FURPS", "McCall", "ISO 25000", "IEEE"].map((normaOption) => (
              <div key={normaOption}>
                <input
                  type="radio"
                  id={normaOption}
                  name="norma"
                  value={normaOption}
                  onChange={handleSelectNorma}
                  checked={norma === normaOption}
                />
                <label htmlFor={normaOption}>{normaOption}</label>
              </div>
            ))}
          </div>
          <button type="submit">Continuar</button>
        </form>
      )}

      {paso === 3 && (
        <div className="criterios-container">
          <h2>Criterios Aplicados ({norma})</h2>
          <ul className="criterios-list">
            {criterios.map((criterio, index) => (
              <li key={index}>
                {criterio.criterio}: {criterio.porcentaje}%
              </li>
            ))}
          </ul>
          <button onClick={handleSubmitEvaluacion}>Guardar Evaluación</button>
        </div>
      )}
    </div>
  );
};

export default EvaluacionFlujo;
