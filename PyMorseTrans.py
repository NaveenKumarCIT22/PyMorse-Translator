import time
import winsound
frequency = 800 # Hertz
duration  = 200 # milliseconds


morsedat = [("A","._"),("B","_..."),("C","_._."),("D","_.."),("E","."),("F",".._."),("G","__."),("H","...."),("I",".."),("J",".___"),("K","_._"),("L","._.."),("M","__"),
            ("N","_."),("O","___"),("P",".__."),("Q","__._"),("R","._."),("S","..."),("T","_"),("U",".._"),("V","..._"),("W",".__"),("X","_.._"),("Y","_.__"),("Z","__.."),
            (1,".____"),(2,"..___"),(3,"...__"),(4,"...._"),(5,"......"),(6,"_...."),(7,"__..."),(8,"___.."),(9,"____."),(0,"_____"),(" "," "),(".","._._._"),(",","__..__"),
            ("'",".____."),(":","___..."),("?","..__.."),("-","_...._"),("/","_.._."),("\"","._.._."),(";","_._._."),("(","_.__."),(")","_.__._"),("\n","<para>")]

def ttom(text):
    out = ""
    for i in text:
        i = i.upper()
        if not i.isdigit():
            for j in morsedat:
                if j[0] == i:
                    out += "<"+j[1]+">"
        else:
            for j in morsedat:
                if j[0] == int(i):
                    out += "<n"+j[1]+">"
    return out

def mtot(mtxt):
    out = ""
    ch = ""
    c = ""
    for i in mtxt:
        if i == '<':
            ch = ""
        elif i == '>':
            for j in morsedat:
                if j[1] == c:
                    ch += str(j[0])
            out += ch
            c = ""
        elif i == 'n':
            # for j in morsedat:
            #     if j[1] == i:
            #         ch += str(j[0])
            # c += i
            pass
        else:
            c += i
            # for j in morsedat:
            #     if j[1] == i:
            #         ch += j[0]
    return out

modestr = "morse or text"
def shout(msg,mode:modestr):
    if mode == "morse":
        for i in msg:
            if i == ".":
                duration  = 200
                frequency = 1900
                winsound.Beep(frequency, duration)
            elif i == "<" or ">":
                time.sleep(0.25)
            elif i == "n":
                pass
            if i == "_":
                frequency = 1900 # Hertz
                duration  = 600
                winsound.Beep(frequency, duration)
            if i == " ":
                time.sleep(0.6)

def binarycov(code):
    out = ""
    for i in code:
        if i == ".":
            out += "10"
        if i == "_":
            out += "1110"
        if i == " ":
            out += "00"
        if i == "p":
            out += "000000"
        if i == ">":
            out += "|"
    return out

def binaryinv(code):
    out = "<"
    c = code
    for _ in range(len(code)):
        if c[:2] == "10":
            out += "."
            c=c[2:]
        if c[:4] == "1110":
            out += "_"
            c=c[4:]
        if c[:1] == "|":
            out += "><"
            c=c[1:]
            if out[-4:] == "><><":
                out = out[:-2]
                # out += "!!!"
        if c[:6] == "000000":
            out += "<para>"
            c=c[6:]
            # out = out[:-2]
        if c[:2] == "00":
            out += " "
            c=c[2:]

    out = out[:-1]
    return out


if __name__ == "__main__":
    # txt = "Sos help 911."
    # # mtxt = "<...><___><...>< ><....><.><._..><.__.>< ><n____.><n.____><n.____>"
    # with open("text.txt","r") as t:
    #     text = t.readlines()
    # txt = ""
    # for a in text:
    #     txt += a #+ '\n'
    # # txt.rstrip("\n")
    # print(txt)
    # mtxt = ttom(txt)
    # print(mtxt)
    # # print(mtot(mtxt))
    # # shout(mtxt,"morse")
    # bc = binarycov(mtxt)
    # print(bc)
    # mc = binaryinv(bc)
    # print(mc)
    print("\nDev:MNK ---> This version(1.5) is under development and is a stable release")
    while True:
        print()
        print("This is PyMorseTrans. Here you can convert msgs to morse text or morse sounds!\nEnter (i) if u want to convert to morse\
            (ii) if u want to convert from morse to text\n      (x) if u want to exit")
        inp = input("Enter your choice: ")
        if inp == "i":
            txt = input("Enter your message: ")
            out = ttom(txt)
            print("The morse conversion\n"+out)
            ask = input("Do you want its sound?(y/n) ")
            if ask.lower() == "y":
                shout(out,"morse")
        elif inp == "ii":
            mrs = input("Enter the morse msg: ")
            out = mtot(mrs)
            print("The morse decrypted msg\n"+out)
        elif inp == "x":
            break
