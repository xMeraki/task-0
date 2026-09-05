# Q2: Lists, Functions and .copy()
def process_list(numbers):
    result_list = numbers.copy()
    
    # Remove negative numbers safely using .remove()
    for item in numbers:
        if item < 0:
            result_list.remove(item)
            
    result_list.append(0)
    result_list.sort()
    return result_list

if __name__ == "__main__":
    original = [5, -2, 8, -1, 3]
    result = process_list(original)
    print("Original:", original)
    print("Result:", result)