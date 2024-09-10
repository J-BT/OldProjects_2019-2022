const width_threshold = 480;


function drawLineChart() {
  if ($("#lineChart").length) {
    ctxLine = document.getElementById("lineChart").getContext("2d");
    optionsLine = {
      scales: {
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "Quantité de matériel transférée"
            }
          }
        ]
      }
    };

    // Set aspect ratio based on window width
    optionsLine.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configLine = {
      type: "line",
      data: {
        labels: [
          "Janvier",
          "Fevrier",
          "Mars",
          "Avril",
          "Mai",
          "Juin",
          "Juillet",
          "Août",
          "Septembre",
          "Octobre",
          "Novembre",
          "Decembre"
        ],
        
        
        datasets: [
          {
            label: "Ambulatoire",
            data: [47,  1, 28, 69,  7, 97, 71, 98, 51, 30, 44, 39],
            fill: false,
            borderColor: "rgb(75, 192, 192)",
            lineTension: 0.1
          },
          {
            label: "Geriatrie",
            data: [21, 19, 36, 14, 53, 69, 42, 79, 41, 13, 23, 69],
            fill: false,
            borderColor: "rgba(255,99,132,1)",
            lineTension: 0.1
          },
          {
            label: "Chirurgie Ortho",
            data:[ 38,  54,  16,  98,  97, 100,  95,  34,  95,  73,  57,  60],
            fill: false,
            borderColor: "rgba(153, 102, 255, 1)",
            lineTension: 0.1
          },
          {
            label: "Gastro-Enterologie",
            data: [40, 29, 19, 94,  9, 88, 60, 38, 36, 21, 89, 26],
            fill: false,
            borderColor: "rgba(153, 102, 255, 1)",
            lineTension: 0.1
          },
          {
            label: "Cardiologie",
            data: [75, 20, 32, 71, 18, 55, 24, 62, 61, 18, 67, 23],
            fill: false,
            borderColor: "rgb(75, 192, 192)",
            lineTension: 0.1
          },
          {
            label: "USIC",
            data: [17, 95, 62, 87, 27, 32, 35, 54, 38, 71, 51, 88],
            fill: false,
            borderColor: "rgba(255,99,132,1)",
            lineTension: 0.1
          },
          {
            label: "Oncologie",
            data: [70, 11, 28, 80, 72, 63, 28, 58, 43, 87,  2, 76],
            fill: false,
            borderColor: "rgba(153, 102, 255, 1)",
            lineTension: 0.1
          },
          {
            label: "Vasculaire",
            data: [10, 61, 57,  7, 77, 26, 42, 34, 47, 11, 46, 52],
            fill: false,
            borderColor: "rgba(153, 102, 255, 1)",
            lineTension: 0.1
          },
          {
            label: "Chirurgie Digestive",
            data:[27, 33, 93, 56, 64,  5, 27, 35, 38, 61, 78, 59],
            fill: false,
            borderColor: "rgba(153, 102, 255, 1)",
            lineTension: 0.1
          },
          {
            label: "Maternite",
            data: [85, 26, 50, 98,  4, 11, 59, 40, 63, 61, 24, 56],
            fill: false,
            borderColor: "rgb(75, 192, 192)",
            lineTension: 0.1
          },
          {
            label: "Dialyse",
            data: [38, 42, 71, 73, 98, 46, 88, 78,  1, 12, 33, 72],
            fill: false,
            borderColor: "rgba(255,99,132,1)",
            lineTension: 0.1
          },
          {
            label: "Urgences",
            data: [56,  2, 53, 99, 22, 69, 43, 69, 46, 68,  7,  8],
            fill: false,
            borderColor: "rgba(153, 102, 255, 1)",
            lineTension: 0.1
          },
          {
            label: "USC",
            data: [89, 51, 43,  6, 88,  4, 67, 47, 71, 11, 55, 57],
            fill: false,
            borderColor: "rgba(153, 102, 255, 1)",
            lineTension: 0.1
          }
        ]
      },
      options: optionsLine
    }; 

    lineChart = new Chart(ctxLine, configLine);
  }
}

