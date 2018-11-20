#rock paper scissor game
c1=0
c2=0
def newgame():
    v=input("enter y to start new game: ").lower()
    if v=='y':
            game()
    else:
        if c1>c2:
          print("p1 is final winner")
        elif c2>c1:
          print("p2 final wins")
        else:
            print("tied")
            #exit()
def game():
    n=1
    if n==1:
        c1=0
        c2=0
        n+=1
    p1=input("enter for p1 1.rock 2.paper 3.scissor? ").lower()
    p2=input("entr for p2 rock paper scissor? ").lower()
    a=['rock','paper','scissor']
    if p1==a[0] and p2==a[2]:
        print("p1 wins")
        c1+=1
        newgame()
    elif p2==a[0] and p1==a[2]:
        print("p2 wins")
        c2+=1
        newgame()
    elif p1==a[1] and p2==a[0]:
        print("p1 wins")
        c1+=1
        newgame()
    elif p1==a[0] and p2==a[1]:
        print("p2 wins")
        c2+=1
        newgame()
    elif p1==a[1] and p2==a[0]:
        print("p1 wins")
        c1+=1
        newgame()
    elif p1==a[2] and p2==a[1]:
        print("p1 wins")
        c1+=1
        newgame()
    elif p1==a[1] and p2==a[2]:
        print("p2 wins")
        c2+=1
        newgame()
    else:
        print("nothing")
    

game()

