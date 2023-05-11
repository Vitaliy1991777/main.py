number = 73408
m = 0
s = 0
while number > 0:
    last_digit = number % 10
s = s + last_digit
if last_digit > m:
    m = last_digit
number = number // 10
print(s + m)