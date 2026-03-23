#ask for width and loop until they enter a number that's more than 0

def int_check(question, low):

    error = "Please enter an integer that is more than 0\n"
    while True:
        try:
            response= int(input(question))

            if response >= low:
                return response
            else:(print(error))
        except ValueError:
            print (error)

# main routine goes here
for item in range (0, 2):
    width = int_check ( "Integer:",1 )
    print(width)

print ()

for item in range (0, 2):
    height = int_check ("height: ",1)
    print(height)