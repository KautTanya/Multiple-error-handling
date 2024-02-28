"""Multiple-error-handling"""
num_input = input("Enter numbers separated by commas: ")
num_list = num_input.split(", ")
new_list = []

try:
    for number in num_list:
        new_list.append(int(number))
    print(new_list)
    index_input = int(input("Enter the index: "))
    print(new_list[index_input])
except ValueError:
    print("This is not an integer")
except IndexError:
    print("No such index exists")
