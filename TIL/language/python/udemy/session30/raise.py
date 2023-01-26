try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("SOMETHING")
except KeyError as error_msg:
    print(f"the key {error_msg} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file closed")