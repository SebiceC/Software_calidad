import './styles/App.css';
import RegistroUsuario from './components/RegistroUsuario';
import Login from './components/Login';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import EmpresaForm from './components/EmpresaForm';
import SeleccionarActividad from './components/SeleccionarActividad';
import Evaluacion from './pages/Evaluacion';
import Resultados from './components/Resultados';
import MatrizRiesgos from './components/MatrizRiesgos';
import MatrizMitigacionRiesgos from './components/MatrizMitigacionRiesgos';
import EliminarDatos from './components/EliminarDatos';
import UserHome from './pages/UserHome';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import EvaluacionTabla from './components/EvaluacionTabla';


function App() {
  return (
    <Router>
      <div>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<RegistroUsuario />} />
        <Route path="/empresa" element={<EmpresaForm />} />
        <Route path="/actividad" element={<SeleccionarActividad />} />
        <Route path="/evaluacion" element={<Evaluacion />} />
        <Route path="/resultados" element={<Resultados />} />
        <Route path="/matriz-riesgos" element={<MatrizRiesgos />} />
        <Route path="/matriz-mitigacion" element={<MatrizMitigacionRiesgos />} />
        <Route path="/eliminar" element={<EliminarDatos />} />
        <Route path='/UserHome' element={<UserHome />} />
        <Route path='/login' element={<Login />} />
        <Route path='/EvaluacionTabla' element={<EvaluacionTabla />} />
      </Routes>
      </div>
    </Router>
  );
}

export default App;
