#!/usr/bin/env python
# coding: utf-8

# In[1]:


import winsound

def mergeSort(array):
    if len(array) > 1:
        pivot = len(array)//2
        left = array[:pivot]
        right = array[pivot:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
                # Play a sound effect for the swap
                winsound.Beep(500, 200)
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

def main():
    array = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    print("Original Array:", array)
    mergeSort(array)
    print("Sorted Array:", array)

if __name__ == "__main__":
    main()


# In[ ]:




