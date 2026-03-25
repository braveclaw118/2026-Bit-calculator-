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

# main routine goes here]
image_ans = image_calc()
print(image_ans)