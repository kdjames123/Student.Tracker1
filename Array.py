A = ["Alex", "Abby", "18" , "5'2", "913-332-4184" ]
B = ["Bobby", "Back", "21" , "6'0", "913-519-2953" ]
C = ["Chris", "Clab", "18" , "5'5", "913-459-8452" ]
All = [A,B,C]

find = input("Would you like to know the first, second, or third? ")

if find == "1" or find.lower() == "first":
    print("First name " + All[0][0])
    print("Last name " + All[0][1])
    print("Age " + All[0][2])
    print("Height " + All[0][3])
    print("Phone number" + All[0][4])
    
elif find == "2" or find.lower() == "second":
    print("First name " + All[1][0])
    print("Last name " + All[1][1])
    print("Age " + All[1][2])
    print("Height " + All[1][3])
    print("Phone number" + All[1][4])
elif find == "3" or find.lower() == "third":
    print("First name " + All[2][0])
    print("Last name " + All[2][1])
    print("Age " + All[2][2])
    print("Height " + All[2][3])
    print("Phone number " + All[2][4])

guess = input("What is the first name of whom you want to find? ")

for i in All:
    if i[0] == guess:
        print("First name " + i[0])
        print("Last name " + i[1])
        print("Age " + i[2])
        print("Height " + i[3])
        print("Phone number " + i[4])

x = input("Would you like to add a column to each person? ")
if x == "yes":
    add = input("What category would you like to add? ")
    for i in All:
        i.append(input("What would you like to add for " + i[0] + " "))
    print("You added the " + add + " category to " + All[0][0] + ", " + All[1][0] + ", " + All[2][0])
    print("Alex has " + All[0][5])
    print("Bpbby has " + All[1][5])
    print("Chris has " + All[2][5])

x = input("Would you like to add a row for yourself? ")
if x == "yes":
    D = [str(input("What is the first name? ")), str(input("What is the last name? ")) , str(input("What is your age? ")),
         str(input("What is your height? ")), str(input("What is your phone number? "))]

    All.append(D)
    print("You added ")
    print("First name " + All[3][0])
    print("Last name " + All[3][1])
    print("Age " + All[3][2])
    print("Height " + All[3][3])
    print("Phone number" + All[3][4])
find1 = input("would you like to find another string? ")
if find1 == "yes":
    discover = input("What is the first name? ")
    for i in All:
        if i[0] == discover:
            for i in All:
                print("First name " + i[0])
                print("Last name " + i[1])
                print("Age " + i[2])
                print("Height " + i[3])
                print("Phone number " + i[4])
