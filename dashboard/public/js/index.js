window.onload = function() {
  var val = 5000;
  var minDate = new Date(val);

  // call function from 'readData.js' to import data
  var datasets = getDataSet();

  // set graphing options
  var options = {
  responsive: true,
    scales: {
      xAxes: [{
        type: 'time',
        ticks: {
                        beginAtZero:true,
                        min: 0,
                        max:   "12/30/2016"  
                    }
      }]
    }};


  // store everything in config
  var config = {
    "type": "line",
    "data": {
      "datasets": datasets ,
     labels: ["10/21/2016", "12/30/2016","12/30/2017"]
    },
    "options": options
  };


  // display chart
  var chartArea = document.getElementById("chart-area").getContext("2d");
  var myLineChart = new Chart(chartArea, config);

  myLineChart.update();
  // var newItem = document.createElement("p");
  // newItem.innerHTML = "TESTING"
  // var list = document.getElementById("myList");
  // list.insertBefore(newItem, list.firstChild);
};

/*
  axisX:{
        title: "time",
        gridThickness: 2,
        interval:2, 
        intervalType: "hour",        
        valueFormatString: "hh TT K", 
        labelAngle: -20
      },

 */
    

