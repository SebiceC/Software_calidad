import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/UserHome.css';

const AdminHome = ({ usuario }) => {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Bienvenido, {usuario || 'Administrador'}</h1>
        <p>¿Qué deseas hacer hoy?</p>
      </header>

      <div className="home-actions">
        <Link to="/empresa" className="action-card">
          <h3>Registrar Empresa</h3>
          <p>Registra los datos de la empresa que deseas evaluar.</p>
        </Link>
        <Link to="/actividad" className="action-card">
          <h3>Seleccionar Actividad</h3>
          <p>Selecciona la actividad que realiza la empresa.</p>
        </Link>
        <Link to="/evaluacion" className="action-card">
          <h3>Realizar Evaluación</h3>
          <p>Evalúa el software de acuerdo a los modelos de calidad.</p>
        </Link>
        <Link to="/resultados" className="action-card">
          <h3>Ver Resultados</h3>
          <p>Consulta los resultados de las evaluaciones realizadas.</p>
        </Link>
        <Link to="/matriz-riesgos" className="action-card">
          <h3>Matriz de Riesgos</h3>
          <p>Gestiona y analiza los riesgos de la empresa.</p>
        </Link>
        <Link to="/matriz-mitigacion" className="action-card">
          <h3>Matriz de Mitigación</h3>
          <p>Crea y administra la matriz de mitigación de riesgos.</p>
        </Link>
      </div>
    </div>
  );
};

export default AdminHome;
