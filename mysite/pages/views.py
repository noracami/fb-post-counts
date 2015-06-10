from django.forms.models import modelform_factory
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils import timezone
import datetime
import json
import time
import urllib.request
from .models import PageItem



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
            print(request_link)
            #time.sleep(5)
            result = ''
            #result = json.loads(urllib.request.urlopen(request_link).read().decode('utf-8'))
            text[len(text):] = [{
                'name': page_item.name,
                'is_recently_count': page_item.last_access_time > timezone.now() - datetime.timedelta(days=1),
                #'notes': result['likes'],
                'request_link': request_link,
            }]
    return render(request, 'page_items/page_list.html',
        {'page_items': page_items, 'text': text})

def page_item_detail(request, pk):
    try:
        page_item = PageItem.objects.get(pk=pk)
    except PageItem.DoesNotExist:
        raise Http404
    return render(request, 'page_items/page_item_detail.html', {'page_item': page_item})

def page_item_create(request):
    PageItemForm = modelform_factory(PageItem, fields=('user', 'name', 'fb_id', 'last_access_time', 'last_like_count', 'picture_url', 'notes',))
    if request.method == 'POST':
        form = PageItemForm(request.POST)
        if form.is_valid():
            page_item = form.save()
            return redirect(page_item.get_absolute_url())
    else:
        form = PageItemForm()
    return render(request, 'page_items/page_item_create.html', {'form': form})

def page_item_update(request, pk):
    try:
        page_item = PageItem.objects.get(pk=pk)
    except PageItem.DoesNotExist:
        raise Http404
    PageItemForm = modelform_factory(PageItem, fields=('user', 'name', 'fb_id', 'last_access_time', 'last_like_count', 'picture_url', 'notes',))
    if request.method == 'POST':
        form = PageItemForm(request.POST, instance=PageItem)
        if form.is_valid():
            page_item = form.save()
            return redirect(page_item.get_absolute_url())
    else:
        form = PageItemForm(instance=page_item)
    return render(request, 'page_items/page_item_update.html', {
        'form': form, 'page_item': page_item,
    })
