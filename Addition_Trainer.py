from random import randint

def Operation_1():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 1  
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve: 
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def Operation_2():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 2
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def Operation_3():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 3
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def Operation_4():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 4
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def Operation_5():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 5
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def Operation_6():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 6
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def Operation_7():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 7
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def Operation_8():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 8
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def Operation_9():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 9
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def Operation_10():
    numb_1 = randint (0, 99)
    numb_2 = randint (0, 99)

    prog_round = 10
    print(f"Round {prog_round}!")
    print(f"Solve for the sum of {numb_1} + {numb_2}.")   
    Ans = int(input(f"Answer: "))
    solve = numb_1 + numb_2
    
    if Ans == solve:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def final_score(score1, score2, score3, score4, score5, score6, score7, score8, score9, score10):
    total_score = score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10
    print(f"You have a score of {total_score}/10!")

def main():
    score1_count = Operation_1()
    score2_count = Operation_2()
    score3_count = Operation_3()
    score4_count = Operation_4()
    score5_count = Operation_5()
    score6_count = Operation_6()
    score7_count = Operation_7()
    score8_count = Operation_8()
    score9_count = Operation_9()
    score10_count = Operation_10()
    final_score(score1_count, score2_count, score3_count, score4_count, score5_count, score6_count, score7_count, score8_count, score9_count, score10_count)
    
main()