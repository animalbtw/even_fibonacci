num = int(input('Fibonacci sequence length is: '))
res_values = []


def fibonacci(value):
  if value <= 1:
    return value
  else:
    return fibonacci(value - 1) + fibonacci(value - 2)


if num <= 0:
  print('Positive number or > 0')
else:
  for values in range(num):
    res_values.append(fibonacci(values))


for res in res_values:
  if res % 2 == 0 and res > 0:
    print(res)
