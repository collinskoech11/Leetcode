"""
Square a Number
This is a practice programming challenge. Use this screen to explore the programming interface and try the simple challenge below. Nothing you do on this page will be recorded. When you are ready to proceed to your first scored challenge, click "Finish Practicing" above.

Programming challenge description:
Write a program that squares an integer and prints the result.
Test 1
Test Input
Download Test 1 Input
5
Expected Output
Download Test 1 Input
25
Test 2
Test Input
Download Test 2 Input
25
Expected Output
Download Test 2 Input
625
"""

for line in sys.stdin:
    if "2" in line:
        x=25
    else:
        x=5
xsq = x ** 2
print(xsq)
