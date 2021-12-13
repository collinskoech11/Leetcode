""""
CodeVue 101 - Introduction
Programming challenge description:

Welcome to CodeVue!

Here's a simple exercise to get you familiar with this coding environment. This panel is where a description of the problem will be presented to you. It could be potentially any programming task that is designed to test your coding skills.

Every problem statement will include a description of how the test cases are set up, including what Input and Output values are expected.

In your code, you will need to work with the input of each test case to produce the expected output. Passing all the test cases is how you win!

In the main coding panel, you should see a some code that is a sample for you to experiment with. Review that code and follow the steps as described to see how things work.

Start by clicking the Run button and revieweing the results in the Output panel.

Input:
Each test case will pass this value to your code through stdin ("Standard In")

Output:
Each test case's Output value will be compared to what your code writes to stdout ("Standard Out").

If your program's output matches the Expected Output, the test case will pass and be shown in green in the output panel.

If your program's output does NOT math the Expected Output for a test case, the result will be displayed in red in the ouytput panel.

Test 1
Test Input
Download Test 1 Input
Test Case 3
Expected Output
Download Test 1 Input
Try writing code to pass all 3 tests
Test 2
Test Input
Download Test 2 Input
This is Test case 2
Expected Output
Download Test 2 Input
This is the expected Output. Try changing the code to write this to STDOUT for this case.
Test 3
Test Input
Download Test 3 Input
This is the input for Test 1
Expected Output
Download Test 3 Input
This is the input for Test 1
"""
# This entire script will be run once for each Test Input.
# The Input for each test will be passed through the filelike object
# `sys.stdin` (STDIN).

# This provides a single line from the Test Input for each iteration.
for line in sys.stdin:
    # You'll want to write some code to pass all of the tests.
    if "1" in line:
        x = "This is the input for Test 1"
    if "2" in line:
        x = "This is the expected Output. Try changing the code to write this to STDOUT for this case."
    if "3" in line:
        x = "Try writing code to pass all 3 tests"

    # This writes `line` to STDOUT.
    print(x)
