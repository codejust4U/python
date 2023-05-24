#this code is only valid for the input 4,3 and 5,3 and the target is 2 in jug2
jug1_liter = int(input("Enter the liters of 1st jug: "))
jug2_liter = int(input("Enter the liters of 2nd jug: "))
target_liter = int(input("Enter the target liters: "))

print("Jug1 : ",jug1_liter,"\njug2: ",jug2_liter,"\nTarget : ",target_liter)
jug1 = 0
jug2 = 0
if  jug1 == 0 or jug2 == 0:
    print(jug1,jug2)
    jug1 += jug1_liter
    print(jug1,jug2)
    if jug2 == target_liter:
        print("You got your desired output")
    elif jug2!=target_liter:
        jug1 = jug1_liter - jug2_liter
        jug2 = jug2 + jug2_liter
        print(jug1,jug2)
        if jug2 == target_liter:
            print("You got your desired output")
        elif jug2 != target_liter:
            jug2 = jug2-jug2_liter
            print(jug1,jug2)
            if jug2 == target_liter:
                print("You got your desired output")
            elif jug2 != target_liter:
                jug2 = jug1
                jug1 -= jug1
                print(jug1,jug2)
                if jug2 == target_liter:
                    print("You got your desired output")
                elif jug2!=target_liter:
                    jug1=jug1+jug1_liter
                    print(jug1,jug2)
                    if jug2==target_liter:
                        print("You got your desired output")
                    elif jug2!=target_liter:
                        amount_needed = jug2_liter-jug2
                        jug1 = jug1 - amount_needed
                        jug2 = jug2 + amount_needed
                        print(jug1,jug2)
                        if jug2 == target_liter:
                            print("You got your desired output")
                        elif jug2!=target_liter:
                            jug2 -= jug2
                            print(jug1,jug2)
                            if jug2==target_liter:
                                print("You got your desired output")
                            elif jug2!=target_liter:
                                jug1,jug2 = jug2,jug1
                                print(jug1,jug2)
                                print("You got your desired output")



else:
    print("Invalid")
