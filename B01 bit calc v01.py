# Generates headings
def statement_generator(statement, decoration):
    print(f"\n {decoration * 5} {statement} {decoration * 5}")

# Display instructions
def instructions():
    statement_generator("instructions", "-")
    print('''
How to use this bit calculator ;)
\n
Image calculation:
 -type in img or image and then type dimensions of the image.
\nInteger (positive full number) calculation:
 -type in int or integer and then the number.
\nText calculation:
- Type in text that wouldn't be interpreted as the others, and then give the text you want to calculate bits of.
\n Closing program:
type "xxx"
    ''')


# ask user for file type (integer, text, image, xxx)
def get_filetype():

    while True:
        response = input("File type").lower()

        #check for i or exit code
        if response == "xxx" or response == "i":
            return response

        # check for integer
        elif response in ['integer','int']:
            return "integer"

        # check for image
        elif response in ['image','img','picture','p']:
            return "Image"

        #check for text
        elif response in ['text','txt','t']:
            return "text"


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



# calculate how many bits are needed to represent an integer
def image_calc():
    # get img dimensions
    width = int_check ( "Image width:",1 )
    height = int_check ("Image height: ",1)

    # calculate number of pixels and multiply them to get number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # set up and return answer
    answer = (f"Number of pixels: {width} X {height} = {num_pixels}"
              f"\nNumber of bits: {num_pixels} X 24 = {num_bits}")

    return answer

# calculate how many bits are needed to represent an integer
def integer_calc():
    # ask for integer
    integer = int_check ( "Integer:",0 )

    # convert integer to binary and work out how many bits are needed
    raw_binary = bin(integer)
    # remove the 0b
    binary = raw_binary[2:]
    num_bits = len(binary)
    # set up and return answer
    answer = f"{integer} in binary is {binary}. We need {num_bits} bits to represent it."

    return answer

# calculate number of bits needed to represent text in ascii

def calc_text_bits():

    # get text from user
    response = input("Enter some text: ")
    # calculate bits needed
    num_chars = len(response)
    num_bits = num_chars * 8
    # set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\n We need {num_chars} X 8 bits to represent it."
              f"\n Which is {num_bits} bits.")

    return answer


# main routine here

# display instructions
want_instructions = input("Press <Enter> to read instructions and any other key to continue")

if want_instructions == "":
    instructions()

while True:
    file_type=get_filetype()

    if file_type == "xxx":
        break

    # if user says "I" check if they want img or int
    if file_type=='i':

        want_image=input("please press <enter> for an integer or any key for an image")
        if want_image== "" :
            file_type= "integer"
        else:
            file_type= "image"

    if file_type == "Image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == 'integer':
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)
