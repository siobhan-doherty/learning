# splitting list of numbers 1 to 100 into odds and evens

listDemo = list(range(1, 100))
print(listDemo)
odd = listDemo[::2]
print("Odd numbers:\n", odd)
even = listDemo[1::2]
print("Even numbers:\n", even)
