def getStudentNames(file):
    students = {}
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        next(f)
        for line in f:
            X = line.strip().split(",")
            if len(X) == 2:
                studentID = X[0].strip()
                studentName = X[1].strip()
                students[studentID] = studentName
    return students

def getStudentScores(file):
    scores = {}
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        next(f)
        for line in f:
            X = line.strip().split(",")
            if len(X) == 3:
                studentID = X[0].strip()
                studentScore = float(X[2].strip())
                if studentID not in scores:
                    scores[studentID] = []
                scores[studentID].append(studentScore)
    return scores

def getResults(students,scores):
    Grades = [["Student ID","Name","Total Scores","Sum of All Scores","Score Average"]]
    for StudentID, name in students.items():
        if StudentID in scores:
            total = len(scores[StudentID])
            totalSum = sum(scores[StudentID])
            average = round(totalSum/total,1)
        else:
            total = 0
            totalSum = 0
            average = 0.0
        Grades.append([StudentID, name, str(total), str(int(totalSum)), str(average)])
    
    with open("grades.txt", "w", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(Grades):
                f.write(",".join(line))
                if i < len(Grades) - 1:
                    f.write("\n")


def main():
    students = getStudentNames("students.txt")
    scores = getStudentScores("scores.txt")
    getResults(students, scores)
    print("ALL DONE!!!")

if __name__=="__main__":
    main()
            