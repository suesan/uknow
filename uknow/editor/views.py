from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from markdown import markdown as md
from lxml.html.clean import Cleaner

from django.contrib.auth.decorators import login_required

@ensure_csrf_cookie
@login_required
def editor_view(request):
    return render(request, 'editor/editor.html', {'example': ''})

@ensure_csrf_cookie
def editor_backbone_view(request):
    return render(request, 'editor/editor_backborn.html', {'example': ''})

def markdown(raw):
    html = md(raw, extensions=['gfm'])
    if not html.strip():
        return html
    kill_tags = ['body', 'head', 'style']
    cleaner   = Cleaner(kill_tags = kill_tags)
    html      = cleaner.clean_html(html)
    return html


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def api_preview(request):
    if not request.is_ajax:
        raise Http404
    if request.method != 'POST':
        raise Http404

    if not request.POST.get('raw', False):
        raw_content = ''
    else:
        raw_content = request.POST['raw']

    content = markdown(raw_content)

    return HttpResponse(content)
