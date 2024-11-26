import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/UserHome.css';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

const UserHome = ({ usuario }) => {
  return (
    <>
    <Navbar />
    <div className="home-container">
      <header className="home-header">
        <h1>Bienvenido, {usuario || 'Usuario'}</h1>
        <p>¿Qué deseas hacer hoy?</p>
      </header>

      <div className="home-actions">
        <Link to="/empresa" className="action-card">
          <h3>Registrar Empresa</h3>
          <p>Registra los datos de la empresa que deseas evaluar.</p>
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
      </div>
    </div>
    <Footer />
    </>
  );
};

export default UserHome;
