from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):
    full_text = request.GET['fulltext']
    text_list = full_text.split()
    text_dict = {}
    for word in text_list:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1

    sorted_word = sorted(text_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': full_text, 'count': len(text_list), 'sorted_word': sorted_word})


def about(request):
    return render(request, 'about.html')
