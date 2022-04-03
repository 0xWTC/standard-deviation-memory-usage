'''
calculate standard deviation of a large random 
array of numbers using the statistics library
calculate how much ram the process is using
'''

import statistics
import psutil
import os
import random

def main(list_size, range_size):
    # create an array of numbers using list comprehension
    numbers = [random.randint(0, range_size) for _ in range(list_size)]
    # calculate the standard deviation of the list
    standard_deviation = statistics.stdev(numbers)
    # print the standard deviation
    print("Standard deviation:", standard_deviation)
    # calculate the memory usage of the program in MegaBytes
    memory_usage = psutil.Process(os.getpid()).memory_info().rss / 1000000
    # print the memory usage
    print("Memory usage:", memory_usage, "MB")

# run the main function
if __name__ == "__main__":
    main(1000000, 10000)
