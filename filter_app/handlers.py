def sortByText(data_list, text):
    no_text_list = []
    text_list = []
    new_list = []

    if text == 'yes':
        for data in data_list:
            if len(data['reviewText']) == 0:
                no_text_list.append(data)
            else:
                text_list.append(data)

    if text == 'no':
        new_list = data_list
    else:
        new_list.append(text_list)
        new_list.append(no_text_list)

    return new_list


def sortByRating(lists, rating):
    for i in range(len(lists)):
        if rating == 'highest':
            lists[i] = sorted(lists[i], reverse=True, key=lambda x: x['rating'])
        elif rating == 'lowest':
            lists[i] = sorted(lists[i], key=lambda x: x['rating'])

    return lists


def sortByDate():
    pass
