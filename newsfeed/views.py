from django.shortcuts import render
from django.http import HttpResponse
from .models import Story
# Create your views here.


def news(request):
    stories_list = Story.objects.all()
    context_dict = {}
    context_dict['stories'] = stories_list
    return render(request, 'News/NewsStories.html', context=context_dict)
