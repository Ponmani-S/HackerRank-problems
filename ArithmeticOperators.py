Problem: Arithmetic Operators
Question

Given two integers, a and b, perform the following operations:

Print the sum of the two numbers.
Print the difference of the two numbers (a - b).
Print the product of the two numbers.


Answer

# Reading input values
a = int(input())
b = int(input())

# Printing the results
print(a + b)  # Sum
print(a - b)  # Difference
print(a * b)  # Product


Explanation

Input: Two integers are taken from the user as input.
Output:
The first output line prints the sum of the two numbers using a + b.
The second output line prints the difference using a - b.
The third output line prints the product using a * b.
The operations are straightforward arithmetic computations.
Sample Input
3
2
Sample Output
5
1
6


Explanation:

The sum of 3 and 2 is 5.
The difference of 3 - 2 is 1.
The product of 3 * 2 is 6.


Complexity Analysis

Time Complexity: O(1), as the operations are basic arithmetic and do not depend on the size of the input.
Space Complexity: O(1), as we only store two integers and the results of arithmetic operations.
