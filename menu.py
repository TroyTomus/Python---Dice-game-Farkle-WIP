#intro
def intro ():
    print ("hello, welcome to farkle")
    #menu().wait(50)
    menu()

#menu/ exit, history, play 1 v1, play ai


#............

def menu():
    print ("\nMenu loaded")
    print("""
1. History
2. Multiplayer
3. Exit
""")
    i=1
    while i==1 :
        x=input("type a number")
        if x == "1":
            print ("\nLoading History...")
            history()
        elif x == "2":
            print ("\nLoading Multiplayer...")
        elif x =="3":
            print("Exit")
        else:
            print("Invalid selection")

# ==============

def history ():
    print ("""
History of Farkle:
Sir Albert Farkle of Iceland is often credited
as the originator of the game in the 14th century
but variations most likely existed before then.

credit: http://farkle.games/farkle-history/
""")

    input("press 'Enter' to go back")
    menu()

# ==============

intro()
