$(document).ready(function () {
    // local variables


    $(function () {
        var pop = function () {
            $('#screen').css({opacity: 0.50, 'width': $(document).width(), 'height': $(document).height()});
        };
        $('#button').click(pop);
    });

});

