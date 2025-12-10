def PalindromeIterative(A):
    left = 0
    right = len(A) - 1
    while left < right:
        if A[left] != A[right]:
            return False
        left += 1
        right -= 1
    return True


def PalindromeRecursive(A):
    if len(A) <= 1:
        return True
    if A[0] != A[-1]:
        return False
    return PalindromeRecursive(A[1:-1])


def main():
    Answer = input("Please enter a word of your choice!!!: ")
    X = (PalindromeIterative(Answer))
    Y = (PalindromeRecursive(Answer))
    print(f"Your answer from the Iterative method is: {X}")
    print(f"Your answer from the Recursive method is: {Y}")


if __name__ == "__main__":
    main()
