from itertools import zip_longest

def zipper(array1, array2):

    max_length = min(len(array1), len(array2))
    return [
        (array1[i], array2[i]) 
        for i in range(max_length)
        ]

try:
    array1 = ["Salvador", "Ubatuba", "Ilhéus"]
    array2 = ["BA", "SP", "MG", "RJ"]


    print(zipper(array1, array2))
    print(list(zip_longest(array1, array2, fillvalue="N/A")))

except Exception as e:
    print(f"An error occurred: {e}")

    