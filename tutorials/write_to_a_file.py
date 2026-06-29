with open("example.txt", "w+") as file:
    file.write("Hello, this is my first line of text!\n")
    
    file.write("This line is appended to the bottom.\n")
    file.write("Another appended line.\n")

    # Move cursor back to start before reading
    file.seek(0)

    content = file.read()

print(content)