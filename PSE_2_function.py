# Create a function named score 
# that is responsible for scoring a given word.

# This function should :
# take in a string named word as a parameter. 
# return the word's total number of points.

def score(word):
    
    # letter_values holds the point values associated with each letter
    # the dictionary key is the num of points
    # the dictionary value is a list with each letter
    letter_values = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    
    #  total points will be the sum total of the word
    #  for the given word, each letter's points will be added to total_points
    #  use the letter_value dictionary to get the point for each letter
    total_points = 0
    
    # iterate through each element in the word
    for letter in word.upper():
        # print(letter)
        
        # loop through the dictionary keys and values
        for key, values in letter_values.items():
            # print(key)
            # print(values)
        
            # check if the letter is in the dictionary
            if letter in values:
                # print(letter)
                # print(values)
                
                # add the points for that letter to the total_points
                total_points += key
                # print(total_points)
    
    # final step is to return the total points for the word given
    # print(total_points)
    return total_points

score("DOG")
# output = 5

score("CAT")
# # output = 5

score("CABBAGE")
# # output = 14

score("QUARTZ")
# # output = 24

score("")
# # output = 0

score("Dog")
# # output = 5

score("DOG")
# # output = 5

score("dOG")
# # output = 5

score("dOG!@)")
# # output = 5