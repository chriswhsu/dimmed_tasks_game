$(document).ready(function () {
    // local variables


    $(function () {
        var pop = function () {
            var dimmlevel = 1 - $("input[name=optradio]:checked").val();
            $('#screen').css({opacity: dimmlevel, 'width': $(document).width(), 'height': $(document).height()});
        };
        $('#button').click(pop);
    });

});

