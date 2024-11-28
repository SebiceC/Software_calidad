import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Navbar.css';


const Navbar = () => {
    return (
      <nav className="navbar">

        <ul className="navbar-links">
          <li>
            <Link to="/UserHome">Inicio</Link>
          </li>
          <li>
            <Link to="/empresa">Registrar Empresa</Link>
          </li>
          <li>
            <Link to="/evaluacion">Realizar Evaluación</Link>
          </li>
          <li>
            <Link to="/resultados">Resultados</Link>
          </li>
          <li>
            <Link to="/matriz-riesgos">Matriz de Riesgos</Link>
          </li>
        </ul>
      </nav>
    );
  };
  
  export default Navbar;
  