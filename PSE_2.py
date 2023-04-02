# Problem Statement
# Imagine programming the logic for a word game

# every player submits one word. 
# each word gets a score,
# the score is based on the letters in the word and its point value.

letter_values = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

# Create a function named score 
# that is responsible for scoring a given word.

# This function should :
# take in a string named word as a parameter. 
# return the word's total number of points.

def score(word):
    #  total points will be the sum total of the word
    #  for the given word, each letter's points  will be added together
    #  the sum will add the points for each letter in the word
    total_points = 0
    # need a way to separate each letter as an individual string value
    # then add the point value of that letter to the total points
    pass
    return total_points

# Test: Input/ Output 
score("DOG")
# 5

score("CAT")
# 5

score("CABBAGE")
# 14

score("QUARTZ")
# 24

# =================================== 1. Clarifying Questions ===================================
# List three or more questions whose answers would clarify the problem statement.

# For each question, provide an answer which includes 
# the effect your decision would have on how you would approach the problem.

# 1. How to handle invalid input- empty string? 
# return 0

# 2. How to handle invalid input- not a valid letter? 
# isalpha() can check if all characters are letters
# if False, return 0

# 3. How to handle a string that is lowercase or mixed case? 
# use .upper() to convert the entire word string to uppercase

# 4. What if user enters two words in one string? 
# split() will split a string into a list, where each word is a list item

# 5. How to handle extra spaces in a string? 
# strip() will remove space before or after 
# if the user accidently adds a space before or after the word

# replace() will remove all spaces including from between words.

# other ways to remove: 
# https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string

# 6. If user entrers valid input, how do we return the correct score?
# How to associate each letter in the word with a point value?
# use helper functions to isolate each letter in the word: 
    # 1. using list comprehension 
        # Input:
        # word="Geeks"
        # x=[i for i in word] 
        # print(x)
        # Output: 
        # ['G', 'e', 'e', 'k', 's']

    # 2.  using string slicing

    # def Convert(word):
    #     list_of_letters = []
    #     list_of_letters[:0] = word
    #     return list_of_letters

    # # Driver code
    # word = "ABCD"
    # print(Convert(word))

    # 3. Using map()
    # word="Geeks"
    # x=list(map(str,word))
    # print(x)

    # 4. Using list
    # word = "Geeks"
    # x = list(word)
    # print(x)
    
# How should the function handle special characters? ------ think .isalpha() covered this


# =================================== 2. Unit Tests ===================================

# Use the comments provided to write at least two example input/outputs:
    # 1. Consider at least one nominal and one edge case.
        # What is the expected output for the given input?
        # You can use the examples provided in the prompt, or other examples.
        
    # 2. Write unit tests for score for the nominal and edge cases 
    #    you identified in the first step:
    #        1. valid input returns correct score
    #        2. invalid input- empty string - returns 0
    #        3. invalid input- not a valid letter/ special character returns 0 or error msg
    #        4. valid word contains lowercase returns correct points
    #        5. valid word string contains spaces returns score
    
# =================================== 2. Unit Tests- NOMINAL


def test_valid_input_returns_correct_score(word):
    pass

    # arrange
    word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # act
    result = score(word)

    # assert
    assert result == 87
    
# example input 1:
test_valid_input_returns_correct_score("DOG")
# expected output: 5

# example input 2:
test_valid_input_returns_correct_score("CAT")
# expected output: 5

# example input 3:
test_valid_input_returns_correct_score("CABBAGE")
# expected output: 14

# example input 4:
test_valid_input_returns_correct_score("QUARTZ")
# expected output: 24



def test_word_contains_lowercase_returns_score(word):
    # arrange
    word = 'AbCdEfGhIjKlMnOpQrStUvWxYz'

    # act
    result = score(word)


    # assert
    assert result == 87

