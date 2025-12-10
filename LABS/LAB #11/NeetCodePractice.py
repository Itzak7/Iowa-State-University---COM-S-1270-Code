
def hasDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i]== nums[i-1]:
            return True
    return False

def isAnagram( s,t):
    if len(s) != len(t):
        return False 
        
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

def topKFrequent( nums, k):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    arr = []
    for num, cnt in count.items():
        arr.append([cnt, num])
    arr.sort()

    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    return res


def main():
    X = [1,2,3,3]
    answer = hasDuplicate(X)
    print(f"{answer}")
    print("----------------------")
    S = "racecar"
    T = "carrace"
    answer2 = isAnagram(S,T)
    print(f"{answer2}")
    print("----------------------")
    K =  2
    Nums = [1,2,2,3,3,3]
    answer3 = topKFrequent(Nums, K)
    print(f"{answer3}")



if __name__ == "__main__":
    main()