import numpy as np
num1 = np.array([2, 2, 3, 2, 1])
num2 = np.array([2, 3, 4, 3, 1])
print("Original arrays:")
print(num1)
print(num2)
print("\n Test said two arrays are equal (element wise) or not:?")
print(num1 == num2)
print(np.equal(num1, num2))
