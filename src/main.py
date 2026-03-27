# Task A: Functions as Objects

def apply_twice(func, x):
    return func(func(x))

print(apply_twice(lambda x: x + 1, 3))
print(apply_twice(abs, -10))
print(apply_twice(lambda x: x * 2, 5))


# Task B: Sorting with Lambda

people = [
    ("Alice", 25),
    ("Bob", 20),
    ("Carol", 30),
    ("Dave", 22)
]

sorted_by_age = sorted(people, key=lambda person: person[1])

sorted_by_name = sorted(people, key=lambda person: person[0])

print("Sorted by age:", sorted_by_age)
print("Sorted by name:", sorted_by_name)


# Task C: Function Factory

def make_multiplier(k):
    # создаём функцию, которая умножает на k
    def multiply(x):
        return x * k
    return multiply

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10))
print(times5(10))


# Task D: Closure Counter

def counter():
    count = 0
    def add_one():
        nonlocal count
        count += 1
        return count
    return add_one

c = counter()
print(c())
print(c())
print(c())


# Task E: Lambda vs def

def square(x):
    return x * x

square2 = lambda x: x * x

print(square(5))
print(square2(5))


# Task F: Functional Composition

numbers = [1,2,3,4,5,6,7,8]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared = map(lambda x: x * x, even_numbers)
result = sum(squared)

print(result)
