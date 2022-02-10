numbers = [25, 11, 7, 75, 56, 503, 493, 685.6];     
     
    
max = numbers[0];    
     
    
for i in range(0, len(numbers)):    
      
   if(numbers[i] > max):    
       max = numbers[i];    
           
print("Largest element present in given array: " + str(max));   