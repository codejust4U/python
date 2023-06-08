A=int(input("A : "))
B=int(input("B : "))
try:
    if (A==0 or A==1) and B==0 or B==1:
        print("----------------------Conjuction-----------------------------")
        def and_operation(A,B):
            res = A and B
            if res == 1:
                print("Conjuction : ",True)
            else:
                print("Conjuction : ",False)
        and_operation(A,B)
        print("------------------------------------------------------")
        print("----------------------Dejuction-----------------------")
        def or_operation(A,B):
            res = A or B
            if res == 1:
                print("Dejuction : ",True)
            else:
                print("Dejuction : ",False)
        or_operation(A,B)
        print("------------------------------------------------------")
        print("----------------------Negation-----------------------")
        def negation_operation(A,B):
            if A==1 or  A==0:
                print("Negation of A: ",not(A))

            if B==1 or  B==0:
                print("Negation of B: ",not(B))
        negation_operation(A,B)
        print("------------------------------------------------------")
        print("----------------------Implication--------------------")
        def implication_operation(A,B):
            if A==1 and B==1:
                res = A and B
                if res == 1:
                    print("Implication : ",True)
                else:
                    print("Implication  : ",False)
            if A==1 and B==0:
                res = A and B
                if res == 1:
                    print("Implication  : ",True)
                else:
                    print("Implication  : ",False)
            if A==0 and B==1:
                res = A or B
                if res == 1:
                    print("Implication  : ",True)
                else:
                    print("Implication  : ",False)
            if A==0 and B==0:
                res = A or B
                if res == 1:
                    print("Implication  : ",True)
                else:
                    print("Implication  : ",False)
        implication_operation(A,B)
        print("------------------------------------------------------")

        print("----------------------Bi-conditional------------------")
        def biconditional_operation(A,B):
            if A==1 and B==1:
                res = A and B
                if res == 1:
                    print("Bi-conditional : ",True)
                else:
                    print("Bi-conditional  : ",False)
            if A==1 and B==0:
                res = A and B
                if res == 1:
                    print("Bi-conditional  : ",True)
                else:
                    print("Bi-conditional  : ",False)
            if A==0 and B==1:
                res = A or B
                if res == 1:
                    print("Bi-conditional  : ",True)
                else:
                    print("Bi-conditional  : ",False)
            if A==0 and B==0:
                res = A or B
                if res == 1:
                    print("Bi-conditional  : ",True)
                else:
                    print("Bi-conditional : ",False)
        biconditional_operation(A,B)
        print("------------------------------------------------------")
    else:
        print("Enter Valid Input")
        
except:
    print("Invalid input")

"""
print("----------------------Conjuction-----------------------------")
def and_operation(A,B):
    res = A and B
    if res == 1:
        print("Conjuction : ",True)
    else:
        print("Conjuction : ",False)
and_operation(A,B)
print("--------------------------------------------------------------")
print("----------------------Dejuction-----------------------------")
def or_operation(A,B):
    res = A or B
    if res == 1:
        print("Dejuction : ",True)
    else:
        print("Dejuction : ",False)
or_operation(A,B)
print("--------------------------------------------------------------")
print("----------------------Negation-----------------------------")
def negation_operation(A,B):
    if A==1 or  A==0:
        print("Negation of A: ",not(A))

    if B==1 or  B==0:
        print("Negation of B: ",not(B))
negation_operation(A,B)
print("--------------------------------------------------------------")
print("----------------------Implication-----------------------------")
def implication_operation(A,B):
    if A==1 and B==1:
        res = A and B
        if res == 1:
            print("Implication : ",True)
        else:
            print("Implication  : ",False)
    if A==1 and B==0:
        res = A and B
        if res == 1:
            print("Implication  : ",True)
        else:
            print("Implication  : ",False)
    if A==0 and B==1:
        res = A or B
        if res == 1:
            print("Implication  : ",True)
        else:
            print("Implication  : ",False)
    if A==0 and B==0:
        res = A or B
        if res == 1:
            print("Implication  : ",True)
        else:
            print("Implication  : ",False)
implication_operation(A,B)
print("--------------------------------------------------------------")

print("----------------------Bi-conditional--------------------------")
def biconditional_operation(A,B):
    if A==1 and B==1:
        res = A and B
        if res == 1:
            print("Bi-conditional : ",True)
        else:
            print("Bi-conditional  : ",False)
    if A==1 and B==0:
        res = A and B
        if res == 1:
            print("Bi-conditional  : ",True)
        else:
            print("Bi-conditional  : ",False)
    if A==0 and B==1:
        res = A or B
        if res == 1:
            print("Bi-conditional  : ",True)
        else:
            print("Bi-conditional  : ",False)
    if A==0 and B==0:
        res = A or B
        if res == 1:
            print("Bi-conditional  : ",True)
        else:
            print("Bi-conditional : ",False)
biconditional_operation(A,B)
print("--------------------------------------------------------------")"""