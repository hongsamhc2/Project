$(document).ready(function () {
    $('.gauge').each(function () {
        var $this = $(this);
        var per = $this.attr('per');
        $this.animate({
            width: per + "%"
        });
    });


    $(document).on("click", ".show", function () {
        $('#sidebar').css({
            'left': '0'
        });
        $('.move').css({
            'left': '30vw'
        });
        $('.menu').empty();
        $('.menu').append('<span class="hide">Close<span>');

    });

    $(document).on("click", ".hide", function () {

        $('#sidebar').css({
            'left': '-200px'
        });
        $('.move').css({
            'left': '18vw'
        });
        $('.menu').empty();
        $('.menu').append('<span class="show">Menu<span>');

    });

    $(window).resize(function () {
        var width = $(window).width();
        if (width >= 1024) {
            $('#sidebar').css({
                'left': '0'
            });
            $('.menu').css({
               'display':'none'
            });
        } else {
            $('#sidebar').css({
                'left': '-200px'
                
            });
            $('.menu').css({
               'display':'block' 
            });
        }
    });
});
