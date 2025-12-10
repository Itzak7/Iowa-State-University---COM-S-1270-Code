#Isaac Aguilar 


def Reading(File):
    with open(File, "r", encoding="utf-8", errors="ignore") as z:
        text = z.read()
    return text

def RemovingASCII(text):
    X = ""
    for ch in text:
        Y = ord(ch)
        if Y == 9 or Y == 10 or Y == 13 or 32 <= Y <=127:
            X += ch 
    return X 

def Cleaned(File,TextV2):
    if File.lower().endswith(".txt"):
        NewFileName = File[:-4] + "_Clean.txt"
    else:
        NewFileName = File + "_Clean.txt"
    with open(NewFileName, "w", encoding="ascii", errors="ignore") as z:
        z.write(TextV2)

def main():
    File = input("Please enter a .txt filename!:")
    Read = Reading(File)
    FinalVersion = RemovingASCII(Read)
    Cleaned(File, FinalVersion)

if __name__ =="__main__":
    main()
