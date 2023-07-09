class Solution:
    """"
    The rules for generating Collatz Sequence are: If n is even: n = n / 2 If n is odd: n = 3n+ 1 For example, if the starting number is 5 the sequence is: 5 -> 16 -> 8 -> 4 -> 2 -> 1 been proved for almost all integers, the repeated application of the above rule will result in a sequence that ends at 1.
The input containing an integer 'n' which denotes the given number. Print the numbers in the sequence as output.
    """
    @staticmethod
    def collatz_sequence(n):
        ans=[n]
        while n>1:
            if n%2==0:
                n//=2
                ans.append(n)
            else:
                n=3*n+1
                ans.append(n)
        return ans

if __name__ == '__main__':
    obj=Solution()
    print(*obj.collatz_sequence(5))
    print(*obj.collatz_sequence(1))
    print(*obj.collatz_sequence(4))