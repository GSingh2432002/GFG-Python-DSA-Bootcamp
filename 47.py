# Maximum Appearing element in ranges
def maxAppear(left, right):
    freq = [0] * 102
    for i in range(len(left)):
        freq[left[i]] += 1
        freq[right[i]+1] -= 1

    max_freq = freq[0]
    max_index = 0
    for i in range(1,100):
        max_freq [i] = max_freq[i] + freq [i-1]
    return  max_index(max(freq))
left = [1, 2, 5, 15]
right = [5, 8, 7, 18]
print(maxAppear(left, right))