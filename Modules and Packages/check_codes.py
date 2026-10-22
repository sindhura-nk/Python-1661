# Calculate fibonacci numbers for a series of 10 numbers
import calculate_fibo
series = calculate_fibo.fibonacci(10)
print("Fibonacci Output",list(series))

# Calculate cube of a number 5
from cube import cube_cal
op = cube_cal(5)
print("cube of a number",op)

# Gather user info and save it in a file
from gather_user_info import user_info
user_info()

# Let's import operations package and access the modules within it
# First add the folder path to sys. This will help python to access the package
import sys
sys.path.append(r"E:\Sindhura\3RI\Python 1661")

# import package along with module
# from package.module import method
from Operations.summation import summation_cal
s1 = summation_cal(90,87)
print("summation output",s1)

from Operations.product import prod
p1 = prod(10,20)
print("product output",p1)