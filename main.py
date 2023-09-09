# print("Hello world!")

# print("Hello Git!")

# важливо думати над логікою виходу із циклу
# counter = 0     # цикл while + лічильник
# while counter < 5: # або while True:
#     user_input = input(">>> ")
#     counter += 1 # counter = counter + 1
#     if user_input == "exit" or counter >= 5:
#         break
#     else:
#         print(f'You write {user_input}')

while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 18:
            print("access allowed")
            break
        else:
            print("Access denied")
            break
    except ValueError:
        print(f'{age} is not a number. Please write a number!')
    finally:
        print("-"*30)