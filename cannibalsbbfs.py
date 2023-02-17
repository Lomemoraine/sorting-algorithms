#Python program to illustrate Missionaries & cannibals Problem 
#This code is contributed by Sunit Mal
print("\n")
print("\tGame Start\nNow the task is to move all of them to right side of the river")
print("rules:\n1. The boat can carry at most two people\n2. If cannibals num greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board")
lM = 3            #lM = Left side Missionaries number 
lC = 3            #lC = Left side Cannibals number 
rM=0            #rM = Right side Missionaries number 
rC=0            #rC = Right side cannibals number 
userM = 0        #userM = User input for number of missionaries for right to left side travel
userC = 0        #userC = User input for number of cannibals for right to left travel  
k = 0
print("\nM M M C C C |     --- | \n")
try:
    while(True):
        while(True):
            print("Left side -> right side river travel")
            #uM = user input for number of missionaries for left to right travel 
            #uC = user input for  number of cannibals for left to right travel 
            uM = int(input("Enter number of Missionaries travel => "))    
            uC = int(input("Enter number of Cannibals travel => "))
  
            if((uM==0)and(uC==0)):
                print("Empty travel not possible")
                print("Re-enter : ")
            elif(((uM+uC) <= 2)and((lM-uM)>=0)and((lC-uC)>=0)):
                break
            else:
                print("Wrong input re-enter : ")
        lM = (lM-uM)
        lC = (lC-uC)
        rM += uM
        rC += uC
  
        print("\n")
        for i in range(0,lM):
            print("M ",end="")
        for i in range(0,lC):
            print("C ",end="")
        print("| --> | ",end="")
        for i in range(0,rM):
            print("M ",end="")
        for i in range(0,rC):
            print("C ",end="")
        print("\n")
  
        k +=1
  
        if(((lC==3)and (lM == 1))or((lC==3)and(lM==2))or((lC==2)and(lM==1))or((rC==3)and (rM == 1))or((rC==3)and(rM==2))or((rC==2)and(rM==1))):
            print("Cannibals eat missionaries:\nYou lost the game")
  
            break
  
        if((rM+rC) == 6):
            print("You won the game : \n\tCongrats")
            print("Total attempt")
            print(k)
            break
        while(True):
            print("Right side -> Left side river travel")
            userM = int(input("Enter number of Missionaries travel => "))
            userC = int(input("Enter number of Cannibals travel => "))
              
            if((userM==0)and(userC==0)):
                    print("Empty travel not possible")
                    print("Re-enter : ")
            elif(((userM+userC) <= 2)and((rM-userM)>=0)and((rC-userC)>=0)):
                break
            else:
                print("Wrong input re-enter : ")
        lM += userM 
        lC += userC
        rM -= userM
        rC -= userC
  
        k +=1
        print("\n")
        for i in range(0,lM):
            print("M ",end="")
        for i in range(0,lC):
            print("C ",end="")
        print("| <-- | ",end="")
        for i in range(0,rM):
            print("M ",end="")
        for i in range(0,rC):
            print("C ",end="")
        print("\n")
  
      
  
        if(((lC==3)and (lM == 1))or((lC==3)and(lM==2))or((lC==2)and(lM==1))or((rC==3)and (rM == 1))or((rC==3)and(rM==2))or((rC==2)and(rM==1))):
            print("Cannibals eat missionaries:\nYou lost the game")
            break
except EOFError as e:
    print("\nInvalid input please retry !!")



# class State:
#     def __init__(self, missionaries, cannibals, boat):
#         self.missionaries = missionaries
#         self.cannibals = cannibals
#         self.boat = boat
        
#     def is_valid(self):
#         if self.missionaries < self.cannibals and self.missionaries > 0:
#             return False
#         if (3 - self.missionaries) < (3 - self.cannibals) and (3 - self.missionaries) > 0:
#             return False
#         return True
        
#     def is_goal(self):
#         if self.missionaries == 0 and self.cannibals == 0:
#             return True
#         return False
    
#     def __str__(self):
#         return "({}, {}, {})".format(self.missionaries, self.cannibals, self.boat)

# def move_people(state, missionaries, cannibals):
#     new_missionaries = state.missionaries - missionaries
#     new_cannibals = state.cannibals - cannibals
#     new_boat = 1 if state.boat == 0 else 0
#     return State(new_missionaries, new_cannibals, new_boat)
    
# def dfs(state, path, visited):
#     if state.is_goal():
#         path.append(state)
#         for s in path:
#             print(s)
#         print()
#         return True
    
#     if state in visited:
#         return False
    
#     visited.add(state)
#     path.append(state)
    
#     if state.boat == 0:
#         for missionaries in range(3, -1, -1):
#             for cannibals in range(3, -1, -1):
#                 if missionaries + cannibals > 2 or missionaries + cannibals == 0:
#                     continue
#                 new_state = move_people(state, missionaries, cannibals)
#                 if new_state.is_valid():
#                     if dfs(new_state, path[:], visited):
#                         return True
#     else:
#         for missionaries in range(1, 4):
#             for cannibals in range(1, 4):
#                 if missionaries + cannibals > 2 or missionaries + cannibals == 0:
#                     continue
#                 new_state = move_people(state, missionaries, cannibals)
#                 if new_state.is_valid():
#                     if dfs(new_state, path[:], visited):
#                         return True
#     return False

# start = State(3, 3, 0)
# dfs(start, [], set())