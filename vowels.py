vowels=['a','e','i','o','u']
consonants=['b','c','d','f','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
ch=input("enter a alphate")
a=ch.lower()
if a in vowels:
    print('vowel')
elif(a in consonants):
    print('consonants')
else :
    print('invalid')
    
            
        
