# TODO Create Variables
#   - Create the following variables
my_first_name = "Ronin"
#       -set this equal to your first name
my_last_name = "Evans"
#       -set this equal to your last name
my_year_of_birth = 1998
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
current_year = 2024
#       -set this equal to 2020




# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name
print(my_first_name)  
#       - last name
print(my_last_name)
#       - first letter of your first name (use the +index)
print(my_first_name[0])
#       - second letter of your last name (use the -index)
print(my_last_name[-4])
#       - first two letter of your first name (use the +index)
print(my_first_name[0:2])
#       - second two letter of your last name (use the -index)
print(my_last_name[-4:-2])
#print(my_last_name[-4:-2]) press shift, alt, down arrow key to copy the above line to the next line




#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
print(my_first_name+my_last_name)
#       -first name six times
print(my_first_name*6)





# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
print(my_first_name + '' + my_last_name + 'was born in' + str(my_year_of_birth))
print(my_first_name,my_last_name,'was born in',str(my_year_of_birth))
print(f'{my_first_name}{my_last_name}was born in{my_year_of_birth}')
#print(my_first_name + '' + my_last_name + 'was born in' + my_year_of_birth) you can only concatonate strings, my bith year is an integer so this won't work
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
age = current_year - my_year_of_birth
print(my_first_name,my_last_name,'is',age,'years old')



# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year


# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case