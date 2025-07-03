try: 
    array = [i for i in range(10) if i % 2 != 0] # even numbers
    print(array)
    
    array2 = [i for i in range(10) if i % 2 == 0] # odd numbers
    print(*array2, sep = "\n") # Unpacking the list for printing each element on a new line
    print(array2, sep = "\n") # Printing the entire list
    
except Exception as e:
    print(f"An error occurred: {e}")
