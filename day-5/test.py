import sys
type=sys.argv[1]
if type=="t2.micro":
    print("2 vCPU, 1 GB RAM")
elif type=="t2.small":
    print("1 vCPU, 2 GB RAM")
elif type=="t2.medium":
    print("2 vCPU, 4 GB RAM")
elif type=="t2.large":
    print("2 vCPU, 8 GB RAM")
else:
    print("Unknown instance type")