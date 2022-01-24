import random
def rand_elem(arr):
    if arr == []:
        return "Invalid input"
    return random.choice(arr)


for index,test in enumerate(tests):
    print(f"Test nr {index+1}")
    print(rand_elem(**test))
    print("-----------------------")