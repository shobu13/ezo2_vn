$(document).ready(function(){
    $("#accueil").mouseover(function(){
        $("#accueil").attr("src", "/static/ezo/img/menu/meijiyuri_accueil_hover.png");
    });
    $("#accueil").mouseout(function(){
        $("#accueil").attr("src", "/static/ezo/img/menu/meijiyuri_accueil_off.png");
    });
});

$(document).ready(function(){
    $("#perso").mouseover(function(){
        $("#perso").attr("src", "/static/ezo/img/menu/meijiyuri_perso_hover.png");
    });
    $("#perso").mouseout(function(){
        $("#perso").attr("src", "/static/ezo/img/menu/meijiyuri_perso_off.png");
    });
});

$(document).ready(function(){
    $("#galerie").mouseover(function(){
        $("#galerie").attr("src", "/static/ezo/img/menu/meijiyuri_galerie_hover.png");
    });
    $("#galerie").mouseout(function(){
        $("#galerie").attr("src", "/static/ezo/img/menu/meijiyuri_galerie_off.png");
    });
});

$(document).ready(function(){
    $("#special").mouseover(function(){
        $("#special").attr("src", "/static/ezo/img/menu/meijiyuri_special_hover.png");
    });
    $("#special").mouseout(function(){
        $("#special").attr("src", "/static/ezo/img/menu/meijiyuri_special_off.png");
    });
});

$(document).ready(function(){
    $("#info").mouseover(function(){
        $("#info").attr("src", "/static/ezo/img/menu/meijiyuri_info_hover.png");
    });
    $("#info").mouseout(function(){
        $("#info").attr("src", "/static/ezo/img/menu/meijiyuri_info_off.png");
    });
});

$(window).resize(function(){
    var width = $('#his').width();
    $('#his').css('height', 2/3*width + 'px');

});

$(document).ready(function(){
    var width = $('#his').width();
    $('#his').css('height', 2/3*width + 'px');
});