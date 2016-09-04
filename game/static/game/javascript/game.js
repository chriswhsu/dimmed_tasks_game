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
        var dl = 1.0 - (dim_level);
        $('#screen').css({opacity: dl, 'width': $(document).width(), 'height': $(document).height()});


    }

    function get_going(clicks) {

        window.location.href = '/game/get_going/' + $("#game_round_user_task_id").text() + '/' + dim_percentage;
    }


    $("#ex1").on("slide", function (slideEvt) {
        set_dim(slideEvt.value/100);
    });

    $('#get_going').click(get_going);


    var dim_percentage;
    var dim_pct = $('#ex1').slider({
        formatter: function (value) {
            dim_percentage = value;
            return 'Dim: ' + value + '%';
        }
    });


    function BuildSummaryChart() {

        var summarychart = new Highcharts.Chart({
            chart: {
                type: 'column',
                renderTo: 'summarychart',
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
        summarychart.showLoading();

        var data = {
            'game_round_id': $("#game_round_id").text()
        };


        $.ajax({
            type: 'POST',
            async: true,
            url: "/game/get_summary_points_ajax/",
            data: JSON.stringify(data),
            success: function (response) {
                while (summarychart.series.length) {
                    summarychart.series[0].remove(redraw = false);
                }
                for (var key in response) {
                    if (response.hasOwnProperty(key)) {
                        if (response[key].slice(0, 1) == 'true') {
                            this_color = 'blue'
                        }
                        else {
                            this_color = 'lightgrey'
                        }
                        summarychart.addSeries({
                            'color': this_color,
                            'name': key,
                            'data': response[key].slice(1, 2)
                        });
                    }
                }
                summarychart.hideLoading();


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

    if ($('#summarychart').length) {
        BuildSummaryChart();
    }


    set_dim($("#dim_level").text());

});

