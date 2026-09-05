n = int(input("Enter number of elements: "))
elements_input = input("Enter elements: ").split()
elements = [int(x) for x in elements_input][:n]

largest = elements[0]
smallest = elements[0]
total_sum = 0
even_count = 0
odd_count = 0
reversed_list = []

for val in elements:
    if val > largest:
        largest = val
    if val < smallest:
        smallest = val
    total_sum += val
    if val % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    reversed_list = [val] + reversed_list

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Sum: {total_sum}")
print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")
print("Reversed:", " ".join(map(str, reversed_list)))