let url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$('document').ready(() => {
    $.get(url, (data) => {
        $('DIV#hello').text(data.hello);
    });
});
