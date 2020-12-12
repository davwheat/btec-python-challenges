import math


class Question:
    def __init__(self, lines):
        self.question = lines[0]
        self.a = lines[1]
        self.b = lines[2]
        self.c = lines[3]
        self.d = lines[4]
        self.answer = lines[5].lower()

    def ask(self):
        print(self.question)
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)

        response = ""
        while not response in ["a", "b", "c", "d"]:
            # invalid answer
            response = input("Answer: ").lower()

        return response

    def isCorrect(self, response):
        return response == self.answer


allLines = []
allQuestions = []
score = 0
askedQuestions = 0

with open("questions.txt", "r") as f:
    text = f.read()
    allLines = text.splitlines(False)

for i in range(math.floor(len(allLines) / 6)):
    baseIndex = 6 * i
    allQuestions.append(
        Question(
            [
                allLines[baseIndex + 0],
                allLines[baseIndex + 1],
                allLines[baseIndex + 2],
                allLines[baseIndex + 3],
                allLines[baseIndex + 4],
                allLines[baseIndex + 5],
            ]
        )
    )

for q in allQuestions:
    askedQuestions += 1
    answer = q.ask()
    if q.isCorrect(answer):
        # correct
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    print("")

print(f"You scored {score} of {askedQuestions}")
