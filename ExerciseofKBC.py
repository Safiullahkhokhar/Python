questions= [["Which language was used to create youtube?",
            'Python','Java','Php','None', 4],
["Which language was used to create Google?",
            'Python','Java','Php','None', 4],
["Which language was used to create Facebook?",
            'Python','Java','Php','None', 4],
["Which language was used to create Amazon?",
            'Python','Java','Php','None', 4],
["Which language was used to create Microsoft?",
            'Python','Java','JavaScript','None', 4]]

levels = [1000, 2000, 3000, 5000, 10000]
money =0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nQueation for Rs. {levels[i]}")
    print(f"a.{question[1]} b.{question[2]}")
    print(f"c.{question[3]} c.{question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have on Rs. {levels[i]}")
        if(i == 4):
            money == 10000
    else:
            print('Wrong answer!')

print(f"Your take home money is {money}")

