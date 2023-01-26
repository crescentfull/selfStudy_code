# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("SOMETHING")
# except KeyError as error_msg:
#     print(f"the key {error_msg} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("this is an error that i made up")

height = float(input("height : "))
weight = int(input("Weight : "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)