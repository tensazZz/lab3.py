#1.1
n = input()
t = tuple(n)
print(t)

#1.2
n = input()
t = tuple(n)
s = ''.join(t)
print(s)

#1.3

def concatenate_tuples(A, B):
    midpoint = len(A) // 2
    result = A[:midpoint] + B[midpoint:]

    return result

tuple_A = (1, 2, 3, 4, 5)
tuple_B = ('a', 'b', 'c', 'd', 'e')

concatenated_tuple = concatenate_tuples(tuple_A, tuple_B)
print(concatenated_tuple)

#4
tuple_A = (1, 2, 3, 4, 5, 6, 7)
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
middle_A = len(tuple_A) // 2 + len(tuple_A) % 2
middle_B = len(tuple_B) // 2
first_half_A = tuple_A[:middle_A]
second_half_B = tuple_B[middle_B:]
result_tuple = first_half_A + second_half_B
print(result_tuple)

#4
def count_elements(input_tuple):
    count_dict = {}
    for element in input_tuple:
        if isinstance(element, list):
            key = tuple(element)
        else:
            key = element
        if key in count_dict:
            count_dict[key] += 1
        else:
            count_dict[key] = 1
    result_tuple = tuple((key, count_dict[key]) for key in count_dict)
    return result_tuple
samples = [
    (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6),
    ('55', '6', '777', 54, 6, 7777, 9, 777, 6),
    ((1,2,3), (['A', 'B']), (1,2,3), (['A']))
]
for sample in samples:
    result = count_elements(sample)
    print(result)

#1.5
def segregate_by_type(input_tuple):
    int_tuple = tuple(x for x in input_tuple if isinstance(x, int))
    float_tuple = tuple(x for x in input_tuple if isinstance(x, float))
    str_tuple = tuple(x for x in input_tuple if isinstance(x, str))
    return int_tuple, float_tuple, str_tuple
sample_input = (55, 6, 777, 70.0, '7', 'A')
int_result, float_result, str_result = segregate_by_type(sample_input)
print(int_result)
print(float_result)
print(str_result)

#2.1
user_input = input()
created_set = {char for char in user_input}
print(created_set)

#2.2
user_input = input()
created_set = {char for char in user_input}
print(created_set)

#2.3
set_A = {1,2,3,4,5}
set_B = {5,7,8,9,2,10}
set_A.difference_update(set_B)
print(set_A)

#2.4
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}
for element in set_C:
    if element in set_A:
        set_A.remove(element)
        set_B.add(element)
print(set_A)
print(set_B)

#2.5
from itertools import combinations
A = {1,2,3,4,5,6}
n = 3
m = 5
combinations_set = list(combinations(A, n))
selected_combinations = combinations_set[:m]
result_list = [set(comb) for comb in selected_combinations]
print(result_list)

#3.1
from itertools import groupby
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'),
             ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]
cars_list.sort(key=lambda x: x[0])
for key, group in groupby(cars_list, key=lambda x: x[0]):
    print(f"{key} {len(list(group))}")
    for car in group:
        print(f"- {car[1]}")

#bonus
data = (5, 55, 10, 1, 0, 1, 55, 77, 10, 5, 5, 55, 77)
from collections import Counter
counter = Counter(data)
items = list(counter.items())
max_occurrence = max(counter.values())
min_occurrence = min(counter.values())
most_popular = [item for item in items if item[1] == max_occurrence]
least_popular = [item for item in items if item[1] == min_occurrence]
frequent_occurrences = Counter(counter.values())
frequent_values = [value for value, count in frequent_occurrences.items() if count > 1]
frequent_elements = [item for item in items if item[1] in frequent_values]