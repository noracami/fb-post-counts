from django.shortcuts import render
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
    return render(request, 'page_list.html',
        {'page_items': page_items, 'text': text})
