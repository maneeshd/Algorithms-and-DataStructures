"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 22/6/17

Worst Case Analysis: Insertion Sort -> O(n^2)
"""
from timeit import Timer, default_timer


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j = j - 1
        data[j+1] = key


def main():
    start = default_timer()
    data = [i for i in range(10000, 0, -1)]    # Worst Case Input(Reverse Sorted)
    insertion_sort(data)
    print("Sort Time = %f Seconds" % (default_timer() - start))


if __name__ == '__main__':
    print("Insertion Sort")
    print("-" * len("Insertion Sort"))
    t = Timer(main)
    print("\nAverage sorting time for 10000 elements in 10 runs = %f Seconds" % (t.timeit(10)/10))