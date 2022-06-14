def alpha_sort(words):
    words = words.split('-')
    for i in words:
        max_list = [words[0]]
        if i > words[0]:
            max_list.remove(words[0])
            max_list.append(i)
            