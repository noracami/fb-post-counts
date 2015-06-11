// pages/static/pages/js/page_list.js

(function ($) {
$('.btn-delete').click(function () {
  var button = this;
  $.ajax({
    'url': $(button).data('href'),
    'type': 'DELETE'
  }).done(function () {
    $(button).parent().parent().remove();
  }).fail(function (e) {
    console.log(e);
  });
});
})(jQuery);

(function ($) {
$('.btn-refresh').click(function () {
  var button = this;
  $.ajax({
    'url': $(button).data('href'),
    'type': 'POST'
  }).done(function () {
    window.location.reload(true);
    //$(button).remove();
  }).fail(function (e) {
    console.log(e);
  });
});
})(jQuery);
