$(document).ready(function(){
    $("#accueil").mouseover(function(){
        $("#accueil").attr("src", "/static/ezo/img/menu/meijiyuri_accueil_hover.png");
    });
    $("#accueil").mouseout(function(){
        $("#accueil").attr("src", "/static/ezo/img/menu/meijiyuri_accueil_off.png");
    });
});

$(document).ready(function(){
    $("#histoire").mouseover(function(){
        $("#histoire").attr("src", "/static/ezo/img/menu/meijiyuri_histoire_hover.png");
    });
    $("#histoire").mouseout(function(){
        $("#histoire").attr("src", "/static/ezo/img/menu/meijiyuri_histoire_off.png");
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


function clear()
{
    $("#ezoim").attr("src", "/static/ezo/img/perso/ezo_off.png");
    $("#ranim").attr("src", "/static/ezo/img/perso/ran_off.png");
    $("#seiim").attr("src", "/static/ezo/img/perso/sei_off.png");
    $("#tsuguim").attr("src", "/static/ezo/img/perso/tsugu_off.png");
    $("#akieim").attr("src", "/static/ezo/img/perso/akie_off.png");
    $("#yoshiim").attr("src", "/static/ezo/img/perso/yoshi_off.png");
    $("#claim").attr("src", "/static/ezo/img/perso/cla_off.png");
};

$("#ezocl").click(function(){
    clear();
    $("#ezoim").attr("src", "/static/ezo/img/perso/ezo_on.png");
    $("#profperso").attr("src","/static/ezo/img/perso/ezo_profile.png")
});

$("#rancl").click(function(){
    clear();
    $("#ranim").attr("src", "/static/ezo/img/perso/ran_on.png");
    $("#profperso").attr("src","/static/ezo/img/perso/ran_profile.png")
});

$("#seicl").click(function(){
    clear();
    $("#seiim").attr("src", "/static/ezo/img/perso/sei_on.png");
    $("#profperso").attr("src","/static/ezo/img/perso/sei_profile.png")
});

$("#tsugucl").click(function(){
    clear();
    $("#tsuguim").attr("src", "/static/ezo/img/perso/tsugu_on.png");
    $("#profperso").attr("src","/static/ezo/img/perso/tsugu_profile.png")
});

$("#akiecl").click(function(){
    clear();
    $("#akieim").attr("src", "/static/ezo/img/perso/akie_on.png");
    $("#profperso").attr("src","/static/ezo/img/perso/akie_profile.png")
});

$("#yoshicl").click(function(){
    clear();
    $("#yoshiim").attr("src", "/static/ezo/img/perso/yoshi_on.png");
    $("#profperso").attr("src","/static/ezo/img/perso/yoshi_profile.png")
});

$("#clacl").click(function(){
    clear();
    $("#claim").attr("src", "/static/ezo/img/perso/cla_on.png");
    $("#profperso").attr("src","/static/ezo/img/perso/cla_profile.png")
});