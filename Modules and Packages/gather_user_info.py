def user_info():
    name = input("Enter your name: ")
    emailID = input("Enter your emailID ")
    with open("Data Entry Form.txt","a") as file:
        file.write(f"\n{name},{emailID}")
    print("Data is saved in the file successfully")