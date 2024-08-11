emailid=input('Enter your email: ').split("@")
domain=emailid[1]
pos=domain.index(".")
domain=domain[:pos]
print("The domain is: ", domain)
