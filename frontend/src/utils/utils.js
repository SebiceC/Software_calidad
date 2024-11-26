export const obtenerPreguntasPorNormaYCriterio = (norma, criteriosSeleccionados, preguntas) => {
    const preguntasNorma = preguntas[norma];
    const preguntasSeleccionadas = [];
  
    criteriosSeleccionados.forEach((criterio) => {
      if (preguntasNorma[criterio]) {
        preguntasSeleccionadas.push(...preguntasNorma[criterio]);
      }
    });
  
    return preguntasSeleccionadas;
  };
  