def test_word_contains_lowercase_returns_capitalized(word):
    # example input 1:

    # arrange
    word = "dOg"
    
    # act
    result = word.upper()
    
    # assert
    assert result == ["DOG"]
    

# example input 2:
test_word_contains_lowercase_returns_capitalized("CaT")
# expected output: ["CAT"]

# example input 3:
test_word_contains_lowercase_returns_capitalized("CaBbAgE")
# expected output: ["CABBAGE"]

# example input 4:
test_word_contains_lowercase_returns_capitalized("QuArTz")
# expected output: ["QUARTZ"]



# =================================== 2. Unit Tests- EDGE
def test_invalid_input_empty_str_returns_0(word):
    pass

    # arrange
    word = ""

    # act
    result = score(word)


    # assert
    assert result == 0




def test_not_letter_char_returns_error_msg(word):
    pass
    
    # arrange
    
    # act
    result = score(word)

    
    # assert
    
# example input 1:
test_not_letter_char_returns_error_msg("D0G")
# expected output: "Please enter words with only letters A-Z"

# example input 2:
test_not_letter_char_returns_error_msg("C@T")
# expected output: "Please enter words with only letters A-Z"



def test_valid_word_contains_spaces_removes_spaces(word):
    pass

    # arrange
    
    # act
    result = score(word)

    
    # assert

# example input 1:
test_valid_word_contains_spaces_removes_spaces(" DOG")
# expected output: ["DOG"]

# example input 2:
test_valid_word_contains_spaces_removes_spaces("CAT ")
# expected output: ["CAT"]

# example input 3:
test_valid_word_contains_spaces_removes_spaces("C A B B A G E")
# expected output: ["CABBAGE"]

# example input 4:
test_valid_word_contains_spaces_removes_spaces(" Q U A R T Z ")
# expected output: ["QUARTZ"]



# =================================== 2. Unit Tests- Examples from LEARN:

# example input 1: word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# expected output 1: score(word) = 87

# example input 2: word = 'dOg'
# expected output 2: score(word) = 5

# example input 3: word = 'dOg!@)'
# expected output 3: score(word) = 5

# def test_correct_score_for_all_letters():
#     # nominal test case

#     # Arrange
#     word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#     # Act
#     result = score(word)

#     # Assert
#     assert result == 87



# def test_case_insensitive():
#     # nominal test case

#     # Arrange
#     word = 'dOg'

#     # Act
#     result = score(word)

#     # Assert
#     assert result == 5



# def test_ignores_special_characters():
#     # edge test case
    
#     # Arrange
#     word = 'dOg!@)'

#     # Act
#     result = score(word)

#     # Assert
#     assert result == 5


# =================================== 3. Create  Logical Steps ===================================
# Without writing code, 
# describe how you would implement score 
# in enough detail that someone else could write the code.

# It may be helpful to break up the problem/algorithm 
# into smaller subproblems/algorithms. 
    # For example: 
    # 1. Handle invalid input
    # 2. Given valid input, perform the computation/solve the problem/etc.
# Your logical steps could take the form of 
# a numbered list, pseudo code, or anywhere in between.

# What's important at this stage is to think through 
# and outline the implementation before writing code.

# =================================== 3. My thought process:

# 1. define the function to take in one parameter, word which is a string
# 2. set a variable for the letter values
# - letter values should be a dictionary 
# - the dictionary key is the integer point value  associated with the letters
# - the dictionary value will be a list containing each letter associated with that integer
# 3. set a variable to hold the total points
# 4. capitalize every letter using .upper
# 5. loop through each letter in the word
# 6. if that letter is a value in any of the the letter_value[i] lists, 
# 7. add the key for that letter to the total_points
# 8. return the total points

# =================================== 3. Example from LEARN:

# Create a dictionary letter_vals with key-value pairs that are letter and corresponding value.

# Initialize the result to 0

# Loop through the characters in the word

# Check if the character is in the letter_vals dictionary

# If it is, add the value of the letter to the result

# Return the result