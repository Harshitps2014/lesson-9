#my chores checklist countdoun
total_chores=4
original_count=total_chores
print(f"you have {original_count} chores to finish today")
completed_count=0
chore_num=1
while chore_num<=total_chores:
    if chore_num==1:
        next_chore="make your bed"
    elif chore_num==2:
        next_chore="feed the pet"
    elif chore_num==3:
        next_chore="take out the trash"
    else:
        next_chore="wash the dishes"
    answer=input(f"have you finished {next_chore}? (yes/no): ")
    if answer=="yes":
        completed_count+=1
        chore_num+=1
        print("great job chores completed")
    else:
        print("okay,finish it and check again")
    print("chores remaining:",total_chores-completed_count)
    print()
print("=======all chores completed===========")
print("great work finishing entire checklist today \n")
print("\n============chore checklist summery==========")
print("chores assigned today:",original_count)
print("chores completed:",completed_count)
print("chores remaining:",total_chores-completed_count)
print("=====================================================")
