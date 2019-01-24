#FizzBuzz, multiples of 3 are Fizz and multiples of 5 are Buzz
#multiples of both are FizzBuzz and multiples or neither are just the number
for i in range(0, 101):
	if i % 3 == 0 and i % 5 != 0:
		print("Fizz")
	elif i % 3 != 0 and i % 5 == 0:
		print("Buzz")
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	if i % 3 != 0 and i % 5 != 0:
		print(i)