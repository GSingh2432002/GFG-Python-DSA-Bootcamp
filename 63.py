# Insertion Sort
# This line defines a function named 'insertionsort' that takes a single parameter 'l' which is expected to be a list.
def insertion_sort(l):
    # This loop iterates over the list starting from the second element(index 1) to the last element. The variable 'i' is the current index of the element being considered for insertion into the sorted portion of the list.
    for i in range(1, len(l)):
        x = l[i] # This line stores the value of the current element(the one to be inserted into its correct position in the sorted portion of the list) in the variable 'x'.
        j = i - 1 # This initializes 'j' to index of the last element in the sorted portion of the list. Initially 'j' is one position to the left of 'i'.
        
        # This 'while' loop runs as long as 'j' is a valid index and the value of 'x' is less than the value of the element at index 'j' in the list. This condition ensures that 'x' is inserted into its correct position by comparing it with each element in the sorted portion from right to left.
        while j>=0 and x < l[j]:
            l[j+1] = l[j] # If 'x' is less than 'l[j]' this line shifts 'l[j]' one position to the right to make space for 'x'. The element at 'j+1' now holds the value of 'l[j]'.
            j = j - 1 # This line decrements 'j' by 1, moving the comparison to the next element to the left in the sorted portion of the list.
            l[j+1] = x # After the 'while' loop ends this line inserts ''x' into the correct position. 'j+1' is the correct index because 'j' was decremented one step too far in the last iteration of the loop.
l = [20,5,40,60,10,30]
insertion_sort(l)
print(*l)