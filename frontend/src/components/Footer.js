import React from 'react';
import '../styles/Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <p>&copy; {new Date().getFullYear()} Software de Calidad. Todos los derechos reservados.</p>
      <p>
        <a href="https://github.com/" target="_blank" rel="noopener noreferrer">
          GitHub
        </a>{" "}
        |{" "}
        <a href="https://www.linkedin.com/" target="_blank" rel="noopener noreferrer">
          LinkedIn
        </a>
      </p>
    </footer>
  );
};

export default Footer;
