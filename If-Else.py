Problem: Python If-Else
Question

Given an integer n, perform the following conditional actions:

If n is odd, print Weird.
If n is even and in the inclusive range of 2 to 5, print Not Weird.
If n is even and in the inclusive range of 6 to 20, print Weird.
If n is even and greater than 20, print Not Weird.

Answer

# Reading the integer input
n = int(input().strip())

# Conditional checks
if n % 2 == 1 or (n % 2 == 0 and 6 <= n <= 20):
    print("Weird")
else:
    print("Not Weird")


Explanation

Odd Numbers: If the number is odd (i.e., n % 2 == 1), it will print Weird.
Even Numbers: If the number is even:
For values between 2 and 5 (inclusive), it will print Not Weird.
For values between 6 and 20 (inclusive), it will print Weird.
For values greater than 20, it will print Not Weird.
The logic uses the modulo operation % to check if a number is even or odd and checks for the specified ranges using conditional operators.


Complexity Analysis

Time Complexity: O(1), since we are only checking a few conditions and performing basic arithmetic.
Space Complexity: O(1), as we only need space for the integer n and a few conditions.
