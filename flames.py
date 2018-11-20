# MY OWN CODE FOR FLAMES GAME
# Visit  https://flames.games for playing game
s1=input("enter name1")
s2=input("enter name2")
for i in s1:
    for j in s2:
         if i==j:
            s1=s1.replace(i,'',1)
            print(s1)
            s2=s2.replace(j,'',1) # only once cancel
            print(s2)
            break   # once its cancelled the other same letter should be left so break
    
print(s1)
print(s2)
count=len(s1)+len(s2)
print(count)
l=['F','L','A','M','E','S']
if count==1:
        print(l[len(l)-1])
    
if count>2:
        while len(l)!=1:  #until 1 letter is left in flames
            while count>len(l):   #reducing count to range of FLAms 6 if its len-1 then del l[count]
             count=count-len(l)   #to avoid indexoutofrange error
            del l[count-1]
            #print(count-1,l)
            l=l[count-1:]+l[0:count-1] #aftr cutting strting count frm next element
            print(l,len(l))  
            count=len(s1)+len(s2) #eg;11-6,11-5 6-5,11-4 7-4----
if l==['F']:
    print("friends".upper())
elif l==['L']:
    print("Love".upper())
elif l==['A']:
    print("something attraction".upper())
elif l==['M']:
    print("marriage".upper())
elif l==['E']:
    print("enemy".upper())
elif l==['S']:
    print("siblings".upper())
        
        
    
