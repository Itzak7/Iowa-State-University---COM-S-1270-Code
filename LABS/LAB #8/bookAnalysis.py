

def analyzeBook(filename):
    count = {}
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
    #     for line in f:
    #         for word in line.split():
    #             for ch in ['_', '"', ',', '.', '-', '?', '!', "'", '(', ')', ':', '[', ']', ';']:
    #                 word = word.replace(ch, "")
    #             word = word.lower()
    #             if word.isalpha():
    #                 if word in count:
    #                     count[word] += 1
    #                 else:
    #                     count[word] = 1
        for line in f:
            for word in line.split():
                # remove punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')
                # ignore case
                word = word.lower()
                # ignore numbers
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
                
        
    return count


def Results(counts, filename):
    if filename.lower().endswith(".txt"):
        outname = filename[:-4] + "_Analysis.txt"
    else:
        outname = filename + "_Analysis.txt"

    with open(outname, "w", encoding="utf-8", errors="ignore") as x:
        for word, number in sorted(counts.items()):
            x.write(f"{word}: {number}\n")

def main():
    filename = input("Please enter a .txt filename!: ")
    counts = analyzeBook(filename)
    Results(counts, filename)
    print("ALL DONE!!!")


if __name__ == "__main__":
    main()

