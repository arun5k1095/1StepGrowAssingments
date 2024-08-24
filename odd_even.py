temperatures = [-1,50,6,-46,-20,81,74,41,24,-60,-2,17,23,28,57,29,-16,-4,29,9,11,2,4,6,13,-18]
even = []
odd = []
for temp in temperatures:
    if temp % 2 == 0:
        even.append(temp)
    else:
        odd.append(temp)
print("Even temperatures: ", even)
print("Odd temperatures: ", odd)