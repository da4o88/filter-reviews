from django.shortcuts import render
from .handlers import sortByText, sortByRating, sortByDate
import json
# Create your views here.

with open('data/reviews.json', 'r') as f:
    data = json.load(f)


def home(request):
    text = "yes"
    sorted_list = sortByText(data, text)
    sort_rating = sortByRating(sorted_list, "highest")
    print(sort_rating)
    return render(request, 'filter_app/index.html')
