def enumerate_list(list):
    new_list = []
    counter = 0
    for index, element in enumerate(list):
        if element != "":
            new_list.append(f"{counter}. {element}")
            counter += 1
    return new_list

def enumerate_backwards(list):
    new_list = []
    counter = 0
    for index, element in enumerate(list):
        if element != "":
            element = element [::-1]
            new_list.append(f"{counter}. {element}") 
            counter += 1
    return new_list
