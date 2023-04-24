def ToH(n , source, target, aux):
	if n==1:
		print ("Move disk 1 from source",source,"to destination",target)
		return
	ToH(n-1, source, aux, target)
	print ("Move disk",n,"from source",source,"to destination",target)
	ToH(n-1, aux, target, source)
		

n = int(input("Enter the number of disks: "))
ToH(n,'A','B','C')
