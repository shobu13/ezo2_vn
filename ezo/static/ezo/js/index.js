$(document).ready(function(){
    $("#histoire").mouseover(function(){
        console.log("test");
        $("#histoire").attr("src", "/static/ezo/img/menu/meijiyuri_histoire_hover.png");
    });
    $("#histoire").mouseout(function(){
        $("#histoire").attr("src", "/static/ezo/img/menu/meijiyuri_histoire_off.png");
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
        var width = $('#logo').width();
        $('#logo').css('height', width /2 + 'px');
 
    });
   
    $(document).ready(function(){
        var width = $('#logo').width();
        $('#logo').css('height', width /2 + 'px');
    });