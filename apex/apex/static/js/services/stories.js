$(function () {
  var pathname = window.location.pathname;
  $('.menu-stories li a[href="'+ pathname +'"]').addClass('active');
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Setup AJAX
$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

function to_bookmarks()
{
    var current = $(this);
    var type = current.data('type');
    var pk = current.data('id');
    var action = current.data('action');

    $.ajax({
        url : "/" + pk + "/" + action + "/",
        type : 'POST',
        data : { 'obj' : pk },

        success : function (json) {

        }
    });

    return false;
}
$(".btn").click(function() {
  $(this).find('span').toggleClass("glyphicon-star glyphicon-star-empty");
});

$(function() {
    $('[data-action="bookmark"]').click(to_bookmarks);
});