import random
n=int(input("nter 1.strong 2.weak 3.moderate passords "))
if n==1:
    l=int(input("enter pasord len between 6 to 10 "))
    list1=[]
    while len(list1)<=l:
        list1.append(random.randint(65,90))
        list1.append(random.randint(97,122))
        list1.append(64)
        list1.append(random.randint(48,57))
        list1.append(random.randint(33,47))
    print(list1)
    while len(list1)>l:
        del list1[random.randrange(0,len(list1))]
    print(list1)
    print("captcha is",end=" ")
    for i in list1:
                  
                  print(chr(i),end='')
if n==2:
    l=int(input("enter pasord len between 4 to 6"))
    list1=[]
    while len(list1)<=l:
        
        list1.append(random.randint(97,122))
    print("password is",end=" ")
    for i in list1:
                  
                  print(chr(i),end='')
    
