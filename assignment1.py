# Name: Tony Miglets
# OSU Email: migletst@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: Oct 21, 2024
# Description:


from static_array import StaticArray

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """Defines a function that takes a static array with integers and returns the minimum and
    maximum values in a tuple"""

    min_val = arr[0]  #Sets min_val to the first index in the Array.

    max_val = arr[0]  #Sets the max_val to the first index in the Array.

    for i in range(1, arr.length()): #Begins the loop to iterate over the Array from index 1 to the total length -1.

        current_val = arr[i]  #Assigns the current index to the current_val container.

        if current_val < min_val:

            min_val = current_val

        elif current_val > max_val:

            max_val = current_val

    return (min_val, max_val) #Returns the values as a tuple.

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """defines a function that returns Fizz, Buzz, and FizzBuzz strings if conditions within a
    static array are met"""

    new_array = StaticArray(arr.length()) #Assigns a new static array with the original values so as to not modify the original

    for i in range(arr.length()):

        value = arr[i]

        if arr[i] % 3 == 0 and arr[i] % 5 == 0: #checks if value is divisible by both 5 and 3.

            new_array[i] = "fizzbuzz"

        elif arr[i] % 3 == 0: #Checks if value is divisible by 3.

            new_array[i] = "fizz"

        elif arr[i] % 5 == 0: #Checks if value is devisible by 5.

            new_array[i] = "buzz"

        else:
            new_array[i] = value #If not divisible by 3 and/or 5, returns the value.

    return new_array

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """defines a function that reverses a static array by swapping elements outward to inward
    by index value"""

    start = 0 #Assigns one pointer to act as a container for swapping.

    end = arr.length() - 1 #Assigns the second point to act as a container for swapping.

    while start < end: #Loops until the two pointers meet in the middle, replacing values out to in.

        temp = arr[start] #Creates a temp container to store the arr[start] value.

        arr[start] = arr[end] #Assigns arr[end] to the now empty arr[start] value.

        arr[end] = temp #arr[end] is now replaced with the temp value.

        start += 1 #Increments the pointer upwards by one value each loop iteration.

        end -= 1 #Increments the pointer downwards by one value each loop iteration.

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """defines a function that rotates a static array by steps(number of times) and returns the new Array"""

    n = arr.length() #creates a variable n, the length of the array, to use in a modulo operator.

    steps = steps % n #Adds a modulo operator to account for large number of steps and reduce needless rotation.
                      # 12 steps % 5 is the same as rotating 2 steps.

    new_arr = StaticArray(n)  # Value created to store rotated values if needed. New array will be same length (n) as StaticArray.

    if steps == 0: #Handles an edge case if the steps are equal to 0.

        for i in range(n):

            new_arr[i] = arr[i] #Assigns new array.

        return new_arr

    if steps > 0:

        for i in range(n):

            new_index = (i + steps) % n #Calculates right rotation while reducing over rotation with a modulo operator.

            new_arr[new_index] = arr[i] #Assigns new array.

    else:

        steps = -steps #Allows us to treat left rotation (negative) like right rotation (positive) for easier calculation.

        for i in range(n):

            new_index = (i - steps) % n #Calculates left rotation while reducing over rotation with a modulo operator.

            new_arr[new_index] = arr[i] #Assigns new array.

    return new_arr



# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """defines a function that receives two integers "start" and "end" as arguments, then returns an array
    with all values between the two integers"""

    size = abs(end - start) + 1 #Calculates the size of the new array.

    result = StaticArray(size) #Creates the new array with the size as the number of elements.

    if start <= end:

        for i in range(size):

            result[i] = start + i #Organizes the values incrementing positively.

    else:

        for i in range(size):

            result[i] = start - i #Organizes the values incrementing negatively.

    return result

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """defines a funciton that checks if a static array is sorted in ascending, descending, no order"""

    n = arr.length() #Assigns length of the array to variable n

    if n == 1: #Handles edge case if there is only one element in the array.

        return 1

    is_ascending = True #Assigns boolean values to ascending and descending.
    is_descending = True

    for i in range(n - 1): #Loops consecutively through the range

        if arr[i] < arr[i + 1]: #Checks if array ascending. Each element must be smaller than the next.
            # Ex. (1 < 2 < 3 < 4).

            is_descending = False

        elif arr[i] > arr[i + 1]: #Checks if array is descending. Each element must be larger than the next.
            # Ex. (4 > 3 > 2 > 1>).

            is_ascending = False

        else:

            return 0

    if is_ascending: #Provides specified return values for each result.
        return 1
    elif is_descending:
        return -1
    else:
        return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """defines a function that finds the mode and frequency of a static array"""

    n = arr.length() #creates variable n equal to length of the array

    mode = arr[0] #Creates a mode container equal to the current index
    mode_count = 1 #Initializes mode to 1
    current_value = arr[0] #Creates a counter to move through the array and increment repeated values
    current_count = 1

    for i in range(1, n):

        if arr[i] == current_value: #Checks if last value is equal to the next value in the array.

            current_count += 1 #If value is the same, increments the counter by 1.

        else: #Once a new value in the index is reached,mode, mode count, current count, and current value are updated, if needed.

            if current_count > mode_count:

                mode = current_value

                mode_count = current_count

            current_value = arr[i]

            current_count = 1

    if current_count > mode_count: #Final check at the end of the loop.

        mode = current_value

        mode_count = current_count

    return (mode, mode_count)



# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """defines a function that removes duplicates from a static array by placing unique elements into a new array"""

    n = arr.length()

    if n <= 1: #Handles edge case if there is only one element, and therefore, no duplicates.

        return arr

    new_arraycount = 1

    for i in range(1, n): #Counts the unique elements for the new array and stores them in new_arraycount

        if arr[i] != arr[i - 1]:

            new_arraycount += 1

    new_array = StaticArray(new_arraycount) #Creates new array with previous count as the number of elements.

    new_array[0] = arr[0] #Sets the first element in the new array as the first element is always unique.

    current_index = 1 #Index for inserting the results into the new array.

    for i in range(1, n):

        if arr[i] != arr[i - 1]:

            new_array[current_index] = arr[i]  # Each unique value is added into the new array.

            current_index += 1

    return new_array


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """defines a function that creates a counting sort algorithm by placing unique elements, in non-ascending order, into a new array"""

    n = arr.length()

    min_val = arr[0] #Create min_val and max_val to find the range and to handle negative numbers(indices) in the array.
    max_val = arr[0]

    for i in range(1, n): #Loop to find the range of the array.

        if arr[i] < min_val:

            min_val = arr[i]

        elif arr[i] > max_val:

            max_val = arr[i]

    size = max_val - min_val + 1
    count = StaticArray(size)

    for i in range(size):
        count[i] = 0 #Initializes all indices in count array to 0's.

    for i in range(n): #Loop that increments each value in the count array, we subtract the min_val to account for negative numbers.

        count[arr[i] - min_val] += 1

    output = StaticArray(n)

    for i in range(1, size): #Loop that adds the previous index to the current index.

        count[i] += count[i - 1]

    for i in range(n -1, -1, -1): #Loop that starts at n - 1, stops when i >= 0, and decrements i by 1 index each loop.

        output[n - count[arr[i] - min_val]] = arr[i] #Places the values from the original array into their sorted indices.

        count[arr[i] - min_val] -= 1 #Decrements count to ensure that a same element, if any, is placed into the correct position.

    return output

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """Defines a function that uses a two pointer method to square an array of integers the sort in non-descending order"""

    n = arr.length()
    squared = StaticArray(n) #The result array for the squared and sorted values
    left = 0 #Initializes left pointer
    right = n - 1 #Initializes right pointer
    squared_index = n - 1 #Array will be filled from the end

    while left <= right: #While loop that squares the left and right indices

        left_square = arr[left] * arr[left]

        right_square = arr[right] * arr[right]

        if left_square > right_square: #Then sorts in non-descending order.

            squared[squared_index] = left_square

            left += 1 #Pointer shifts inward.

        else:

            squared[squared_index] = right_square

            right -= 1 #Pointer shifts inward.

        squared_index -= 1 #Result index moves backwards through the array.

    return squared






# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":



    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')