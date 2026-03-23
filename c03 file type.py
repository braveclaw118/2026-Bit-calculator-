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








# main routine here
while True:
    file_type=get_filetype()


    # if user says "I" check if they want img or int
    if file_type=='i':

        want_image=input("please press <enter> for an integer or any key for an image")
        if want_image== "" :
            file_type= "integer"
        else:
            file_type= "image"

    print(f"You chose {file_type}")

    if file_type =="xxx":
        break