function createRadarChart(labels, data) {
  // 1. Configuração dos dados do gráfico
  const dataRadar = {
    labels: labels,
    datasets: [
      {
        label: 'Conhecimento',
        data: data,
      },
    ],
  };

  // 2. Configuração das opções do gráfico
  const options = {
    scales: {
      r: {
        beginAtZero: true,
        min: 0,
        max: 100,
        ticks: {
          display: false,
          stepSize: 20,
        },
        grid: {
          color: 'rgba(0, 0, 0, 1)', // Define a cor da grade
        },
        angleLines: {
          color: 'rgba(0, 0, 0, 1)', // Define a cor dos eixos radiais
        },
        pointLabels: {
          color : 'rgba(255, 255, 255, 1)',
          font: {
            size: 20, // Define o tamanho da fonte das point labels
          },
        },
      },
    },
    plugins: {
      legend: {
        display:false
      },
    }
  };

  // 3. Criação do gráfico de radar
  const radarChart = new Chart(document.getElementById('radar-chart'), {
    type: 'radar',
    data: dataRadar,
    options: options,
  });
}
