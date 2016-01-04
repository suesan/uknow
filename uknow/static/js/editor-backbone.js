$(function() {
    var Editor = Backbone.Model.extend({
        defaults: {
            raw: '',
            html: ''
        }
    });

    var EditorView = Backbone.View.extend({
        el: '.editor-body',
        events: {
            'keyup #editor-body-textarea': 'updateEditor',
            'change #editor-body-textarea': 'updateEditor'
            // スクロールイベントは'initialize'メソッドの中でバインドされている
        },
        initialize: function() {
            this.listenTo(this.model, 'change:html', this.renderPreview);
            $('#editor-body-textarea').on('scroll', this.scroll);
            this.updateEditor();
        },
        renderPreview: function() {
            $('.editor-body-preview').html(this.model.get('html'));
        },

        updateEditor: function() {
            var raw =  $('#editor-body-textarea').val();
            var self = this;
            this.model.set('raw', raw);
            // HTMLに変換
            $.ajax({
                url: '/api/v1/editor/preview/',
                type: 'POST',
                dataType:'text',
                data: {
                    raw: raw
                },
                crossDomain: true
            }).done(function (data) {
                self.model.set('html', data);
            }).fail(function(data) {
                console.log('error');
            });
        },

        /*
         * プレビューのオートスクロール
         */
        scroll: function() {
            console.log('onscroll');
            var textarea = $('#editor-body-textarea');
            var preview = $('.editor-body-preview');
            var scrollTop = textarea.scrollTop();
            var scrollHeight = textarea[0].scrollHeight;
            var scrollPointRatio = scrollTop / scrollHeight;
            // Do Scroll Preview!
            preview.animate({ scrollTop: preview[0].scrollHeight * scrollPointRatio }, 0);
        }

    });

    var editor = new Editor();
    var editorView = new EditorView({model: editor});
});
