from django.shortcuts import render
from .handlers import sortByText, sortByRating, sortByDate
import json

# Read JSON file
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
        sort_rating = sortByRating(sorted_list, rating, text)
        sort_date = sortByDate(sort_rating, text, rating, review_date)

        if len(sort_date) == 2:
            reviews = sort_date[0] + sort_date[1]
        else:
            reviews = sort_date

    return render(request, 'filter_app/index.html', {"data": reviews, })
