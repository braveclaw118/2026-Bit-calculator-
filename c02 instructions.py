# Generates headings
def statement_generator(statement, decoration):
    print(f"\n {decoration * 5} {statement} {decoration * 5}")

# Display instructions
def instructions():
    statement_generator("instructions", "-")
    print('''
instructions here
-Instruction 1
-Instruction 2
-
you get it right?
    ''')

# main routine here

# display instructions
want_instructions = input("Press <Enter> to read instructions and any other key to continue")

if want_instructions == "":
    instructions()

print("program continues")