# Q3: Prime Numbers Using for-else
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        # The else block associated with a for loop executes only when the loop completes its entire iteration normally, without hitting a 'break' statement.
        return True
    return False

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    primes = [str(i) for i in range(2, n + 1) if is_prime(i)]
    print(" ".join(primes))