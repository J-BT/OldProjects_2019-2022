

    /* 1er Graph**************************************************** */

    var chartdata = []
    var chartdata2 = []
    var chartdata3 = []
    var chartdata4 = []
    var chartdata5 = []
    var chartdata6 = []
    var chartdata7 = []
    var chartdata8 = []
    var chartdata9 = []
    var chartdata10 = []
    var chartdata11 = []
    var chartdata12 = []
    var chartdata13 = []
    var volume = []

    function processData(data)
    {   
        
        /*On recup les données importées en python*/
        var data1 = data.res;
        var data2 = data.res2;
        var data3 = data.res3;
        var data4 = data.res4;
        var data5 = data.res5;
        var data6 = data.res6;
        var data7 = data.res7;
        var data8 = data.res8;
        var data9 = data.res9;
        var data10 = data.res10;
        var data11 = data.res11;
        var data12 = data.res12;
        var data13 = data.res13;

        //alert(data1[0][0] + '---->' + data1[0][1])
        
        for (var i=0; i < data1.length; i++) 
        {   
            chartdata.push([
                data1[i][0], // Date
                data1[i][1], // Prix
            ]);
        }
        
        for (var i=0; i < data2.length; i++)
        {   
            chartdata2.push([
                data2[i][0], // Date
                data2[i][1], // Prix
            ]);
        }
        for (var i=0; i < data3.length; i++)
        {   
            chartdata3.push([
                data3[i][0], // Date
                data3[i][1], // Prix
            ]);
        }
        for (var i=0; i < data4.length; i++)
        {   
            chartdata4.push([
                data4[i][0], // Date
                data4[i][1], // Prix
            ]);
        }
        for (var i=0; i < data5.length; i++)
        {   
            chartdata5.push([
                data5[i][0], // Date
                data5[i][1], // Prix
            ]);
        }
        for (var i=0; i < data6.length; i++)
        {   
            chartdata6.push([
                data6[i][0], // Date
                data6[i][1], // Prix
            ]);
        }
        for (var i=0; i < data7.length; i++)
        {   
            chartdata7.push([
                data7[i][0], // Date
                data7[i][1], // Prix
            ]);
        }
        for (var i=0; i < data8.length; i++)
        {   
            chartdata8.push([
                data8[i][0], // Date
                data8[i][1], // Prix
            ]);
        }
        for (var i=0; i < data9.length; i++)
        {   
            chartdata9.push([
                data9[i][0], // Date
                data9[i][1], // Prix
            ]);
        }
        for (var i=0; i < data10.length; i++)
        {   
            chartdata10.push([
                data10[i][0], // Date
                data10[i][1], // Prix
            ]);
        }
        for (var i=0; i < data11.length; i++)
        {   
            chartdata11.push([
                data11[i][0], // Date
                data11[i][1], // Prix
            ]);
        }
        for (var i=0; i < data12.length; i++)
        {   
            chartdata12.push([
                data12[i][0], // Date
                data12[i][1], // Prix
            ]);
        }
        for (var i=0; i < data13.length; i++)
        {   
            chartdata13.push([
                data13[i][0], // Date
                data13[i][1], // Prix
            ]);
        }
    }


    function plotCharts(){
        Highcharts.stockChart('container', {
            chart: {
                height: (9 / 16 * 100) + '%'// 16:9 ratio pour le graph
            },
            navigation: {
                bindings: {
                    rect: {
                        annotationsOptions: {
                            shapeOptions: {
                                fill: 'rgba(255, 0, 0, 0.8)'
                            }
                        }
                    }
                },
                annotationsOptions: {
                    typeOptions: {
                        line: {
                            stroke: 'rgba(255, 0, 0, 1)',
                            strokeWidth: 10
                        }
                    }
                }
            },
            yAxis: [{
                labels: {
                    align: 'left'
                },
                height: '80%'
            }, {
                labels: {
                    align: 'left'
                },
                top: '80%',
                height: '20%',
                offset: 0
            }],
            series: [{
                type: 'line',
                id: 'courbe1',
                name: 'Service1',
                data: chartdata
            },
            {
                type: 'line',
                id: 'courbe2',
                name: 'Service2',
                data: chartdata2
            },
            {
                type: 'line',
                id: 'courbe3',
                name: 'Service3',
                data: chartdata3
            },
            {
                type: 'line',
                id: 'courbe4',
                name: 'Service4',
                data: chartdata4
            },
            {
                type: 'line',
                id: 'courbe5',
                name: 'Service5',
                data: chartdata5
            },
            {
                type: 'line',
                id: 'courbe6',
                name: 'Service6',
                data: chartdata6
            },
            {
                type: 'line',
                id: 'courbe7',
                name: 'Service7',
                data: chartdata7
            },
            {
                type: 'line',
                id: 'courbe8',
                name: 'Service8',
                data: chartdata8
            },
            {
                type: 'line',
                id: 'courbe9',
                name: 'Service9',
                data: chartdata9
            },
            {
                type: 'line',
                id: 'courbe10',
                name: 'Service10',
                data: chartdata10
            },
            {
                type: 'line',
                id: 'courbe11',
                name: 'Service11',
                data: chartdata11
            },
            {
                type: 'line',
                id: 'courbe12',
                name: 'Service12',
                data: chartdata12
            },
            {
                type: 'line',
                id: 'courbe13',
                name: 'Service13',
                data: chartdata13
            }]
        });


    }

    $( document ).ready(function()
    {
        $.getJSON('/Highcharts', function(data){
            processData(data);
            plotCharts();
        });
    });


    