from random import randint

quote_file = "quotes.txt"

def get_random_quote():
    start_line  = None
    end_line    = None

    # Open the quote file
    with open(quote_file) as file:
        line = file.readlines()

    # Let's begin with some random line number
    # When '%%' is found, save the line number and break the loop
    for i in range(len(line)-1):
        random_line = (randint(0, len(line)-1))
        if "%%" in line[random_line]:
            start_line = random_line
            break

    # Find the closest next '%%' line number
    for i in range(start_line+1, len(line)):
        if "%%" in line[i]:
            end_line = i
            break

    # We don't need the '%%' to be printed
    start_line += 1

    # Join all the text between these two '%%'
    quote = "".join(line[start_line:end_line])

    return quote
