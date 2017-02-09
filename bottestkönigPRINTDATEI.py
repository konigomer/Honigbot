import sys



#Dialog = True
print("Wer wagt es mich zu stören?")
#2Name is not = "ich", "ich bin", "Ich" or "Ich bin"
Name = input()

if "ich" in Name or "ich bin" in Name or "Ich" in Name or "Ich bin" in Name or Name == "":
        print("Nur deinen Namen und nichts mehr!!")

        Name = input()
    
#if not Name == "Ich" or "ich": print("was führt dich hierher"), print(Name)

if "ich" in Name or "ich bin" in Name or "Ich" in Name or "Ich bin" in Name or Name == "":
        print("weil du so frech bist, wirst du sterben!!"),
        print("du bist auf tragische weise gestorben"),
        sys.exit()


print("Was führt dich hierher", Name,"?")

input() 

print("Was belästigst du mich damit",Name,"? Verschwinde!")

input() 

print("Ich werde dich töten lassen",Name,"!!")

B = input()
if "" == B:
        print("Ich werde dich töten lassen",Name,"!!")
        C = input()
        if "" == C:
                print("Du bist Tod")
                sys.exit()

print("Bist du ein Narr oder sehnst du dich nach dem Tod?")


    

A = input()

if "Narr" in A or "narr" in A:
        print("Los Verschwinde und ich drück ein Auge zu!"),
        sys.exit()
           #

if not "mutig" in A or not "Mutig" in A or "" in A or not "mut" in A or not "Mut" in A or "nein" in A or "Nein" in A or "Ja" in A or "ja" in A:
        print("Du bist also nicht mutig?")
        E = input()
        if not "mut" in E.lower(): #Fehler!!!!
                print("Du wurdest vom König getötet"),
                sys.exit()

elif "" == A:
        print("Antworte! Bist du mutig oder dumm?")
        D = input()
        if "" == D:
                print("Du bist Tod")
                sys.exit()
                
#funktioniert bis hier
        
        

if "ich bin mutig" in E or "mut" in E or "Mut" in E  : print("Trete vor", Name)
F = input()

print("So sei es.",Name,"ich werde dir vielleicht ein Wunsch erfüllen.")
    
input()
print("Nein das ist nicht möglich.",Name)

input()
print("Du wirst sterben!")
print("*Bleibst du oder rennst du weg?*")

G=input()
print("du wurdest von den Wachen Erschlagen")
        
#E.lower()


#lesezeichen erstellen
###print durch return ersetzen
