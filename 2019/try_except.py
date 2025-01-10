# # Try Except Examples
# # for user input of numerical data
# try:
#     # potential for user to enter "four" which will not
#     # convert to an integer 
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Sorry you must enter a numerical data type.")
    
    
    
# # Better version
# while True:
#     try:
#         num = float(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Sorry you must enter a numerical data type. Try again.")
#         continue # make them start the loop again
    


file = input("Enter the path to the file to be analyzed: ")

try:
    file_handle = open(file, 'r')
except FileNotFoundError:
    print("Sorry that file does not exist.")
    quit()  # quit running python
text = file_handle.read()
lines = text.split('\n')
print("There are " + str(len(lines))+ " lines of text in the "
      + file + " file")

