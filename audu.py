class Problem:

    def calc_area():
        l = float(input())
        b = float(input())
        return l*b
    
    def calc_volume():
        l = float(input())
        b = float(input())
        h = float(input())
        return l*b*h
    


print(Problem.calc_area())
print(Problem.calc_volume())