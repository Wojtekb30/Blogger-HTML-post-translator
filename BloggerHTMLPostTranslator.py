from googletrans import Translator
import tkinter as tk
from tkinter import filedialog #import libraries, I used time for debug so it's unused in the release version
#import time
root = tk.Tk()
root.title("Blogger Translator")
root.withdraw() #run hidden Tkinter instance for file choose menu
print("Welcome to Blogger translator, created by Wojtekb30 on 18.12.2022, V0.1")
print("For now it only translates raw text written in HTML between <p> and </p>s")
lang = str(input("Type destination language code (for example pl, en): "))
print("Choose HTML or TXT file")
plik = open(filedialog.askopenfilename(filetypes=(('HTML file','*.html'),('Text file','*.txt'))))
tresc = str(plik.read())
plik.close()
translator = Translator() #set up translator
x=0
trybpracy = 0
tempwynik = ""
wynik = ""
print("Working.")
while True:
    print("Character "+str(x+1)+" out of "+str(len(tresc)) + " processed.")
    try:
        if str(tresc[x-2])+str(tresc[x-1])+str(tresc[x])=="<p>": #set work mode 1 if <p> detected.
            trybpracy = 1
            wynik = wynik + str(tresc[x])
            x=x+1
            
        if str(tresc[x-3])+str(tresc[x-2])+str(tresc[x-1])+str(tresc[x])=="</p>": #if </p> detected then translate, append to final result and return to work mode 0.
            #wynik = wynik + str(tresc[x])
            x=x+1
            print("Text found. Translating...")
            tempwynik = tempwynik[:-3]
            #print(tempwynik)
            tlumacz = translator.translate(tempwynik, dest=lang) #translate
            print(tlumacz.text)
            wynik = wynik+str(tlumacz.text)+"</p>"
            tempwynik = ""
            trybpracy = 0
            
        if trybpracy == 0: #if work mode 0 then just append next letters to the final result
            wynik = wynik + str(tresc[x])
            
        if trybpracy == 1: #if work mode 1 then append to variable which will be translated
            tempwynik = tempwynik + str(tresc[x])
            
        x=x+1
        #print(wynik)
        #print(tempwynik) #debug, keep commented
        #time.sleep(0.2)
    except:
        break #end loop if there are no more letters or something fails
print("Done, either finished or an error occured")
print("Let's save the result")

zapisfilename = filedialog.asksaveasfilename(filetypes=[("HTML file","*.html"), ("Text file","*.txt")], defaultextension = "*.html")
if zapisfilename: #save new translated file
    zapisanyplikk = open(zapisfilename, "w")
    zapisanyplikk.write(wynik)
    zapisanyplikk.close()

input("Press ENTER/RETURN to close")
