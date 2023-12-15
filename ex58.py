def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# PPrincipal
nnumersprimers = 0
b = []

for num in range(1, 101):
    if es_primo(num):
        b.append(num)
        nnumersprimers += 1

print("Hi ha {} números primers i són {}".format(nnumersprimers, b))
