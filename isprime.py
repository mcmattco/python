# is num prime?

def is_prime(num):
	prime_nums = []
	half_of_num_int = int((num/2)+1)
	num_is_prime = True
	
	for i in range(2,half_of_num_int+1):  #define the nums between 2 and half of num to divide by
		if num % i == 0:
			num_is_prime = False
			break
	if num_is_prime == True:
		prime_nums.append(num)

is_prime(10)
