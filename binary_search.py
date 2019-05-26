random_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
searched_number = int(2)

def binary_search_main(random_array, searched_number):
    a = False
    while a != True:
        binary_search_engine(random_array, searched_number)

def binary_search_engine(random_array, searched_number):
    if len(random_array) > 3:
        n = len(random_array) / 2
        if n > searched_number:
            random_array = random_array[0, n]
            return random_array
        elif n < searched_number:
            random_array = random_array[n, -1]
            return random_array
        else:
            return a == False
    else:
        return a == True