function drawBarChart() {
  if ($("#barChart").length) {
    ctxBar = document.getElementById("barChart").getContext("2d");

    optionsBar = {
      responsive: true,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: "Nombre d'unités transférées"
            }
          }
        ]
      }
    };

    optionsBar.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configBar = {
      type: "bar",
      data: {
        labels: ["Materiel 1", "Materiel 2", "Materiel 3",
         "Materiel 4", "Materiel 5", "Materiel 6",
         "Materiel 7", "Materiel 8", "Materiel 9",
         "Materiel 10",
         "Materiel 11", "Materiel 12", "Materiel 13",
         "Materiel 14", "Materiel 15", "Materiel 16",
         "Materiel 17", "Materiel 18", "Materiel 19",
         "Materiel 20",
         "Materiel 21", "Materiel 22", "Materiel 23",
         "Materiel 24", "Materiel 25", "Materiel 26",
         "Materiel 27", "Materiel 28", "Materiel 29",
         "Materiel 30",
         "Materiel 31", "Materiel 32", "Materiel 33",
         "Materiel 34", "Materiel 35", "Materiel 36",
         "Materiel 37", "Materiel 38", "Materiel 39",
         "Materiel 40",
         "Materiel 41", "Materiel 42", "Materiel 43",
         "Materiel 44", "Materiel 45", "Materiel 46",
         "Materiel 47", "Materiel 48", "Materiel 49",
         "Materiel 50",
         "Materiel 51", "Materiel 52"],
        datasets: [
          {
            label: "#Tout le matériel disponible",
            data: [12, 19, 3, 5, 2, 3, 12, 19, 3, 5,
            12, 19, 3, 5, 2, 3, 12, 19, 3, 5,
            12, 19, 3, 5, 2, 3, 12, 19, 3, 5,
            12, 19, 3, 5, 2, 3, 12, 19, 3, 5,
            12, 19, 3, 5, 2, 3, 12, 19, 3, 5,
            12, 19, 3, 5, 2, 3, 12, 19, 3, 5,
            12, 19],
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)"
            ],
            borderColor: [
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(255,99,132,1)",
              "rgba(54, 162, 235, 1)"
            ],
            borderWidth: 1
          }
        ]
      },
      options: optionsBar
    };

    barChart = new Chart(ctxBar, configBar);
  }
}

function drawPieChart() {
  if ($("#pieChart").length) {
    ctxPie = document.getElementById("pieChart").getContext("2d");
    optionsPie = {
      responsive: true,
      maintainAspectRatio: false
    };

    configPie = {
      type: "pie",
      data: {
        datasets: [
          {
            data: [40, 15, 35, 20],
            backgroundColor: [
              window.chartColors.purple,
              window.chartColors.green,
              window.chartColors.blue,
              window.chartColors.red
            ],
            label: "Pourcentage raisons"
          }
        ],
        labels: ["Casse", "Vol", "Defectueux", "Mise a niveau" ]

      },
      options: optionsPie
    };

    pieChart = new Chart(ctxPie, configPie);
  }
}

function updateChartOptions() {
  if ($(window).width() < width_threshold) {
    if (optionsLine) {
      optionsLine.maintainAspectRatio = false;
    }
    if (optionsBar) {
      optionsBar.maintainAspectRatio = false;
    }
  } else {
    if (optionsLine) {
      optionsLine.maintainAspectRatio = true;
    }
    if (optionsBar) {
      optionsBar.maintainAspectRatio = true;
    }
  }
}

function updateLineChart() {
  if (lineChart) {
    lineChart.options = optionsLine;
    lineChart.update();
  }
}

function updateBarChart() {
  if (barChart) {
    barChart.options = optionsBar;
    barChart.update();
  }
}

function reloadPage() {
  setTimeout(function() {
    window.location.reload();
  }); // Reload the page so that charts will display correctly
}

function drawCalendar() {
  if ($("#calendar").length) {
    $("#calendar").fullCalendar({
      height: 400,
      events: [
        {
          title: "Meeting",
          start: "2018-09-1",
          end: "2018-09-2"
        },
        {
          title: "Marketing trip",
          start: "2018-09-6",
          end: "2018-09-8"
        },
        {
          title: "Follow up",
          start: "2018-10-12"
        },
        {
          title: "Team",
          start: "2018-10-17"
        },
        {
          title: "Company Trip",
          start: "2018-10-25",
		  end: "2018-10-27"
        },
        {
          title: "Review",
          start: "2018-11-12"
        },
        {
          title: "Plan",
          start: "2018-11-18"
        }
      ],
      eventColor: "rgba(54, 162, 235, 0.4)"
    });
  }
}
