word=str(input("Enter a string"))  
count = 0;  
   
for i in range(0, len(word)):  
    if(word[i] != ' '):  
        count = count + 1;  

print("Total number of characters in a string: " + str(count));  
