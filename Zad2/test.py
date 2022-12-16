import json

with open("quiz.json","r") as file:
    content=file.read()

#print(content)
data = json.loads(content)
score=0

for q in data:
    print(q["question_text"])

    for i,choice in enumerate(q["alternatives"]):
        print(i+1, "-" ,choice)

    answer=int(input())
    q["choice"]=answer
    if q["choice"]==q["correct"]:
        score=score+1

for i,que in enumerate(data):
    message=f"{i+1}. You answer: {que['choice']}, "\
            f"Correct answer is: {que['correct']}"
    print(message)

print(f"You got {score} points / {len(data)} points")

#print(type(content))
#print(type(data))