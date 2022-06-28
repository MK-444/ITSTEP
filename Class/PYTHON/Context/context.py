import time
#context management

f = open("output.txt", "w")

try:
    text = f.write("Ahoj")
    
except ZeroDivisionError:
    print("Chyba!!!")
    
finally:
    print("Tohle se stane vzdycky, at uz je chyba nebo ne")
    f.close()


