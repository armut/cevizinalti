function login() {
    $.ajax({
        url: "/login",
        type: "POST",
        data: $("#login_form").serialize(),
        success: function() {
            location.reload(true);
        },
        error: function(e) {
            alert("Olamaz beklenmedik bir hata vuku buldu.");
        }
    });
}

function logout() {
    $.ajax({
        url: "/logout",
        type: "POST",
        success: function() {
            location.reload(true);
        },
        error: function() {
            alert("O hayır. Bu da ne?\n Nereden çıktı?\n Daha önce hiç görmemiştim.\n Kafamda binlerce soru.");
        }
    });
}

$(document).ready(function() {
    $(".login_btn").click(function(e) {
        login();
    });

    $(".logout_btn").click(function(e) {
        logout();
    });
});
