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


    function post_completion(resource_id, resource_value) {

        var data = {
            'resource_id': resource_id,
            'resource_value': resource_value
        };

        $.ajax({
            type: 'POST',
            async: true,
            url: "/set_get_resource_setting_ajax/",
            data: JSON.stringify(data),
            success: function (response) {

                if (res_type == 'LIGHT') {
                    bright(response.resource_level);
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert("#SetGetResourceSetting: jqXHR= " + jqXHR.status + " " + jqXHR.readyState + ", textStatus= " + textStatus + ", errorThrown= " + errorThrown)
            }
        });
    }

    


});

