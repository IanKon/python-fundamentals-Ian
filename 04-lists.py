# lists
fruits = ["apple", "banana", "cherry"]

## indexing
print(fruits[0])
print(fruits[-1])

## slice
print(fruits[0:2])
print(fruits[1:])

## length
print(len(fruits))

## append / insert / remove / pop
fruits.append("orange")
fruits.insert(1, "kiwi")
fruits.remove("banana")
last = fruits.pop()
print(fruits, last)

## sort()
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

## tuples / sets
point = (10, 20)
print(point[0])

unique = {1, 2, 2, 3, 3}
print(unique)