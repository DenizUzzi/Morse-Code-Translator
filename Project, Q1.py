#the main part of the function is calling each function depending on the user input and uses them together.
def main():
    d = {}
    d = dictionary(d) #calls the letters and morse code that was put in a dictionary
    message = ' '
    #while loop affects what function is ran, depending on the choice of the operator
    while True:
        choice = menu() 
        if choice == 't':
            text = input("Please enter text to translate:\n")
            code = encode(text.upper(),d)
            print(code)
            print()
            
        
        elif choice == 'm':
            code = input("Please enter morse to translate:\n")
            text = decode(code,d)
            print(text)
            print()
            
            
        elif choice == 'e':
            print("Thanks for using this program!\n")
            break
#fucntion to split the file into two columns, and store them as a key,value pair in a dictionary
def dictionary(d):
    d = {} #created empty dictionary
    file = open("MorseCode.txt",'r')
    for line in file:
        key,value = line.split() #splits each line into two columns.
        d[key] = value 
    return d

#function to switch English to Morse Code
def encode(message,d): #takes message and dictionary as an argument to find each letter of the message in the dictionary and return it's morse code equivalent
    cipher = ""
    for letter in message:
        if letter != " ": #checks for space
            cipher = cipher + d[letter] + " " #space to separate each character in morse code so it isn't jumbled
        else:
            cipher = cipher + "   " #3 spaces to separate morse code words
    return cipher
#function to switch Morse Code to Enlgish
def decode(message,d): #takes message and dictionary as an argument to find each morse code of message in the dictionary and return it to it's English letter
    message += " " #added extra space to access the last morse code
    decipher = ""
    text = ""
    for letter in message:
        if letter !=" ": #checks for space
            count = 0
            text = text + letter #stores morse code of a single character
        else:
            count = count + 1
            if count >= 2: #indicates new word
                decipher = decipher +" " #space to separate words
            else:
                decipher += list(d.keys())[list(d.values()).index(text)] #accesses dictionary keys by using values
                text = ""
    return decipher
#function to print starting menu of program
def menu():
    print("Hello, this program allows you to translate text to morse code or translate morse code to text.\n")
    print()
    print("Please, select one of the below options: ")
    print()
    print("*** Enter 't' for encoding text\n")
    print("*** Enter 'm' for decoding morse code\n")
    print("*** Enter 'e' to exit the program\n")
    choice = input("My input is: ")
    while True:  #takes user input and gives back "invalid option" if they do not enter a valid choice
        if choice == 't' or choice == 'm' or choice == 'e': 
            return choice
        else:
            print("***invalid option")
            choice = input("Please enter a valid option: ")
main() #calls main function of program
    
