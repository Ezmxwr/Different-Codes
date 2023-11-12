from hashlib import md5
count=0
flag = 0
pass_hash = input ("Enter hash file name : ")
print(" ")

wordlist = "passlist.txt"

try:

    with open(pass_hash,"r") as pash:
    
         for hashpass in pash :
             hashpass = hashpass.strip()

             try:
                     with open(wordlist,"r") as pasfile:
                      for word in pasfile:
                          
                        enc_wrd = word.encode('utf-8')
                        digest = md5(enc_wrd.strip()).hexdigest()
                        count+=1
                        if digest.lower() ==hashpass.lower():
                            print("Password found")
                            print("Password is " + word)
                            print(count, " passwords have been checked until reach correct one ")
                            print(" ")
                            flag = 1
                            break
                     if flag ==0:
                        print("password/passphrase is not in the list" )
                    #reset for the next hashed passowrd
                     flag = 0
                     count= 0
                 
             except FileNotFoundError:
                 print("No file found:" , wordlist)
                 break

except:
    print("No file found named :", pass_hash_file)  

