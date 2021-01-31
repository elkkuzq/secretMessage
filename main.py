from tkinter import messagebox, simpledialog, Tk

def getTask():
    task = simpledialog.askstring('Task', 'whether you want to encrypt or decrypt')
    return task

def getMessage():
    message = simpledialog.askstring('message', 'Write your message: ')
    return message

def isEven(number):
    return number % 2 == 0

def getEvenLetters():
    letters = []
    for counter in range(0, len(message)):
        if isEven(counter):
            letters.append(message[counter])
        return letters
def getOddLetters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not isEven(counter):
            odd_letter.append(message[counter])
        return odd_letters

def swapLetters(message):
    letterlist = []
    if not isEven(len(message)):
        message += 'x'
    even_letters = getEvenLetters(message)
    odd_letters = getOddLetters(message)
    
    for counter in range(0, int(len(message) / 2)):
        letterlist.append(odd_letters[counter])
        letterlist.append(even_letters[counter])
    new_message = ''.join(letterlist)
    return new_message

#pääohjelma
root = Tk()
root.withdraw()

while True:
    task = getTask()
    if task == 'encrypt':
        message = getMessage()
        encrypted = swapLetters(message)
        messagebox.showinfo('the message to be unpacked is', encrypted)
        
    elif task == 'decrypt':
        message = getMessage()
        decrypted = swapLetters(message)
        messagebox.showinfo('the message that is cracked is', decrypted)
    else:
        break
root.mainloop()

