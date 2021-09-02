

function getdata(){
    $.post( "http://127.0.0.1:5000/predict", function( data ) {
    var response = JSON.parse(data);
    console.log(response.data);
    if ($('#amlinechart4').length) {
        var chart = AmCharts.makeChart("amlinechart4", {
            "type": "serial",
            "theme": "light",
            "legend": {
                "useGraphSettings": true
            },
            "dataProvider": response.data,
            "categoryField": "index",
            "startDuration": 0.5,
            "graphs": [{
                "balloonText": "[[values]]",
                "bullet": "round",
                "title": "Prediction",
                "valueField": "values",
                "fillAlphas": 0,
                "lineColor": "#31aeef",
                "lineThickness": 2,
                "negativeLineColor": "#31aeef",
                "position": "top",
            }],
            "chartCursor": {
                "cursorAlpha": 0,
                "zoomable": false
            },
            "indexField": "values",
            "indexAxis": {
                "gridPosition": "index",
                "axisAlpha": 0,
                "fillAlpha": 0.05,
                "fillColor": "#000000",
                "gridAlpha": 0,
                "position": "top"
            },
            "export": {
                "enabled": false
            }
        });
    }
    
    return response;
  });
}

getdata()