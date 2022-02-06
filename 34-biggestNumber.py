l = [6, 10, 20,4,77,45]

'''biggest= l[0]

for number in l:
    if number > biggest:
        biggest=number
print(biggest)
'''
def biggest(numbers):
    biggest = numbers[0]

    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest

print(biggest((l)))
