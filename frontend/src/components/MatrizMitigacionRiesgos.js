import React, { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import "../styles/MatrizMitigacion.css";
import Navbar from "./Navbar";
import Footer from "./Footer";

const MatrizMitigacion = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const riesgos = location.state?.riesgos || []; // Maneja el caso en que no se pasen riesgos

  const [mitigaciones, setMitigaciones] = useState(
    riesgos.map((riesgo) => ({
      codigo: riesgo.codigo,
      descripcion: riesgo.descripcion,
      fase: riesgo.fase,
      nivelRiesgo: riesgo.nivelRiesgo,
      tipoRespuesta: "",
      responsable: "",
      planMitigacion: "",
    }))
  );

  const handleChange = (index, e) => {
    const newMitigaciones = [...mitigaciones];
    newMitigaciones[index][e.target.name] = e.target.value;
    setMitigaciones(newMitigaciones);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Matriz de mitigación:", mitigaciones);
    alert("Matriz de Mitigación guardada con éxito");
  };

  const handleVolverInicio = () => {
    navigate("/UserHome");
  };

  if (riesgos.length === 0) {
    return <div>No hay riesgos disponibles para la matriz de mitigación.</div>;
  }

  return (
    <>
      <Navbar />
      <div className="matriz-mitigacion-container">
        <h1>Matriz de Mitigación</h1>
        <form onSubmit={handleSubmit}>
          <table className="tabla-mitigacion">
            <thead>
              <tr>
                <th>Código del Riesgo</th>
                <th>Descripción del Riesgo</th>
                <th>Fase Afectada</th>
                <th>Nivel de Riesgo</th>
                <th>Tipo de Respuesta</th>
                <th>Responsable</th>
                <th>Plan de Mitigación</th>
              </tr>
            </thead>
            <tbody>
              {mitigaciones.map((fila, index) => (
                <tr key={index}>
                  <td>{fila.codigo}</td>
                  <td>{fila.descripcion}</td>
                  <td>{fila.fase}</td>
                  <td>{fila.nivelRiesgo}</td>
                  <td>
                    <select
                      name="tipoRespuesta"
                      value={fila.tipoRespuesta}
                      onChange={(e) => handleChange(index, e)}
                    >
                      <option value="">Seleccione</option>
                      <option value="Mitigar">Mitigar</option>
                      <option value="Evitar">Evitar</option>
                      <option value="Transferir">Transferir</option>
                      <option value="Aceptar">Aceptar</option>
                    </select>
                  </td>
                  <td>
                    <input
                      type="text"
                      name="responsable"
                      placeholder="Responsable"
                      value={fila.responsable}
                      onChange={(e) => handleChange(index, e)}
                    />
                  </td>
                  <td>
                    <input
                      type="text"
                      name="planMitigacion"
                      placeholder="Plan de Mitigación"
                      value={fila.planMitigacion}
                      onChange={(e) => handleChange(index, e)}
                    />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <button type="submit" className="guardar-btn">
            Guardar Matriz de Mitigación
          </button>
          <button onClick={handleVolverInicio} className="inicio-btn">
            Volver al Inicio
          </button>
        </form>
      </div>
      <Footer />
    </>
  );
};

export default MatrizMitigacion;
