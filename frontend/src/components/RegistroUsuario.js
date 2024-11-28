import React, { useState } from 'react';
import '../styles/RegistroUsuario.css';
import { useNavigate } from 'react-router-dom';

const RegistroUsuario = () => {
  const [formData, setFormData] = useState({
    nombre: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const [error, setError] = useState(null); // Para manejar errores
  const [loading, setLoading] = useState(false); // Para mostrar el estado de carga
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      alert('Las contraseñas no coinciden');
      return;
    }

    setLoading(true); // Mostrar que la solicitud está en curso

    // Aquí construimos el cuerpo de la solicitud (con los datos del formulario)
    const data = {
      nombre: formData.nombre,
      correo: formData.email,
      contraseña: formData.password,
      rol: 'Usuario', // Asignar un rol por defecto (puedes cambiarlo si tienes un campo para ello)
    };

    try {
      // Realizar la solicitud POST al backend
      const response = await fetch('http://localhost:5000/usuarios', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Hubo un error al registrar al usuario');
      }

      const result = await response.json();

      // Verificamos si hubo un error en el backend
      if (result.error) {
        setError(result.error);
        alert('Error al registrar usuario: ' + result.error);
      } else {
        alert('Usuario registrado con éxito');
        console.log('Usuario registrado:', result);
        // Limpiar el formulario si la inserción fue exitosa
        setFormData({
          nombre: '',
          email: '',
          password: '',
          confirmPassword: '',
        });

        navigate('/Login');

      }
    } catch (err) {
      setError(err.message);
      alert('Error en la conexión: ' + err.message);
    } finally {
      setLoading(false); // Ocultar el estado de carga
    }
  };

  return (
    <div className="registro-container">
      <h1>Registrar Usuario</h1>
      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label htmlFor="nombre">Nombre completo</label>
          <input
            className='input-registrar-usuario'
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
            className='input-registrar-usuario'
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
            className='input-registrar-usuario'
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
            className='input-registrar-usuario'
            type="password"
            id="confirmPassword"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            placeholder="Confirme su contraseña"
            required
          />
        </div>
        <button type="submit" className="btn" disabled={loading}>
          {loading ? 'Registrando...' : 'Registrar'}
        </button>
        {error && <div className="error-message">{error}</div>}
      </form>
    </div>
  );
};

export default RegistroUsuario;
