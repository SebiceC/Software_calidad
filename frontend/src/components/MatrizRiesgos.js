import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/MatrizRiesgos.css";
import Navbar from "./Navbar";
import Footer from "./Footer";

const MatrizRiesgos = () => {
  const [mostrarMatriz, setMostrarMatriz] = useState(false);
  const [matrizGuardada, setMatrizGuardada] = useState(false);
  const [riesgos, setRiesgos] = useState([
    { codigo: "", descripcion: "", fase: "", causa: "", probabilidad: "", impacto: "" },
  ]);

  const navigate = useNavigate();

  const handleChange = (index, e) => {
    const newRiesgos = [...riesgos];
    newRiesgos[index][e.target.name] = e.target.value;
    setRiesgos(newRiesgos);
  };

  const addRow = () => {
    setRiesgos([
      ...riesgos,
      { codigo: "", descripcion: "", fase: "", causa: "", probabilidad: "", impacto: "" },
    ]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Aquí se simula el guardado en la base de datos
    console.log("Matriz de riesgos guardada:", riesgos);
    alert("Matriz de riesgos guardada con éxito.");

    // Marca como guardada para mostrar las opciones posteriores
    setMatrizGuardada(true);
  };

  const handleContinuar = () => {
    setMostrarMatriz(true);
  };

  const handleMatrizMitigacion = () => {
    navigate("/matriz-mitigacion", { state: { riesgos } });
  };

  return (
    <>
      <Navbar />
      <div className="matriz-riesgos-container">
        {!mostrarMatriz ? (
          <>
            <h1>Matriz de Riesgos</h1>
            <div className="tablas-informativas">
              <h2>Tabla 1: Niveles de Probabilidad</h2>
              <table className="tabla-probabilidad">
                <thead>
                  <tr>
                    <th>Nivel</th>
                    <th>Descriptor</th>
                    <th>Descripción</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>1</td>
                    <td>Raro</td>
                    <td>El evento puede ocurrir solo en circunstancias excepcionales.</td>
                  </tr>
                  <tr>
                    <td>2</td>
                    <td>Improbable</td>
                    <td>El evento podría ocurrir en algún momento.</td>
                  </tr>
                  <tr>
                    <td>3</td>
                    <td>Posible</td>
                    <td>El evento podría ocurrir en algún momento.</td>
                  </tr>
                  <tr>
                    <td>4</td>
                    <td>Probable</td>
                    <td>El evento probablemente ocurrirá en la mayoría de las circunstancias.</td>
                  </tr>
                  <tr>
                    <td>5</td>
                    <td>Casi Seguro</td>
                    <td>Se espera que el evento ocurra en la mayoría de las circunstancias.</td>
                  </tr>
                </tbody>
              </table>

              <h2>Tabla 2: Niveles de Impacto</h2>
              <table className="tabla-impacto">
                <thead>
                  <tr>
                    <th>Nivel</th>
                    <th>Descriptor</th>
                    <th>Descripción</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>1</td>
                    <td>Insignificante</td>
                    <td>Si el hecho llegara a presentarse, tendría consecuencias mínimas.</td>
                  </tr>
                  <tr>
                    <td>2</td>
                    <td>Menor</td>
                    <td>Si el hecho llegara a presentarse, tendría bajo impacto.</td>
                  </tr>
                  <tr>
                    <td>3</td>
                    <td>Moderado</td>
                    <td>Si el hecho llegara a presentarse, tendría impacto moderado.</td>
                  </tr>
                  <tr>
                    <td>4</td>
                    <td>Mayor</td>
                    <td>Si el hecho llegara a presentarse, tendría alto impacto.</td>
                  </tr>
                  <tr>
                    <td>5</td>
                    <td>Catastrófico</td>
                    <td>Si el hecho llegara a presentarse, tendría impacto catastrófico.</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <button onClick={handleContinuar} className="continuar-btn">
              Continuar
            </button>
          </>
        ) : (
          <div>
            <h1>Matriz de Riesgos</h1>
            <form onSubmit={handleSubmit}>
              <table className="tabla-riesgos">
                <thead>
                  <tr>
                    <th>Código</th>
                    <th>Descripción del Riesgo</th>
                    <th>Fase Afectada</th>
                    <th>Causa</th>
                    <th>Estimación Probabilidad</th>
                    <th>Estimación Impacto</th>
                  </tr>
                </thead>
                <tbody>
                  {riesgos.map((fila, index) => (
                    <tr key={index}>
                      <td>
                        <input
                          type="text"
                          name="codigo"
                          placeholder="Código"
                          value={fila.codigo}
                          onChange={(e) => handleChange(index, e)}
                        />
                      </td>
                      <td>
                        <input
                          type="text"
                          name="descripcion"
                          placeholder="Descripción del Riesgo"
                          value={fila.descripcion}
                          onChange={(e) => handleChange(index, e)}
                        />
                      </td>
                      <td>
                        <input
                          type="text"
                          name="fase"
                          placeholder="Fase Afectada"
                          value={fila.fase}
                          onChange={(e) => handleChange(index, e)}
                        />
                      </td>
                      <td>
                        <input
                          type="text"
                          name="causa"
                          placeholder="Causa"
                          value={fila.causa}
                          onChange={(e) => handleChange(index, e)}
                        />
                      </td>
                      <td>
                        <select
                          name="probabilidad"
                          value={fila.probabilidad}
                          onChange={(e) => handleChange(index, e)}
                        >
                          <option value="">Seleccione</option>
                          <option value="1">1 - Raro</option>
                          <option value="2">2 - Improbable</option>
                          <option value="3">3 - Posible</option>
                          <option value="4">4 - Probable</option>
                          <option value="5">5 - Casi Seguro</option>
                        </select>
                      </td>
                      <td>
                        <select
                          name="impacto"
                          value={fila.impacto}
                          onChange={(e) => handleChange(index, e)}
                        >
                          <option value="">Seleccione</option>
                          <option value="1">1 - Insignificante</option>
                          <option value="2">2 - Menor</option>
                          <option value="3">3 - Moderado</option>
                          <option value="4">4 - Mayor</option>
                          <option value="5">5 - Catastrófico</option>
                        </select>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
              <button type="button" onClick={addRow} className="agregar-fila-btn">
                Agregar Riesgo
              </button>
              <button type="submit" className="guardar-btn">
                Guardar Matriz
              </button>
            </form>
            {matrizGuardada && (
              <div className="acciones-matriz">
                <button onClick={handleMatrizMitigacion} className="matriz-mitigacion-btn">
                  Ir a Matriz de Mitigación
                </button>
              </div>
            )}
          </div>
        )}
      </div>
      <Footer />
    </>
  );
};

export default MatrizRiesgos;
