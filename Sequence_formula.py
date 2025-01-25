"""
Name: Mahmud
Program: Name/ Version: sequence/version 1 
Description: The program analyzes the given numbers to determine if it’s an linear or quadratic sequence.
      Once the sequence type is identified, the program can find the nth term of the sequence you want. 
      It also generates the mathematical formula that describes the entire sequence, allowing you to calculate
      any term you want, like the 10th or 100th term, with ease."
      n = term in sequence
Date: 11/4/24
"""

# Needed variables
input_check = 4
iteration = 0
sequence = [] # stores the user input
p_s1,p_s2,p_s3,p_s4 = [1,4,9,16] # perfect square
sequence_type = "This isnt a linear or quadratic sequence"
sequence_formula = "Sequence None"


# user interface
print("The program analyzes the given numbers to determine if it’s a linear or quadratic sequence"
      " Once the sequence type is identified, the program can find the nth term of the sequence you want. "
      "It also generates the mathematical formula that describes the entire sequence, allowing you to calculate"
      " any term you want, like the 10th or 100th term, with ease."
      " n = term in sequence\n")

# makes sure the users input is a int or float
while (iteration < input_check):
    place = "First"
    if iteration + 1 == 2:
        place = "Secound"
    elif iteration + 1 == 3:
        place = "Third"
    elif iteration + 1 == 4:
        place = "Fourth"
    try:
        sequence_input = float(input(f"Write the {place} number in the sequence? "))
        sequence.append(sequence_input)
        iteration += 1
    except:
        print("\nThat is not a number try again\n")

while True:
    try:
        decimal_check = int(input("\nif theres a decimal in any of the number, what place is the longest one an example is: "
            "0.1 which u would type 1 for\n and 0.01 which u would type 2 for. if theres none type zero 0. "))
        break
    except:
        print("\nInvalid input. Please enter a whole number.")
             

print(f"\n{sequence}")

first_num = sequence[0]
secound_num = sequence[1]
third_num = sequence[2]
fourth_num = sequence[3]

    
def linear_check():
    global sequence_type
    global sequence_formula
    global linear_diff1
    global linear_diff2
    global linear_diff3
    global term_diff
    
    linear_diff1 = round(sequence[1] - sequence[0],decimal_check)
    linear_diff2 = round(sequence[2] - sequence[1],decimal_check)
    linear_diff3 = round(sequence[3] - sequence[2],decimal_check)
    
    if first_num == linear_diff1:
        term_diff = 0
    else:
        term_diff = round(first_num - linear_diff1,decimal_check)
    
    if linear_diff1 == linear_diff2 and linear_diff2 == linear_diff3:
        sequence_type = "Sequence type: linear sequence"
        if term_diff == 0:  
            sequence_formula = f"Sequence formula: {linear_diff1}n"
        elif term_diff > 0:
            sequence_formula = f"Sequence formula: {linear_diff1}n + {term_diff}"
        elif term_diff < 0:
            sequence_formula = f"Sequence formula: {linear_diff1}n - {abs(term_diff)}"
    else:
        pass

def quadratic_check():
    global sequence_type
    global sequence_formula
    
    first_diff1 = round(sequence[1] - sequence[0],decimal_check)
    first_diff2 = round(sequence[2] - sequence[1],decimal_check)
    first_diff3 = round(sequence[3] - sequence[2],decimal_check)
    
    secound_diff1 = round(first_diff2 - first_diff1,decimal_check)
    secound_diff2 = round(first_diff3 - first_diff2,decimal_check)
    
    if (sequence_type == "This isnt a linear or quadratic sequence" and sequence_formula == "Sequence None"):
        
        pass
    

linear_check()
quadratic_check()
print(sequence_type)
print(sequence_formula)


# allows user to find the nth term of what ever they want
while sequence_type != "This isnt a linear or quadratic sequence":
    try:
        find_n = int(input("\nwhich term in the sequence would you like to know? "))
        break
    except:
        print("Invalid input. Please enter a whole number.")

# caculates what the term in the sequence the user wants to know if it a sequence
if sequence_type == "Sequence type: linear sequence":
    n_term = (linear_diff1 * find_n) + term_diff
    print(f"The {find_n}th term is {n_term}")  
else:
    print("\nUnable to calculate the nth term as the sequence type is not recognized.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


