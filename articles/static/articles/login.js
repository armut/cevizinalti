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
    
    // Hide the login form except login button.
    $("#uid").hide();
    $("#pass").hide();

    $(".login_btn").click(function(e) {
        // If text inputs aren't visible, then show them once,
        if( !($("#uid").is(":visible")) ) {
            $("#uid").fadeIn();
            $("#pass").show();
        }
        else { // If not, then ready to go.
            login();
        }
    });

    $(".logout_btn").click(function(e) {
        logout();
    });
});
