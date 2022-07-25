from poplib import POP3_PORT


name = "In Search of Lost Typing"
author = "Marcel Pythons"
year = 1992

# Combine these in a tuple
book = (name, author, year)

# Print the name of the book
print(book[0])
print(book[1], book[2])

book2 = {"name": name, "author": author, "year": year}

print(book2["name"])

for data in book2.values():
    if data == 1992:
        print(data)

my_list = [1,2,3]
my_list.append(5)
my_list.append(1)

print(my_list)

my_list.pop(0)

print(my_list)
# the smallest average result

def calculate_avg(dicti: dict):
    avg = 0
    for d in dicti.keys():
        if d == "name": continue
        avg += dicti[d]
    avg = avg / 3

    return avg

def smallest_average(person1: dict, person2: dict, person3: dict):
    
    p1 = calculate_avg(person1)
    p2 = calculate_avg(person2)
    p3 = calculate_avg(person3)

    if p1 < p2 < p3:
        return person1
    elif p2 < p1 < p3:
        return person2
    else:
        return person3

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))

# row sums
def row_sums(matrix: list):
    sum = 0
    for d in matrix:
        sum = 0
        for v in d:
            sum += v
        d.append(sum)

my_matrix = [[1, 2], [3, 4]]
row_sums(my_matrix)
print(my_matrix)