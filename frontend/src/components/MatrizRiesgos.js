import React, { useState } from 'react';

const MatrizRiesgos = () => {
  const [riesgos, setRiesgos] = useState([{ riesgo: '', impacto: '' }]);

  const handleChange = (index, e) => {
    const newRiesgos = [...riesgos];
    newRiesgos[index][e.target.name] = e.target.value;
    setRiesgos(newRiesgos);
  };

  const addRow = () => {
    setRiesgos([...riesgos, { riesgo: '', impacto: '' }]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Matriz de riesgos:', riesgos);
    alert('Matriz guardada con éxito');
  };

  return (
    <div>
      <h1>Matriz de Riesgos</h1>
      <form onSubmit={handleSubmit}>
        {riesgos.map((fila, index) => (
          <div key={index}>
            <input
              type="text"
              name="riesgo"
              placeholder="Riesgo"
              value={fila.riesgo}
              onChange={(e) => handleChange(index, e)}
            />
            <input
              type="text"
              name="impacto"
              placeholder="Impacto"
              value={fila.impacto}
              onChange={(e) => handleChange(index, e)}
            />
          </div>
        ))}
        <button type="button" onClick={addRow}>Agregar Riesgo</button>
        <button type="submit">Guardar Matriz</button>
      </form>
    </div>
  );
};

export default MatrizRiesgos;
