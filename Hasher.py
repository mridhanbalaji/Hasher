import random

#The length of the phrase to hash
n = 1000

def hashs(n):
    #Creates a list for all the variables to create the phrase
    hashlist = []
    #Creates a variable to store the phrase
    hash =[]
    
    #Variables to use in the hash
    numsArr = [1,2,3,4,5,6,7,8,9,0, 1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
    alpha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    syms = "!@#$%^&*()_+}:{<>?-=[];,.?!@#$%^&*()_+}:{<>?-=[];,.?"

    #Appends all the values in the variables into a list to create a random phrase
    for i in alpha:
        hashlist.append(i)
    for i in numsArr:
        hashlist.append(i)  
    for i in syms:
        hashlist.append(i)

    #Creates a random phrase, then length of the parameter
    a = 0
    while a < n:
        b = random.choice(hashlist)
        hash.append(b)
        a += 1

    #returns the phrase, as a phrase, not inside opf a list
    return  ''.join(map(str, hash))

#Calls the function to generate the phrase, and assigns it to a variable
a = hashs(10)

#PRints the phrase for me to see
print(a)

#Creates a function to creaete a hash of the phrase
def hashss():
    return hash(a)

#Calls the hash function
hashss()

#The usersinput recieved from the server, where they mine the crypto
userhash = input()

if userhash == hashss():
    
#        -----> NEED TO CREATE <--------
    #Transfer 1 of the cryptocurrency
    #generate a new block
    
    #Makee it harder to hash, by adding 20 sylybals everytime one block is claimed, by hasshing
    n += 20
    

   