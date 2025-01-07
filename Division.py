Problem: Python: Division
Question

Given two integers, a and b, perform the following operations:

Print the result of integer division, a // b.
Print the result of float division, a / b.
Note: No rounding or formatting is required.

Answer


# Reading input values
a = int(input())
b = int(input())

# Printing the results
print(a // b)  # Integer division
print(a / b)   # Float division


Explanation

Input: The program reads two integers, a and b.
Output:
The first line prints the result of integer division using the // operator, which discards the decimal part.
The second line prints the result of float division using the / operator, which includes the decimal part.
Key Points:
Integer division (//) truncates any fractional part of the result.
Float division (/) produces a precise result including decimals.

Sample Input
4
3

Sample Output
1
1.3333333333333333


Explanation:

The result of 4 // 3 is 1 because it performs integer division, discarding the remainder.
The result of 4 / 3 is 1.3333333333333333, which includes the fractional part.


Complexity Analysis

Time Complexity: O(1), as division operations take constant time.
Space Complexity: O(1), as we only store two integers and their results.
