"""
Self Describing Numbers
Programming challenge description:
A number is a self-describing number when (assuming digit positions are labeled 0 to N-1), the digit in each position is equal to the number of times that that digit appears in the number.
Input:
Your program should read lines of text from standard input. Each line contains a single positive integer, N.
Output:
For each input N, print 1 to standard output if N is a self-describing number. Otherwise, print 0.

For the curious, here''s how 2020 is a self-describing number: Position 0 has value 2 and there are two 0s in the number. Position 1 has value 0 because there are no 1's in the number. Position 2 has value 2 and there are two 2's. And the position 3 has value 0 and there are zero 3's.
Test 1
"""
def isSElfDescriptiveNumber(num):
    s = str(num)
    for i in range(len(s)):
        temp_char = s[i]
        b = ord(temp_char) - ord('0')
        count = 0
        for j in range(len(s)):
            temp = ord(s[j]) - ord('0')
            if (temp == i):
                count += 1
         if (count != b):
            return False
    return True

if __name__=="__main__":
    for i in range(100000000):
        if (isSelfDescriptiveNumber(i)):
            print(i)
