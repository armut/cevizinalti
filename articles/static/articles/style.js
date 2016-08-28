function adjustStyle(width) {
    width = parseInt(width);
    if(width < 701) {
        $("#size-stylesheet").attr("href", "/static/articles/small.css");
    }
    else if(width < 900) {
        $("#size-stylesheet").attr("href", "/static/articles/medium.css");
    }
    else {
        $("#size-stylesheet").attr("href", "/static/articles/main.css");
    }
}

$(function() {
    adjustStyle($(this).width());
    $(window).resize(function() {
        adjustStyle($(this).width());
    });
});
