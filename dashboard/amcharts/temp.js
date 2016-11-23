var dataset;
var glob = "SFSDF"
var firstDate = new Date();
firstDate.setHours( 0, 0, 0, 0 );
firstDate.setDate( firstDate.getDate() - 10 );

var periods = 
  [ 
    {
      "period": "hh",
      "count": 1,
      "label": "1 hour"
    },{
      "period": "DD",
      "count": 1,
      "label": "1 day"
    },{
      "period": "DD",
      "count": 10,
      "label": "10 days"
    }, {
      "period": "MM",
      "count": 1,
      "label": "1 month"
    }, {
      "period": "YYYY",
      "count": 1,
      "label": "1 year",
      "selected": true
    }, {
      "period": "YTD",
      "label": "YTD"
    }, {
      "period": "MAX",
      "label": "MAX"
    } 
  ]

//     

// TEMPORARY RANDOM DATA GENERATOR
function generateChartData( data, field ) {
  var ret = [];
  for (var i = 0; i < 10; i++) {
    
    var randVal = Math.floor(Math.random() * (100));
    ret.push({
      "value": randVal,
    });
  }

  function compare(a,b) {
    if (a.value < b.value)
      return -1;
    if (a.value > b.value)
      return 1;
    return 0;
  }

  ret.sort(compare);

  for (var i = 0; i < ret.length; i++) {
    var newDate = new Date(firstDate);
    newDate.setDate(newDate.getDate() + i );
    ret[i]["date"] = newDate;
  }

  return ret;
}



// CREATE CHART
var chart = AmCharts.makeChart( "chartdiv", {
  "type": "stock",
  
  "dataSets": [],
  
  "panels": [{
    "title": "App Monitor",
    "recalculateToPercents": "never",
    
    "stockGraphs": [{
      "valueField": "value",
      "comparable": true,
      "bullet": "round",
      "compareGraphBullet" : "round"
    }],

    "stockLegend": {}
  }],

  "chartCursorSettings": {
    "valueLineEnabled": true,
    "valueLineBalloonEnabled": true,
    "bulletsEnabled" : true
  },

  "dataSetSelector": {
    "position": "left"
  },

  "periodSelector": {
    "dateFormat" : "MM-DD-YYYY HH:NN:SS",
    "position": "left",
    "inputFieldsEnabled": true,
    "periods": periods
  },

  "balloon": {
    "adjustBorderColor": true,
    "color": "#000000",
    "cornerRadius": 5,
    "fillColor": "#FFFFFF"
  }


} );



jQuery(document).ready(function() {
    // REMOVE DATASET
    jQuery( ".btn-dataset-remove" ).on( "click", function() {
    if ( chart.dataSets.length > 1 ) {
      // REMOVE LATEST DATASET AND VALIDATE
      var dataset = chart.dataSets.pop();
      chart.validateNow();

    }
    } );


    // ADD DATASET
    jQuery( ".btn-dataset-add" ).on( "click", function() {
      glob = chart.panels[0].stockGraphs;


      // CREATE DATASET
      dataset = new AmCharts.DataSet();
      dataset.title = "Dataset " + ( chart.dataSets.length + 1 );
      dataset.dataProvider = generateChartData();
      dataset.categoryField = "date";

      // LOOP THROUGH PANELS
      // TO GENERATE DATA AND CREATE FIELDMAPPINGS FOR EACH GRAPH

      for ( i1 in chart.panels ) {
        // LOOP THROUGH PANEL GRAPHS
        for ( i2 in chart.panels[ i1 ].stockGraphs ) {
          var valueField = chart.panels[ i1 ].stockGraphs[ i2 ].valueField;
          
          chart.panels[ i1 ].bullet = "square";
          chart.panels[ i1 ].bulletSize = 12;

          
          // GENERATE NEW GRAPH DATA
          dataset.dataProvider = generateChartData( dataset.dataProvider, valueField );

          // ADD FIELDMAPPING
          dataset.fieldMappings.push( {
            "fromField": valueField,
            "toField": valueField
          } );
        }
      }

      // ADD NEW DATASET
      chart.dataSets.push( dataset );
      chart.validateNow();
    } );

} );