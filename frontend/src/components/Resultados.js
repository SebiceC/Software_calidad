import React from 'react';

const Resultados = () => {
  return (
    <div>
      <h1>Resultados</h1>
      <table>
        <thead>
          <tr>
            <th>Fecha</th>
            <th>Empresa</th>
            <th>Evaluador</th>
            <th>Resultado</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>2023-11-01</td>
            <td>Empresa X</td>
            <td>Usuario A</td>
            <td>Aprobado</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default Resultados;
