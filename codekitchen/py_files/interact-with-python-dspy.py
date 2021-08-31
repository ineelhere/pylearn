#asking user for a text (name)
username = input('Please enter your name - ')

#lets greet the user now
print ('Hello ' +username)

#ask the user's birth year
year = input('Please enter your Birth Year - ')

#calculating the age, here we have to change the type for year from string to integer
age = 2021- int(year)

#now we will print the results
print(f'Hey {username}, You are {age} years old :) ')

#using "f" before writing the print statement saves us a lot of time and effort
#just need to keep in mind that we are keeping the variables in {}
