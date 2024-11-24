import React, { useState } from 'react';
import "../styles/EmpresaForm.css";

const EmpresaForm = () => {
  const [empresa, setEmpresa] = useState({
    nombre: '',
    direccion: '',
    telefono: '',
    email: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setEmpresa({ ...empresa, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Datos de la empresa:', empresa);
    alert('Empresa registrada con éxito');
    // Aquí puedes enviar los datos a un backend
  };

  return (
    <div className='empresa-form'>
      <h1>Registrar Empresa</h1>
      <form onSubmit={handleSubmit}>
        <label>Nombre:</label>
        <input name="nombre" value={empresa.nombre} onChange={handleChange} />
        <label>Dirección:</label>
        <input name="direccion" value={empresa.direccion} onChange={handleChange} />
        <label>Teléfono:</label>
        <input name="telefono" value={empresa.telefono} onChange={handleChange} />
        <label>Email:</label>
        <input name="email" value={empresa.email} onChange={handleChange} />
        <button type="submit">Guardar</button>
      </form>
    </div>
  );
};

export default EmpresaForm;
