import React, { useState } from "react";
import { useLocation } from "react-router-dom";
import "../styles/EvaluacionTabla.css";

const EvaluacionTabla = () => {
  const location = useLocation();
  const { tipoSoftware, norma, criterios } = location.state || {
    tipoSoftware: "Desconocido",
    norma: "Desconocida",
    criterios: [],
  };

  const [valores, setValores] = useState({});
  const [observaciones, setObservaciones] = useState({});

  const handleValorChange = (criterio, value) => {
    setValores((prev) => ({
      ...prev,
      [criterio]: value,
    }));
  };

  const handleObservacionesChange = (criterio, value) => {
    setObservaciones((prev) => ({
      ...prev,
      [criterio]: value,
    }));
  };

  const handleGuardarEvaluacion = () => {
    const resultados = criterios.map((criterio) => ({
      criterio: criterio.criterio,
      valor: valores[criterio.criterio] || 0,
      observacion: observaciones[criterio.criterio] || "",
    }));

    console.log("Evaluación guardada:", {
      tipoSoftware,
      norma,
      resultados,
    });

    alert("Evaluación guardada con éxito.");
  };

  return (
    <div className="evaluacion-tabla-container">
      <h1>Evaluación de {norma}</h1>
      <h2>Software: {tipoSoftware}</h2>
      <table className="evaluacion-tabla">
        <thead>
          <tr>
            <th>Ítem</th>
            <th>Descripción</th>
            <th>Valor</th>
            <th>Observaciones</th>
          </tr>
        </thead>
        <tbody>
          {criterios.map((criterio, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{criterio.descripcion}</td>
              <td>
                <input
                  type="number"
                  min="0"
                  max="100"
                  value={valores[criterio.criterio] || ""}
                  onChange={(e) =>
                    handleValorChange(criterio.criterio, e.target.value)
                  }
                />
              </td>
              <td>
                <input
                  type="text"
                  value={observaciones[criterio.criterio] || ""}
                  onChange={(e) =>
                    handleObservacionesChange(criterio.criterio, e.target.value)
                  }
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={handleGuardarEvaluacion} className="guardar-btn">
        Guardar Evaluación
      </button>
    </div>
  );
};

export default EvaluacionTabla;
