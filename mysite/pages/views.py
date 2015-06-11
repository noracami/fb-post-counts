from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_http_methods
import datetime
import json
import time
import urllib.request
from .models import PageItem
from .forms import PageItemForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def page_list(request):
    page_items = PageItem.objects.all().order_by('id')
    text = []
    if False:
        request_link = 'https://graph.facebook.com/818773044827025'
        result = json.loads(urllib.request.urlopen(request_link).read().decode('utf-8'))
        text[len(text):] = [{'data': result}]
        request_link = 'https://graph.facebook.com/563212453789705'
        result = ''
        result = json.loads(urllib.request.urlopen(request_link).read().decode('utf-8'))
        text[len(text):] = [{'data': result}]
    if True:
        for page_item in page_items:
            request_link = ''
            request_link = '%s%s' % (
                'https://graph.facebook.com/',
                page_item.fb_id,
            )
            #print(request_link)
            #time.sleep(5)
            result = ''
            #result = json.loads(urllib.request.urlopen(request_link).read().decode('utf-8'))
            text[len(text):] = [{
                'name': page_item.name,
                'is_recently_count': page_item.last_access_time > timezone.now() - datetime.timedelta(seconds=600),
                #'notes': result['likes'],
                'request_link': request_link,
                'page_item': page_item,
            }]
    return render(request, 'page_items/page_list.html',
        {'page_items': page_items, 'text': text})

def page_item_detail(request, pk):
    try:
        page_item = PageItem.objects.get(pk=pk)
    except PageItem.DoesNotExist:
        raise Http404
    return render(request, 'page_items/page_item_detail.html', {'page_item': page_item})

@login_required
def page_item_create(request):
    if request.method == 'POST':
        form = PageItemForm(request.POST, submit_title='加入')
        if form.is_valid():
            page_item = form.save(commit=False)
            if request.user.is_authenticated():
                page_item.creator = request.user
            page_item.save()
            return redirect(page_item.get_absolute_url())
    else:
        form = PageItemForm(submit_title='加入')
    return render(request, 'page_items/page_item_create.html', {'form': form})

def page_item_update(request, pk):
    try:
        page_item = PageItem.objects.get(pk=pk)
    except PageItem.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = PageItemForm(request.POST, instance=page_item, submit_title='更新')
        if form.is_valid():
            page_item = form.save()
            return redirect(page_item.get_absolute_url())
    else:
        form = PageItemForm(instance=page_item, submit_title='更新')
    return render(request, 'page_items/page_item_update.html', {
        'form': form, 'page_item': page_item,
    })

@login_required
@require_http_methods(['POST', 'DELETE'])
def page_item_delete(request, pk):
    try:
        page_item = PageItem.objects.get(pk=pk)
    except PageItem.DoesNotExist:
        raise Http404
    if page_item.can_user_delete(request.user):
        page_item.delete()
        if request.is_ajax():
            return HttpResponse()
        return redirect('page_list')
    return HttpResponseForbidden()

def page_item_refresh(request, pk):
    try:
        page_item = PageItem.objects.get(pk=pk)
    except PageItem.DoesNotExist:
        raise Http404
    #page_item.refresh()
    request_link = 'https://graph.facebook.com/%d?fields=likes' % page_item.fb_id
    result = json.loads(urllib.request.urlopen(request_link).read().decode('utf-8'))
    page_item.last_like_count = result['likes']
    page_item.save()
    if request.is_ajax():
        return HttpResponse()
    return redirect('page_list')
