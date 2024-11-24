import React from 'react';

const Evaluacion = () => {
  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Evaluación guardada con éxito');
  };

  return (
    <div>
      <h1>Realizar Evaluación</h1>
      <form onSubmit={handleSubmit}>
        <label>Criterio 1:</label>
        <input type="text" name="criterio1" placeholder="Calificación" />
        <label>Criterio 2:</label>
        <input type="text" name="criterio2" placeholder="Calificación" />
        <button type="submit">Guardar Evaluación</button>
      </form>
    </div>
  );
};

export default Evaluacion;
