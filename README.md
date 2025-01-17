# Sorting and Algorithm Performance Analysis

## Description

This project provides various sorting algorithms and performance analysis using `matplotlib` to plot execution times. The following algorithms are implemented:

- **Insertion Sort**
- **Bubble Sort**
- **Merge Sort**
- **Quick Sort**

Additionally, the project includes functions for validating parentheses and recursive string operations, with performance measured and plotted over increasing problem sizes.

### Key Features

- **Sorting Algorithms**: Implementations of common sorting algorithms such as insertion sort, bubble sort, merge sort, and quicksort.
- **Performance Analysis**: Plots the execution time of each algorithm based on problem size using `matplotlib`.
- **Recursive Functions**: Demonstrates recursive functions such as palindrome checking and parenthesis validation.
- **Visualization**: Generates graphs to visualize the time complexity of sorting algorithms and other operations.

## Tech Stack

- **Python 3.x**
- **matplotlib** for plotting
- **time** for measuring execution times
- **sys** for recursion limit adjustments

## Code Overview

### Functions

- **`worstlst(x)`**: Generates a worst-case list of length `x` (sorted in reverse order).
- **`getGraph(name, functionName, worstcase, repeattime)`**: Plots the performance of a given function over increasing problem sizes.
- **`insertionsort(lst)`**: Performs insertion sort on the provided list.
- **`bubblesort(lst)`**: Performs bubble sort on the provided list.
- **`mergesort(lst)`**: Sorts a list using the merge sort algorithm.
- **`quicksort(lst)`**: Sorts a list using the quicksort algorithm.
- **`swap(lst, x, y)`**: Swaps two elements in the list.
- **`shuffle(lst)`**: Randomly shuffles the elements in the list.
- **`parenthesisvalidator3(str)`**: Validates whether a string of parentheses is correctly balanced using recursion.

### Performance Analysis

For each sorting algorithm, the execution time is measured and plotted as the input size increases. The `getGraph` function is used to generate these plots, visualizing the performance of each algorithm.
