$(document).ready(function () {
    // local variables


    function BuildPointChart() {


        var compchart = new Highcharts.Chart({
            chart: {
                type: 'column',
                renderTo: 'compchart',
                width: '500'

            },
            title: {
                text: ''
            },
            yAxis: {
                title: {text: 'Points'}
            },
            xAxis: {
                categories: ['Points'],
                labels: {
                    style: {
                        fontSize: '20px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }

            },
            legend: {
                enabled: false
            }
        });

        var pctchart = new Highcharts.Chart({
            chart: {
                type: 'column',
                renderTo: 'pctchart',
                width: '500'

            },
            title: {
                text: ''
            },
            yAxis: {
                title: {text: 'Dimmed Pct'}
            },
            xAxis: {
                categories: ['Dimmed Pct'],
                labels: {
                    style: {
                        fontSize: '20px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }

            },
            legend: {
                enabled: false
            }
        });


        var this_color;
        compchart.showLoading();

        var data = {
            'game_round_task_id': $("#game_round_task_id").text()
        };


        $.ajax({
            type: 'POST',
            async: true,
            url: "/game/get_comparison_points_ajax/",
            data: JSON.stringify(data),
            success: function (response) {
                while (compchart.series.length) {
                    compchart.series[0].remove(redraw = false);
                }
                for (var key in response) {
                    if (response.hasOwnProperty(key)) {
                        if (response[key].slice(0, 1) == 'true') {
                            this_color = 'blue'
                        }
                        else {
                            this_color = 'lightgrey'
                        }
                        compchart.addSeries({
                            'color': this_color,
                            'name': key,
                            'data': response[key].slice(1, 2)
                        });
                    }
                }
                compchart.hideLoading();


                while (pctchart.series.length) {
                    pctchart.series[0].remove(redraw = false);
                }
                for (var key in response) {
                    if (response.hasOwnProperty(key)) {
                        if (response[key].slice(0, 1) == 'true') {
                            this_color = 'blue'
                        }
                        else {
                            this_color = 'lightgrey'
                        }
                        pctchart.addSeries({
                            'color': this_color,
                            'name': key,
                            'data': response[key].slice(2, 3)
                        });
                    }
                }
                pctchart.hideLoading();

            }
        });
    }


    if ($('#compchart').length) {
        BuildPointChart();
    }

    function set_dim(dim_level) {
        var dl = (dim_level);
        $('#screen').css({opacity: dl, 'width': $(document).width(), 'height': $(document).height()});


    }

    function get_going(clicks) {

        window.location.href = '/game/get_going/' + $("#game_round_user_task_id").text() + '/' + dim_percentage;
    }


    $("#ex1").on("slide", function (slideEvt) {
        set_dim(slideEvt.value / 100);
    });

    $('#get_going').click(get_going);


    var dim_percentage;
    var dim_pct = $('#ex1').slider({
        formatter: function (value) {
            dim_percentage = value;
            return 'Brightness: ' + value + '%';
        }
    });


    $('#button').click(function () {
        BuildSummaryChart();
    });

    function BuildSummaryChart() {


        var piechart = new Highcharts.Chart({
            chart: {
                renderTo: 'piechart',
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie',
                width: 500
            },
            title: {
                text: 'Points for Each User'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                        style: {
                            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                        }
                    }
                }
            },
            series: [{
                name: 'Users',
                colorByPoint: true,
                data: [{
                    name: 'Microsoft IE',
                    y: 56.33,
                    sliced: true
                }, {
                    name: 'Chrome',
                    y: 24.03
                }, {
                    name: 'Firefox',
                    y: 10.38
                }, {
                    name: 'Safari',
                    y: 4.77
                }, {
                    name: 'Opera',
                    y: 0.91
                }, {
                    name: 'Unknown',
                    y: 0.2
                }]
            }]
        });


        var sum_pct_chart = new Highcharts.Chart({
            chart: {
                type: 'column',
                renderTo: 'sum_pct_chart',
                width: '500'

            },
            title: {
                text: ''
            },
            yAxis: {
                title: {text: 'Dimmed Pct'}
            },
            xAxis: {
                categories: ['Dimmed Pct'],
                labels: {
                    style: {
                        fontSize: '20px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }

            },
            legend: {
                enabled: false
            }
        });


        var this_color;
        piechart.showLoading();

        var data = {
            'game_round_id': $("#game_round_id").text()
        };


        $.ajax({
            type: 'POST',
            async: true,
            url: "/game/get_summary_points_ajax/",
            data: JSON.stringify(data),
            success: function (response) {
                while (piechart.series.length) {
                    piechart.series[0].remove(redraw = false);
                }

                var my_arrary = []
                for (var key in response) {
                    my_arrary.push({name: key, y: response[key].slice(1, 2)[0]});
                }
                piechart.addSeries({
                    'color': this_color,
                    'name': key,
                    'data': my_arrary
                });

                piechart.hideLoading();


                while (sum_pct_chart.series.length) {
                    sum_pct_chart.series[0].remove(redraw = false);
                }
                for (var key in response) {
                    if (response.hasOwnProperty(key)) {
                        if (response[key].slice(0, 1) == 'true') {
                            this_color = 'blue'
                        }
                        else {
                            this_color = 'lightgrey'
                        }
                        sum_pct_chart.addSeries({
                            'color': this_color,
                            'name': key,
                            'data': response[key].slice(2, 3)
                        });
                    }
                }
                sum_pct_chart.hideLoading();


            }
        });
    }

    if ($('#piechart').length) {
        BuildSummaryChart();
    }


    set_dim($("#dim_level").text());


});

