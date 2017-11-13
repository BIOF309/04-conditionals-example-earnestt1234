
# coding: utf-8

# In[24]:

print('Enter a integer between 1 and 10,000,000 and I will tell you if it is prime.') 

#Invitation to user.  This program should wwork for all positive integers; the limit is based on computational power.

x=float(input()) 

#User input, converts input to float.  If input is a string of letters (i.e. 'ten'), this will cause
#a Python error.  I couldn't figure a way to cease the program if a word was entered - the input func. 
#interprets all entries as strings, regardless of if they are numbers or words.

if x > 10000000 or x < 1: 
    print("\nYour number is out of range; enter a number between 1 and 10,000,000.")
    
#This checkpoint verifies that the number is in range.
    
elif x/(round(x,0)) !=1:
    print("\nYour number is not an integer.")
    
#This checkpoint deals with entries that are not integers (if the entry rounds to an integer (that isn't itself), it is not an
#integer), and prints an error.  Note that this bit cannot handle numbers between 0 and 0.5, as there will be a division
#by 0 error.  This made me decide to keep the lower limit of the program at 1, rather than 0.  I would like to fix this, 
#as it would be helpful to include the case of 0.

else:
    
#The meat of the program; actually checking prime status.  Everything is nested in this "else", so that the prime status is only
#checked when the above conditions are met.

    print("\nCalculating...")
    
    #helpful to have this for some of the larger entries.
    
    if x == 1:
        print("\n1 is not prime.")
        
    #Special case that doesn't work well with the while loop below.
    
    elif x == 2:
        print("\n2 is prime!")
    
    #Another special case.
        
    else:
        c=2
        
        #starts a counter c, which will be the tool used to check divisors of the entry
        
        while c<= (x/2):
            
        #We only need to check divisors up to half the size of the entry; any number larger than x/2 
        #will not divide x with no remainder
        
            if x % c == 0:
                print("\n" + str(int(x)) + " is not prime.")
                break
                
            #Takes advantage of python's built in modulus operation.  If there is a remainderr of 0, the program ends
            #and reports that the entry isn't prime.
                
            elif x % c != 0:
                c = c + 1
                
            #If the divisor c left a remainder, then it increases the value of c and repeats (until c has reached x/2)
                
        if c > (x/2):
                print("\n" + str(int(x)) + " is prime!" )
                
            #This code only runs when c has reached a value great than x/2; the while loop has ceased and this code reports
            #that the number is prime (since all possible divisors up to x/2 have been tried).


# In[ ]:



