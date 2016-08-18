$(document).ready(function () {
    // local variables

    function BuildPointChart() {


        var compchart = new Highcharts.Chart({
            chart: {
                type: 'column',
                renderTo: 'compchart',
                width: '900'

            },
            title: {
                text: ''
            },
            yAxis: {
                title: {text: 'Points'}
            },
            xAxis: {
                opposite: true,
                // categories: ['Bonus', 'Lights', 'Total'],
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
            'game_round_user_id': $("#game_round_user_id").text()
        };


        $.ajax({
            type: 'POST',
            async: true,
            url: "/game/get_comparison_points/",
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
                            'data': response[key].slice(1, 5)
                        });
                    }
                }
                compchart.hideLoading();

            }
        });
    }


    if ($('#compchart').length) {
        BuildPointChart();
    }

});

