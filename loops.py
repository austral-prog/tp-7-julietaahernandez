def index_of_by_index(word, list, index):
    for new_index in range(index, len(list)):
        if list[new_index] == word:
            return new_index
    return -1


def index_of_empty(list):
    for index, color in enumerate(list):
        if color == "":
            return index
    return -1

def index_of(word, list):
    index = 0 
    for color in list:
        if color == word:
            return index 
        index += 1
    return -1

def put(word, list):
    for index, color in enumerate(list):
        if color == "":
            list [index] = word 
            return index 
    return -1

def remove(word, list):
    counter = 0
    for index, color in enumerate(list):
        if color == word:
            list [index] = "" 
            counter += 1 
    return counter 
    return -1
