# Take Principal (P) , Periode (N) years , Rate Of Intrest (R) %p.a.and
P = float(input('Please enter Principal in INR : '))
N = float(input('Please enter Period in Years : '))
R = float(input('Please enter rate of Intrest in %.p.a. : '))

# Calculate Simple Intrest
I = (P*N*R)/100

# Calculate Amount
A = P + I 

# Print above results
print(f'Simple Intrest for given values is {I:.2f} INR')
print(f'Amount is {A:.2f} INR')
