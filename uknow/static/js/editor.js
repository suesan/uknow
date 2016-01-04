$(function () {
    var textarea = $('#editor-body-textarea');
    var preview = $('.editor-body-preview');
    var updatePreview = function (raw) {
        $.ajax({
            url: '/api/v1/editor/preview/',
            type: 'POST',
            dataType:'text',
            data: {
                raw: raw
            },
            crossDomain: false
        }).done(function (data) {
            preview.html(data);
        }).fail(function(data) {
            console.log('error');
        });
    };

    updatePreview(textarea.val());

    textarea.on('keyup change', function() {
        var raw = textarea.val();
        updatePreview(raw);
    });

    textarea.on('scroll', function() {
        var scrollTop = textarea.scrollTop();
        var scrollHeight = textarea[0].scrollHeight;
        var scrollPointRatio = scrollTop / scrollHeight;
        // Do Scroll Preview!
        preview.animate({ scrollTop: preview[0].scrollHeight * scrollPointRatio }, 0);
    });
});
