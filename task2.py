# this script will create a list with elements of different types and count the number of string elements in it

task2 = [1,2.0,"sasha",False,(1,2,3),[1,2,3,4,5],"hola",{"key":"value"},"ciao"]

counter=0

for i in task2:
    if type(i) == str:
        counter += 1
        print(i)
        
# output the result
print()
print(f'The number of string elements in list "task2" is {counter} :)')
print()
