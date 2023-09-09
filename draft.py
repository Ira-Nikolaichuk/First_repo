#num_1 = 90
#num_2 = 87
#example = f"Simple example {num_1} + {num_2} = {num_1 + num_2}"
#print(example)

#name = input("Enter your name: ")
#last_name = input("Enter your last name: ")
#full_name = f"{name} {last_name}"
#print(full_name)

# num_1 = str(1)
# num_2 = int(float(str(1.8)))
# string_1 = int('3')
#print(type(num_1), type(num_2), type(string_1))

volume = float(input("Fuel volume: "))
price = float(input("Fuel price: "))
bill = f'Your bill {volume * price} UAH'
print(bill)
print(type(volume), type(price))