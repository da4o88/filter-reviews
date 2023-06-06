from django.shortcuts import render
from .handlers import sortByText, sortByRating, sortByDate
import json
# Create your views here.

with open('data/reviews.json', 'r') as f:
    data = json.load(f)


def home(request):
    reviews = ''
    if request.method == "POST":
        text = request.POST["review-text"]
        rating = request.POST["rating"]
        review_date = request.POST["date-review"]
        min_rating = int(request.POST["min-rating"])


        sorted_list = sortByText(data, text, min_rating)
        sort_rating = sortByRating(sorted_list, rating)
        if len(sort_rating) > 1:
            reviews = sort_rating[0] + sort_rating[1]
        elif len(sort_rating) == 1:
            reviews = sort_rating[0]

    return render(request, 'filter_app/index.html', {"data": reviews, })
