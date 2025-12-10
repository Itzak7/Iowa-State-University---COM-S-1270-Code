def reverseIterative(A):
    result = ""
    for i in A:
        result = i + result
    return result


def reverseRecursive(A):
    if len(A) <= 1:
        return A
    return A[-1] + reverseRecursive(A[:-1])


def main():
    Answer = input("Please enter a word of your choice!!!: ")
    X = (reverseIterative(Answer))
    Y = (reverseRecursive(Answer))
    print(f"Your answer from the Iterative method is: {X}")
    print(f"Your answer from the Recursive method is: {Y}")


if __name__ == "__main__":
    main()
