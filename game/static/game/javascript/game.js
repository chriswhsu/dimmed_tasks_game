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
            },
            plotOptions: {
                column: {
                    minPointLength: 3
                }
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
                title: {text: 'Brightness'}
            },
            xAxis: {
                categories: ['Brightness'],
                labels: {
                    style: {
                        fontSize: '20px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }

            },
            legend: {
                enabled: false
            },
            plotOptions: {
                column: {
                    minPointLength: 3
                }
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

    function set_brightness(brightness_level) {
        var dl = (brightness_level);
        $('#screen').css({opacity: dl, 'width': $(document).width(), 'height': $(document).height()});


    }

    function get_going(clicks) {

        window.location.href = '/game/get_going/' + $("#game_round_user_task_id").text() + '/' + bright_percentage;
    }


    $("#ex1").on("slide", function (slideEvt) {
        set_brightness(slideEvt.value / 100);
    });

    $('#get_going').click(get_going);


    var bright_percentage;
    var bright_pct = $('#ex1').slider({
        formatter: function (value) {
            bright_percentage = value;
            return 'Brightness: ' + value + '%';
        }
    });


    function animate_slices(winners, winner_list) {

        var segments = piechart.series[0].data.length;
        var tps = 100;

        function slice(segment, loop) {
            // on the first pass pull the pie slice out.
            setTimeout(function () {
                piechart.series[0].data[segment].slice()
            }, tps * (segment + 1) + (loop * segments * tps));

            // Then push it back in delayed somewhat by the total percentage of points they have.
            if (jQuery.inArray(piechart.series[0].data[segment].name, winners) >= 0 && loop == 4) {
                setTimeout(function () {
                    set_winner(winner_list);
                }, tps * (segment + 1) + (loop * segments * tps) + 500);
            }
            else {
                setTimeout(function () {
                    piechart.series[0].data[segment].slice()
                }, tps * (segment + 1) + (loop * segments * tps) + 500);
            }
        }

        for (var x = 0; x < 5; x++) {
            for (var qq = 0; qq < segments; qq++) {

                slice(qq, x)

            }
        }
    }

    function set_winner(winning_name) {

        $('#winner').html(winning_name)

    }


    $('#button').click(function () {
        BuildSummaryChart(animate_slices);
    });

    if ($('#piechart').length) {
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
                text: '% of Total Points by User'
            },
            tooltip: {
                pointFormat: '{point.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: false,
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
                data: []
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
                title: {text: 'Brightness'}
            },
            xAxis: {
                categories: ['Brightness'],
                labels: {
                    style: {
                        fontSize: '20px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }

            },
            legend: {
                enabled: false
            },
            plotOptions: {
                column: {
                    minPointLength: 3
                }
            }
        });
    }


    function BuildSummaryChart(callback) {

        var this_color;
        piechart.showLoading();

        $.ajax({
            type: 'POST',
            async: true,
            url: "/game/get_summary_points_ajax/",
            data: JSON.stringify({
                'game_round_id': $("#game_round_id").text()
            }),
            success: function (response) {
                while (piechart.series.length) {
                    piechart.series[0].remove(redraw = false);
                }
                var winners = []
                var my_arrary = [];
                for (var key in response.points) {
                    my_arrary.push({name: key, y: response.points[key].slice(1, 2)[0]})
                    if (response.points[key].slice(3, 4)[0] == true) {
                        winners.push(key);
                    }
                }
                piechart.addSeries({
                    'name': key,
                    'data': my_arrary
                });

                setTimeout(function () {
                    callback(winners, response.winners_text)
                }, 1000);

                piechart.hideLoading();


                while (sum_pct_chart.series.length) {
                    sum_pct_chart.series[0].remove(redraw = false);
                }
                for (var key in response.points) {
                    if (response.points.hasOwnProperty(key)) {
                        if (response.points[key].slice(0, 1) == 'true') {
                            this_color = 'blue'
                        }
                        else {
                            this_color = 'lightgrey'
                        }
                        sum_pct_chart.addSeries({
                            'color': this_color,
                            'name': key,
                            'data': response.points[key].slice(2, 3)
                        });
                    }
                }
                sum_pct_chart.hideLoading();
            }
        });
    }

    if ($('#piechart').length) {
        BuildSummaryChart(animate_slices);
    }

    set_brightness($("#brightness_level").text());


});

