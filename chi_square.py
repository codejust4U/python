data1 = [30,35,20,10,5]
expected_val = int(input("Enter the expected value: "))
chi = []
sum = 0
for i in range(len(data1)):
    chi = ((data1[i]-expected_val)**2)/expected_val
    sum=sum+chi
    print(f"Individual sum and Previous sum for iteration: {i+1}: ",sum)

print("\n\nTotal sum:",sum)
