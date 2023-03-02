import sys
import threading
import numpy


def compute_height(n, parents):
    heights = numpy.zeros(n)
    max_height = 0

    for i in range(n):
        node = i
        height = 0
        while node != -1:
            if heights[node] != 0:
                height += heights[node]
                break

            height += 1
            node = parents[node]

        heights[i] = height
        if height > max_height:
            max_height = height

    return int(max_height)

def main():
    # implement input form keyboard and from files
    input_type = input("F or I: ")

    if "I" in input_type or "i" in input_type:
        n = int(input("Count: "))
        parents = list(map(int, input("Nodes: ").split()))
        max_height = compute_height(n, parents)

    elif "F" in input_type or "f" in input_type:
        test_num = input("Choose test number (01-25): ")
        with open(f"test/{test_num}", "r") as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            max_height = compute_height(n, parents)

    print(max_height)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()