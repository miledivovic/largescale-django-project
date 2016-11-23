
colors = [
  'rgb(255, 99, 132)',
  'rgb(75, 192, 192)',
  'rgb(54, 162, 235)',
  'rgb(153, 102, 255)',
  'rgb(231,233,237)',
  'rgb(255, 159, 64)',
  'rgb(255, 205, 86)',
]


function filterByTag(md , t){
  var tmp = md.filter(function (el) {
      return el.tag === t;
  });
  console.log(t)
  return tmp;
}


function getTags(array){
  var unique = {};
  var distinct = [];
  for( var i in array ){
    var un = unique[array[i].tag];
    if( typeof(un) == "undefined"){
      distinct.push(array[i].tag);
     }
    unique[array[i].tag] = 0;
  }
  return distinct;
}


var titles = ["title_1" , "title_2"]




function newData(label, data, bgcolor){
  d = {
    fill: false,
    lineTension: 0.1,
    backgroundColor: bgcolor,
    borderColor: bgcolor,
    borderDashOffset: 0.0,
    pointBorderColor: "red",
    pointBackgroundColor: "red",
    pointBorderWidth: 1,
    pointHoverRadius: 5,
    pointRadius: 5,
    pointHitRadius: 10,
  }
  d.label = label;
  d.data = data;
  return d;
}

var ops = {
        responsive: true,
          scales: {
              xAxes: [{
                  type: 'linear',
                  position: 'bottom'
              }]
          }};





var mydata
window.onload = function() {
   mydata = JSON.parse(log);

   var tags = getTags(mydata)

  var dataByTag = []

  for (var i = 0; i < tags.length; i++) {
   dataByTag.push(filterByTag(mydata, tags[i]));
  }



  var datasets = [];

  for (var i = 0; i < dataByTag.length; i++) {
    var tmp = newData(dataByTag[i][0].tag, dataByTag[i], colors[i])
    datasets.push(tmp)
  }

  var data = {
    datasets: datasets,
  }

  var config = {
    type: 'line',
    "data": {"datasets": datasets},
    options: ops
  };




  
  var ctx = document.getElementById("chart-area").getContext("2d");
  window.myChart = new Chart(ctx, config);


  var newItem = document.createElement("p");
  newItem.innerHTML = "TESTING"

  var list = document.getElementById("myList");
  list.insertBefore(newItem, list.firstChild);

};





