window.onload = function() {


var config = {
            type: 'line',
            data: {
                labels: ["January", "February", "March", "April", "May", "June", "July"],
                datasets: [{
                        label: "My First dataset",
                        data: [10, 80, 56, 60, 6, 45, 15],
                        fill: false,
                        backgroundColor: "#eebcde ",
                        borderColor: "#eebcde",
                        borderCapStyle: 'butt',
                        borderDash: [5, 5],
                    }]
            },
            options: {
                responsive: true,
                legend: {
                    position: 'bottom',
                },
                hover: {
                    mode: 'label'
                },
                scales: {
                    xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Month'
                            }
                        }],
                    yAxes: [{
                            display: true,
                            ticks: {
                                beginAtZero: true,
                                steps: 10,
                                stepValue: 5,
                                max: 100
                            }
                        }]
                },
                title: {
                    display: true,
                    text: 'Chart.js Line Chart - Legend'
                }
            }
        };

        var ctx = document.getElementById("canvas").getContext("2d");
       new Chart(ctx, config);

}