command_list = ["plain", "bold", "italic", "inline-code", "link",
                "header", "unordered-list", "ordered-list", "new-line"]

def plain():
    return input("- Text: ")

def bold():
    return "**" + input("- Text: ") + "**"

def italic():
    return "*" + input("- Text: ") + "*"

def inline_code():
    return "`" + input("- Text: ") + "`"

def link():
    return "[" + input("- Label: ") + "]" + "(" + input("- URL: ") + ")"

def header():
    while True:
        level = int(input("- Level: "))
        if level in range(1, 7):
            break
        else:
            print("The level should be within the range of 1 to 6")
    return "#" * level + " " + input("- Text: ") + "\n"

def new_line():
    return "\n"

text_ = ""
while True:
    command = input("- Choose a formatter: ")
    if command == "!done":
        break
    elif command == "!help":
        print("Available formatters: " + " ".join(command_list))
        print("Special commands: !help !done")
    elif command not in command_list:
        print("Unknown formatting type or command. Please try again.")
        continue
    elif command == "header":
        text_ += header()
    elif command == "plain":
        text_ += plain()
    elif command == "bold":
        text_ += bold()
    elif command == "italic":
        text_ += italic()
    elif command == "inline-code":
        text_ += inline_code()
    elif command == "link":
        text_ += link()
    elif command == "new-line":
        text_ += new_line()
    print(text_)
