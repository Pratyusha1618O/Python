## Passing immutable object

#defining the function   
def change_list(list):   
    list.append(20)   
    list.append(30)  
    print("list inside function = ",list) 

#defining the list   
list1 = [10,30,40,50]  

#calling the function    
change_list(list1);   
print("list outside function = ",list1); 