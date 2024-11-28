import React, { useEffect, useState } from 'react';
import '../styles/Matrices.css';

const Matrices = () => {
  const [matrizRiesgo, setMatrizRiesgo] = useState([]);
  const [matrizMitigacion, setMatrizMitigacion] = useState([]);
  const [error, setError] = useState(null);
  const [cargando, setCargando] = useState(true);
  const nivelesProbabilidad = {
    1: 'Raro',
    2: 'Improbable',
    3: 'Posible',
    4: 'Probable',
    5: 'Casi Seguro',
  };
  
  const nivelesImpacto = {
    1: 'Insignificante',
    2: 'Menor',
    3: 'Moderado',
    4: 'Mayor',
    5: 'Catastrófico',
  };
  useEffect(() => {
    const fetchData = async () => {
      try {
        const respuestaRiesgo = await fetch('http://localhost:5000/api/matriz-riesgo');
        if (!respuestaRiesgo.ok) throw new Error('Error al cargar la matriz de riesgo');
        const dataRiesgo = await respuestaRiesgo.json();
        setMatrizRiesgo(dataRiesgo);

        const respuestaMitigacion = await fetch('http://localhost:5000/api/matriz-mitigacion');
        if (!respuestaMitigacion.ok) throw new Error('Error al cargar la matriz de mitigación');
        const dataMitigacion = await respuestaMitigacion.json();
        setMatrizMitigacion(dataMitigacion);
      } catch (err) {
        setError(err.message);
      } finally {
        setCargando(false);
      }
    };

    fetchData();
  }, []);

  if (cargando) return <p>Cargando...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>Matrices de Riesgo y Mitigación</h1>

      <h2>Matriz de Riesgo</h2>
      <table border="1" style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th>Descripción del Riesgo</th>
            <th>Fase</th>
            <th>Probabilidad</th>
            <th>Impacto</th>
            <th>Nivel de Riesgo</th>
          </tr>
        </thead>
        <tbody>
          {matrizRiesgo.length > 0 ? (
            matrizRiesgo.map((riesgo, index) => (
              <tr key={index}>
                <td>{riesgo.descripcion_riesgo}</td>
                <td>{riesgo.fase}</td>
                <td>{nivelesProbabilidad[riesgo.probabilidad]}</td>
                <td data-risk={riesgo.nivel_riesgo}>{riesgo.nivel_riesgo}</td>
                <td>{riesgo.nivel_riesgo}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="5">No hay datos disponibles en la Matriz de Riesgo</td>
            </tr>
          )}
        </tbody>
      </table>

      <h2>Matriz de Mitigación de Riesgos</h2>
      <table border="1" style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th>Amenaza/Oportunidad</th>
            <th>Descripción del Riesgo</th>
            <th>Fase</th>
            <th>Nivel de Riesgo</th>
            <th>Tipo de Respuesta</th>
            <th>Responsable</th>
            <th>Plan de Mitigación</th>
          </tr>
        </thead>
        <tbody>
          {matrizMitigacion.length > 0 ? (
            matrizMitigacion.map((mitigacion, index) => (
              <tr key={index}>
                <td>{mitigacion.amenaza_oportunidad}</td>
                <td>{mitigacion.descripcion_riesgo}</td>
                <td>{mitigacion.fase}</td>
                <td data-risk={mitigacion.nivel_riesgo}>{mitigacion.nivel_riesgo}</td>
                <td>{mitigacion.tipo_respuesta}</td>
                <td>{mitigacion.responsable}</td>
                <td>{mitigacion.plan_mitigacion}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="7">No hay datos disponibles en la Matriz de Mitigación</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Matrices;
