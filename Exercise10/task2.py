# # Task 2 (simple)
# attempts = 0
#
# while True:
#     BankPin = input("Enter Your Password: ")
#
#     if BankPin == "Password":
#         print("Thank you, what services would you like?")
#         break
#     else:
#         attempts += 1
#         print("Incorrect Pin. Please try again.")
#         if attempts == 3:
#             print("Locked out")
#         break

## Task 2 (Extended)
import time

attempts = 0
locked_out = False
locked_out_time = 0

while True:
    if locked_out:
        current_time = time.time()
        time_since_lockout = current_time - locked_out_time
        if time_since_lockout >= 10:
            print("Password unlock timer has expired. Please try again.")
            locked_out = False
        else:
            print(f"Sorry, you have been locked out. Please wait {10 - int(time_since_lockout)} seconds.")

    BankPin = input("Enter Your Password: ")

    if BankPin == "Password":
        print("Thank you, what services would you like?")
        break

    attempts += 1
    print("Incorrect Pin. Please try again.")
    if attempts == 3:
        locked_out = True
        locked_out_time = time.time()