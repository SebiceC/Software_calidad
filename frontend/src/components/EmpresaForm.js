import React, { useState } from 'react';
import "../styles/EmpresaForm.css"; // Asegúrate de que el archivo CSS esté en la ruta correcta
import Navbar from './Navbar';
import Footer from './Footer';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const EmpresaForm = () => {
  const [formData, setFormData] = useState({
    nombre: '',
    nombre_software: '',
    ciudad: '',
    telefono: '',
    email: '',
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/register_company', formData);
      alert(response.data.message);  // Mostrar mensaje de éxito
      navigate('/UserHome');
    } catch (error) {
      alert('Hubo un error al registrar la empresa');
    }
  };

  return (
    <>
      <Navbar />
      <div className="empresa-form-container">
        <div className="empresa-form">
          <h1>Registrar Empresa</h1>
          <form onSubmit={handleSubmit}>
            <label>Nombre:</label>
            <input
              name="nombre"
              value={formData.nombre}
              onChange={handleChange}
            />
            <label>Nombre del software:</label>
            <input
              name="nombre_software"
              value={formData.nombre_software}
              onChange={handleChange}
            />
            <label>Ciudad:</label>
            <input
              name="ciudad"
              value={formData.ciudad}
              onChange={handleChange}
            />
            <label>Teléfono:</label>
            <input
              name="telefono"
              value={formData.telefono}
              onChange={handleChange}
            />
            <label>Email:</label>
            <input
              name="email"
              value={formData.email}
              onChange={handleChange}
            />
            <button type="submit">Guardar</button>
          </form>
        </div>
      </div>
      <Footer />
    </>
  );
};

export default EmpresaForm;
