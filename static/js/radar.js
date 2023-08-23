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
    scale: {
      ticks: {
        beginAtZero: true,
      },
    },
    legend: {
      display: false, // Define para "false" para remover a legenda
    },
  };

  // 3. Criação do gráfico de radar
  const radarChart = new Chart(document.getElementById('radar-chart'), {
    type: 'radar',
    data: dataRadar,
    options: options,
  });
}
