$(document).ready(function () {


    function get_question_and_choices_ajax() {
        var data = {
            'grut_id': $('#game_round_user_task_id').text(),
            'question_id': $('#question_id').text(),
            'answer_code': $("input[name=choices]:checked").val()

        };

        $.ajax({
            type: 'POST',
            async: true,
            url: "/game/get_question_and_choices_ajax/",
            data: JSON.stringify(data),
            success: function (response) {
                if (response.over) {
                    window.location.href = '/game/continue_game/' + $("#game_round_user_task_id").text();
                }
                else {

                    $('#clear_count').html(response.score + " Points")
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert("#next_iteration_ajax: jqXHR= " + jqXHR.status + " " + jqXHR.readyState + ", textStatus= " + textStatus + ", errorThrown= " + errorThrown)
            }
        });
    }

    $("#make_choice").click(function () {
        get_question_and_choices_ajax()
    });


});

