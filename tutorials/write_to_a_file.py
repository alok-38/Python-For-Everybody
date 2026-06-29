# Open the file in write mode ('w')
with open("example.txt", "w") as file:
    file.write("Hello, this is my first line of text!\n")
    # Append
    file.write("This line is appended to the bottom.\n")
    
    try:
        with open("example.txt", "x") as file:
            file.write("This only works if the file is brand new")
    except FileExistsError:
        print("Error: The file already exists!")