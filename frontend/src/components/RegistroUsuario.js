import React, { useState } from 'react';
import '../styles/RegistroUsuario.css';

const RegistroUsuario = () => {
  const [formData, setFormData] = useState({
    nombre: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (formData.password !== formData.confirmPassword) {
      alert('Las contraseñas no coinciden');
      return;
    }
    // Aquí puedes manejar el envío de datos (conexión a una API, por ejemplo)
    alert('Usuario registrado con éxito');
    console.log('Datos del formulario:', formData);
  };

  return (
    <div className="registro-container">
      <h1>Registrar Usuario</h1>
      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label htmlFor="nombre">Nombre completo</label>
          <input
            type="text"
            id="nombre"
            name="nombre"
            value={formData.nombre}
            onChange={handleChange}
            placeholder="Ingrese su nombre completo"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Correo Electrónico</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Ingrese su correo electrónico"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Contraseña</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            placeholder="Cree una contraseña"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="confirmPassword">Confirmar Contraseña</label>
          <input
            type="password"
            id="confirmPassword"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            placeholder="Confirme su contraseña"
            required
          />
        </div>
        <button type="submit" className="btn">
          Registrar
        </button>
      </form>
    </div>
  );
};

export default RegistroUsuario;
