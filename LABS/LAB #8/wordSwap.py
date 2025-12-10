
import random 

def wordSwap(Sentence):
    words = Sentence.split()
    swappedSentence = {}
    for i in words:
        if i not in swappedSentence:
            swappedSentence[i] = random.choice(words)
    print("Your word swap dictionary:")
    print(swappedSentence)
    newSentence = [swappedSentence[i] for i in words]
    print("Your new swapped sentence!:")
    print(" ".join(newSentence))

def main():
    Sentence = input("Please type a sentence of your choice!: ")
    wordSwap(Sentence)

if __name__ == "__main__":
    main()