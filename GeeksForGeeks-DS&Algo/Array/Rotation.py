# Naive Rotation right:
# 1. Consider a temporary array to store elements upto the rotation count.
# 2. Shift left the remaining 'length_ar - k' elements.
# 3. Now add back the elements of the temporary array to the main array and return the array.
# Time complexity: O(n)
# Space complexity: O(k)
#
#
# Rotate 1 element each time right:
# 1. In this, instead of taking a temporary array, we take a temporary variable to store the single element which we
#     rotate at a time.
# 2. For each element upto index k, take that element into temporary variable and shift left the remaining elements.
#     Then add back the temporary variable to the end of the main list.
#
# Time Complexity: O(n*k)
# Space Complexity: O(1)
#
# Juggling Algorithm
#


import math


def naive_rotate(ar, k):
    len_ar = len(ar)
    k = k%len_ar
    b = [0]*k
    for i in range(k):
        b[i] = ar[i]

    for i in range(len_ar-k):
        ar[i] = ar[k+i]

    for i in range(k):
        ar[len_ar-k+i] = b[i]

    return ar


def juggling_algorithm(ar, k):
    n = len(ar)
    gcd = math.gcd(n, k)
    for i in range(gcd):
        temp_val = ar[i]
        j = i
        while 1:
            temp = j + k

            if temp >= n:
                temp = temp-n

            if temp == i:
                break

            ar[j] = ar[temp]
            j = temp

        ar[j] = temp_val

    return ar


ar = [3, 7, 8, 4, 6, 2]
print('Array before rotation', ar)
print('Array after k=4 rotation', juggling_algorithm(ar, 4))
