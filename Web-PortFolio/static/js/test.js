$(document).ready(function () {
    $('button').click(function () {
        var code = $('option:selected ').val();
        alert(code);
        get_data();

    });

});

function get_data() {
    var code = $('option:selected').val();

    $.ajax({
        type: 'POST',
        url: './stock_data',
        data: {
            code: code
        },
        dataType: 'JSON',
        success: function (data) {
            alert(data)
        },
        error: function (error) {
            console.log(error)
        }



    });
}
