def sum_of_digits(number):
    total = 0
    num_str = str(number)
    for digit in num_str:
     total += int(digit)
    return total
prompt="Enter a number: "
num=int(input(prompt))
result= sum_of_digits(num)
print("The sum of digits of",num,"is",result)
