def dround(array, decimals=1):
    for i in array.keys():
        array[i] = round(array[i], 2)
    return array


