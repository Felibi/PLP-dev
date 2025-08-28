def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
print('enter base and exponent:')
print(large_power(int(input()), int(input())))

'''
# Example usage
print(large_power(2, 13))
print(large_power(3, 8))
print(large_power(5, 5))
'''
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
print('enter a number:')
print(divisible_by_ten(int(input())))