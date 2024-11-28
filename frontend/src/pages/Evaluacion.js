import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../styles/Evaluacion.css";
import preguntas from "../data/preguntas.json";
import { obtenerPreguntasPorNormaYCriterio } from "../utils/utils";

const EvaluacionFlujo = () => {
  const [paso, setPaso] = useState(1);
  const [tipoSoftware, setTipoSoftware] = useState("");
  const [norma, setNorma] = useState("");
  const [criterios, setCriterios] = useState([]);
  const [empresas, setEmpresas] = useState([]);
  const [empresaSeleccionada, setEmpresaSeleccionada] = useState(""); // Estado para la empresa seleccionada
  const [nombreSoftware, setNombreSoftware] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    axios
      .get("http://localhost:5000/compañias")
      .then((response) => {
        console.log(response.data);
        setEmpresas(response.data.empresas); // Actualiza el estado con las empresas
      })
      .catch((error) => {
        console.error("Error al obtener las empresas:", error);
      });
  }, []);

  useEffect(() => {
    const empresa = empresas.find((empresa) => empresa.id_empresa === empresaSeleccionada);
    
    if (empresa) {
      setNombreSoftware(empresa.nombre_software);
      console.log("Software seleccionado:", empresa.nombre_software); // Este log debería aparecer aquí
    }
  }, [empresaSeleccionada, empresas]);  // Este useEffect se dispara cuando `empresaSeleccionada` o `empresas` cambian
  
  

  const criteriosPorNorma = {
    "Software Bancario": {
      FURPS: [
        { criterio: "Funcionalidad", porcentaje: 40 },
        { criterio: "Usabilidad", porcentaje: 25 },
        { criterio: "Confiabilidad", porcentaje: 20 },
        { criterio: "Rendimiento", porcentaje: 10 },
        { criterio: "Soportabilidad", porcentaje: 5 },
      ],
      McCall: [
        { criterio: "Corrección", porcentaje: 35 },
        { criterio: "Fiabilidad", porcentaje: 25 },
        { criterio: "Eficiencia", porcentaje: 20 },
        { criterio: "Integridad", porcentaje: 10 },
        { criterio: "Facilidad de Uso", porcentaje: 10 },
      ],
      "ISO 25000": [
        { criterio: "Adecuación Funcional", porcentaje: 30 },
        { criterio: "Eficiencia de Desempeño", porcentaje: 20 },
        { criterio: "Compatibilidad", porcentaje: 15 },
        { criterio: "Capacidad de Interacción", porcentaje: 15 },
        { criterio: "Fiabilidad", porcentaje: 10 },
        { criterio: "Seguridad", porcentaje: 10 },
      ],
      IEEE: [
        { criterio: "Funcionalidad", porcentaje: 35 },
        { criterio: "Confiabilidad", porcentaje: 25 },
        { criterio: "Mantenibilidad", porcentaje: 20 },
        { criterio: "Portabilidad", porcentaje: 10 },
        { criterio: "Rendimiento", porcentaje: 10 },
      ],
    },
    "Software Académico": {
      FURPS: [
        { criterio: "Funcionalidad", porcentaje: 30 },
        { criterio: "Usabilidad", porcentaje: 30 },
        { criterio: "Confiabilidad", porcentaje: 20 },
        { criterio: "Rendimiento", porcentaje: 10 },
        { criterio: "Soportabilidad", porcentaje: 10 },
      ],
      McCall: [
        { criterio: "Portabilidad", porcentaje: 30 },
        { criterio: "Flexibilidad", porcentaje: 25 },
        { criterio: "Facilidad de Uso", porcentaje: 20 },
        { criterio: "Mantenibilidad", porcentaje: 15 },
        { criterio: "Corrección", porcentaje: 10 },
      ],
      "ISO 25000": [
        { criterio: "Adecuación Funcional", porcentaje: 30 },
        { criterio: "Fiabilidad", porcentaje: 20 },
        { criterio: "Seguridad", porcentaje: 15 },
        { criterio: "Mantenibilidad", porcentaje: 20 },
        { criterio: "Protección", porcentaje: 15 },
      ],
      IEEE: [
        { criterio: "Funcionalidad", porcentaje: 30 },
        { criterio: "Portabilidad", porcentaje: 20 },
        { criterio: "Confiabilidad", porcentaje: 30 },
        { criterio: "Rendimiento", porcentaje: 10 },
        { criterio: "Mantenibilidad", porcentaje: 10 },
      ],
    },
  };

  const handleSelectSoftware = (e) => {
    setTipoSoftware(e.target.value);
    setNorma("");
    setCriterios([]);
  };

  const handleSelectNorma = (e) => {
    setNorma(e.target.value);
    setCriterios(criteriosPorNorma[tipoSoftware][e.target.value] || []);
  };

  const handleSubmitSoftware = (e) => {
    e.preventDefault();
    if (tipoSoftware) {
      setPaso(3);
    } else {
      alert("Por favor selecciona un tipo de software.");
    }
  };

  const handleSubmitNorma = (e) => {
    e.preventDefault();
    if (norma) {
      setPaso(4);
    } else {
      alert("Por favor selecciona una norma.");
    }
  };

  const handleSubmitEvaluacion = (e) => {
    e.preventDefault();

    const criteriosSeleccionados = criterios.map((criterio) => criterio.criterio);
    const preguntasEvaluacion = obtenerPreguntasPorNormaYCriterio(norma, criteriosSeleccionados, preguntas);

    const datosEvaluacion = {
      tipoSoftware,
      norma,
      criterios,
      preguntas: preguntasEvaluacion,
    };
    navigate("/evaluacionTabla", { state: datosEvaluacion }); // Redirige con datos
  };

  // Definir las funciones faltantes
  const handleSelectEmpresa = (e) => {
    const selectedEmpresaId = e.target.value;
    console.log("ID de empresa seleccionada:", selectedEmpresaId);  // Verifica el ID seleccionado
  
    // Verifica que el ID de empresa no esté vacío
    if (selectedEmpresaId !== "") {
      setEmpresaSeleccionada(selectedEmpresaId);  // Actualiza el estado de la empresa seleccionada
    } else {
      setNombreSoftware("");  // Si no hay empresa seleccionada, resetea el software
    }
  };
  
  

  const handleSubmitEmpresa = (e) => {
    e.preventDefault();
    if (empresaSeleccionada) {
      setPaso(2); // Continúa al siguiente paso
    } else {
      alert("Por favor selecciona una empresa.");
    }
  };

  return (
    <div className="evaluacion-flujo">
      <h1>Realizar Evaluación</h1>

      {paso === 1 && (
        <form onSubmit={handleSubmitEmpresa}>
          <label>Selecciona la Empresa:</label>
          <select value={empresaSeleccionada} onChange={handleSelectEmpresa}>
            <option value="">Seleccione una empresa</option>
            {empresas.map((empresa) => (
              <option key={empresa.id_empresa} value={empresa.id_empresa}>
                {empresa.nombre}
              </option>
            ))}
          </select>
          {empresaSeleccionada && (
            <div>
              <p><strong>Software seleccionado:</strong> {nombreSoftware}</p>
            </div>
          )}
          <button type="submit">Continuar</button>
        </form>
      )}

      {paso === 2 && (
        <form className="seleccionar-tipo-software" onSubmit={handleSubmitSoftware}>
          <label>Selecciona el Tipo de Software:</label>
          <select className="selector-tipo-software" value={tipoSoftware} onChange={handleSelectSoftware}>
            <option value="">Seleccione un tipo</option>
            <option value="Software Bancario">Software Bancario</option>
            <option value="Software Académico">Software Académico</option>
          </select>
          <button type="submit">Continuar</button>
        </form>
      )}

      {paso === 3 && (
        <form onSubmit={handleSubmitNorma}>
          <label>Selecciona la Norma:</label>
          <div className="normas">
            {["FURPS", "McCall", "ISO 25000", "IEEE"].map((normaOption) => (
              <div key={normaOption}>
                <input
                  type="radio"
                  id={normaOption}
                  name="norma"
                  value={normaOption}
                  onChange={handleSelectNorma}
                  checked={norma === normaOption}
                />
                <label htmlFor={normaOption}>{normaOption}</label>
              </div>
            ))}
          </div>
          <button type="submit">Continuar</button>
        </form>
      )}

      {paso === 4 && (
        <div className="criterios-container">
          <h2>Criterios Aplicados ({norma})</h2>
          <ul className="criterios-list">
            {criterios.map((criterio, index) => (
              <li key={index}>
                {criterio.criterio}: {criterio.porcentaje}%
              </li>
            ))}
          </ul>
          <button onClick={handleSubmitEvaluacion}>Evaluar</button>
        </div>
      )}
    </div>
  );
};

export default EvaluacionFlujo;
