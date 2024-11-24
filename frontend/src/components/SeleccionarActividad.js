import React, { useState } from 'react';

const SeleccionarActividad = () => {
  const [actividad, setActividad] = useState('');

  const handleSelect = (e) => {
    setActividad(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Actividad seleccionada:', actividad);
    alert('Actividad registrada con éxito');
  };

  return (
    <div>
      <h1>Seleccionar Actividad</h1>
      <form onSubmit={handleSubmit}>
        <label>Actividad:</label>
        <select value={actividad} onChange={handleSelect}>
          <option value="">Seleccione una actividad</option>
          <option value="Tecnología">Tecnología</option>
          <option value="Educación">Educación</option>
          <option value="Salud">Salud</option>
        </select>
        <button type="submit">Guardar</button>
      </form>
    </div>
  );
};

export default SeleccionarActividad;
