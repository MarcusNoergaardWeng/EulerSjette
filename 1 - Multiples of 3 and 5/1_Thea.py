array = range(1,1000+1)

multiples = []

for n in array:
    if n%3 == 0 or n%5 == 0:
        multiples.append(n)
        
print(sum(multiples))