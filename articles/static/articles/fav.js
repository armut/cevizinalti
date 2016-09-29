function fav() {
    $.ajax({
        url: "fav/",
        type: "POST",
        success: function() {
            alert("success");
        },
        error: function() {
            alert("error");
        }
    });
}

$(document).ready(function() {
    $("#fav-link").click(function() {
        fav();       
    });
});
