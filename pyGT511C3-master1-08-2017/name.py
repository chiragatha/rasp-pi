import string
num2alpha = dict(zip(range(1, 27), string.ascii_lowercase))
name =[]
s=""
while True:
    alph=int(input("enter number: "))
    if (alph <=26 and alph >=1):
        name.append(num2alpha[alph])
        print (name)
    else:
        print ("Name is %s" %(s.join(name)))
        break
        
    
    
