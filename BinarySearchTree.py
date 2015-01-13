## Navleen Singh (1302228)
## 1XA3 Final Project 
## BinarySearchTree.py


class Binary_Search_Tree():
    
    def __init__(self):

## Defines all the self varabiles that are used in all the procedures
        self.T = []
        self.L=[]
        self.tempT=[]
        self.x=False

##  Run all the procedures       
        self.getvalue(self.T)
        self.getTree()             
        self.minimumTree(self.T)
        self.maximumTree(self.T)
        self.increasing_orderTree(self.T)
        print("Increasing order is:",self.L)
        self.L=[]
        self.decreasing_orderTree(self.T)
        print("Decreasing order is:",self.L)
        
        value=eval(input("Enter a number to be searched: "))
        self.searchTree(self.T,value)
        
        delete=eval(input("Enter a number to be deleted: "))
        self.deleteTree(self.T,delete)


## Out puts Tree that the user created 
    def getTree(self):
        print("Your Tree is:",self.T)
        
## This function searches if the value entered is in the binary tree
    def searchTree(self,T,value):

## Checks if T has nothing in it
        if T==[]:
            print("Can't fint",value)
            
## Checks the first value of T
        elif T[0]==value:
            print("Found",value)
            
## If value is less then T's element then it goes to the left of the tree        
        elif T[0]>value:
            self.searchTree(T[1],value)
            
## If value is greater then T's element then it goes to the right of the tree       
        elif T[0]<value:
            self.searchTree(T[2],value)

## Find the nuber and delete it
    def deletesearch(self,T,value):
       
        if T==[]:
            pass
        
        elif T[0]==value:
            self.x=True
            
## Bass case for the deltetion 
            if T[1] == [] and T[2] == []:
                T[:] = []
                
## Second case
            elif T[2] != [] and T[1] == []:
                T[:] = T[2]

## Third case
            elif T[1] != [] and T[2] == []:
                T[:] = T[1]
                
## Fourth case     
            else:
                if T[2][1] !=[]:
                    T[0] = T[2][1][0]
                    T[1][2][:] = T[2][1][1]
                    T[2][1][:] = T[2][1][2]
                else:
                    if T[2] != []:
                        T[0] = T[2][0]
                        T[2][:] = T[2][2]

## Searches for the number                        
        elif T[0]>value:
            self.deletesearch(T[1],value)
            if self.x == False:
                self.deletesearch(T[2],value)  
        elif T[0]<value:
            self.deletesearch(T[2],value)
            if self.x == False:
                self.deletesearch(T[1],value)

## Runs the deletesearch here and if it cant be found then nothing will come
    def deleteTree(self,T,value):
        self.deletesearch(T,value)
        if self.x==False:
            print("\nNothing\n")
        self.x = False
        print(T)

## Goes all the way too the left of the tree to get the smallest value
    def minimumTree(self,T):
        if T[1]==[]:
            print("The minimum value is:",T[0])
            
## Recursive statment to make the main list smaller
        else:
            self.minimumTree(T[1])

## Goes all the way too the right of the tree to get the largest value
    def maximumTree(self,T):
        if T[2]==[]:
            print("The maximum value is:",T[0])
            
## Recursive statment to make the main list smaller
        else:
            self.maximumTree(T[2])

## Takes a value from the user and puts it in list T
    def getvalue(self,T):
        x=input("Enter a value to be put in the tree (Exit=q): ")
        try:
        
## Checks what the user inputed if 'q' then it will quit   
            if x=='q':
                self.T=T
            
## If it is a number then it will put it in the proper place useing the insert
            elif type(int(x))==int:
                self.L.append(int(x))
                self.insertTree(T,int(x))
                self.getvalue(T)
                
        except:
            
## If something else is inputed it will error
            print("Error",x)

## Takes in a T list and the value to in put in the new list T
    def insertTree(self,T,value):

## If it finds the right place it puts the value in that part of the list    
        if T==[]:

## Add value to the list            
            T.append(value)

## Add empty list for left and right path            
            T.append([])
            T.append([])

## Use recursive statment to find the right place for the value        
        elif value>=T[0]:
            
## Take the right path            
            self.insertTree(T[2],value)
        elif value<T[0]:

## Take the left path           
           self. insertTree(T[1],value)

## Takes the tree T 
    def decreasing_orderTree(self,T):

## Checks if the tree T is empty        
        if T==[]:
            pass
        else:

## If not put it in decreasing order           
            self.decreasing_orderTree(T[2])
            self.L.append(T[0])
            self.decreasing_orderTree(T[1])
            
## Takes the tree T 
    def increasing_orderTree(self,T):
        
## Checks if the tree T is empty 
        if T==[]:
            pass
        else:

## If not put it in decreasing order 
            self.increasing_orderTree(T[1])
            self.L.append(T[0])
            self.increasing_orderTree(T[2])


Binary_Search_Tree()
