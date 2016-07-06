$(document).ready(function () {
    // local variables

    var dl = 1.0 - $("#dim_level").text();
    $('#screen').css({opacity: dl, 'width': $(document).width(), 'height': $(document).height()});

    $(function () {
        var pop = function () {
            var dimmlevel = 1 - $("input[name=optradio]:checked").val();
            $('#screen').css({opacity: dimmlevel, 'width': $(document).width(), 'height': $(document).height()});
        };

        $('#dim_button').click(pop);
    });


});

