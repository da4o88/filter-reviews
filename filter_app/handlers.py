def sortByText(data_list, text='no', min_rating=1):
    no_text_list = []
    text_list = []
    new_list = []

    if text == 'yes':
        for data in data_list:
            if len(data['reviewText']) == 0 and int(data['rating']) >= min_rating:
                no_text_list.append(data)
            elif int(data['rating']) >= min_rating:
                text_list.append(data)
    elif text == 'no':
        for data in data_list:
            if int(data['rating']) >= min_rating:
                no_text_list.append(data)

    if text == 'no':
        new_list = no_text_list
    else:
        new_list.append(text_list)
        new_list.append(no_text_list)

    return new_list


def sortByRating(lists, rating, text):
    if text == 'yes':
        for i in range(len(lists)):
            if rating == 'highest':
                lists[i] = sorted(lists[i], reverse=True, key=lambda x: x['rating'])
            elif rating == 'lowest':
                lists[i] = sorted(lists[i], key=lambda x: x['rating'])
    elif text == 'no':
        if rating == 'highest':
            lists = sorted(lists, reverse=True, key=lambda x: x['rating'])
        elif rating == 'lowest':
            lists = sorted(lists, key=lambda x: x['rating'])

    return lists


def sortByDate(dates, text, rating, review_date):

    if text == 'yes':
        for i in range(len(dates)):
            dates[i] = dateSorting(dates[i], rating, review_date)
    elif text == 'no':
        dates = dateSorting(dates, rating, review_date)

    return dates


def dateSorting(reviews, ratings, review_date):
    rating_5 = []
    rating_4 = []
    rating_3 = []
    rating_2 = []
    rating_1 = []
    sort_dates = [rating_5, rating_4, rating_3, rating_2, rating_1]
    sorted_dates = []

    for data in reviews:
        if data['rating'] == 5:
            rating_5.append(data)
        elif data['rating'] == 4:
            rating_4.append(data)
        elif data['rating'] == 3:
            rating_3.append(data)
        elif data['rating'] == 2:
            rating_2.append(data)
        elif data['rating'] == 1:
            rating_1.append(data)

    # Change order of list from highest to lowest
    if ratings == 'lowest':
        sort_dates.reverse()

    # Sort by date
    for rating in sort_dates:
        if review_date == 'newest':
            rating.sort(reverse=True, key=lambda x: x['reviewCreatedOnDate'])
            sorted_dates += rating
        elif review_date == 'oldest':
            rating.sort(key=lambda x: x['reviewCreatedOnDate'])
            sorted_dates += rating

    return sorted_dates
