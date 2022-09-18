#my cpt (create performance task) for AP comuputer...
#science principles, these comments are to explain the code... 
#all of the code is origional and I recieved no assitance  

#the function of the program is to simulate scalars which are..
#a ability of vectors, when all of the values in a vector are multiplied...
#by the same amount it is called a scalar and the vector will become...
#stretched by that amount

def scalar(vector, factor):
    final = []
    for value in vector:
        #iterating through all values in the vector
        try: # a try and except block is a valid form of selection
            final.append(int(value) * int(factor))
            #appending the multiplied value to the final vector
            #the int function is neccesary because the items are strings however...
            #it will return an error if the value is floating point...
            #which is why we need to have a try-except statment
        except:
            return "no floating point values"
    return final

while True:
    vec = input().split(" ") #split splits the input string into an array of strings...
    # when seperated by the argument so "1 4 8" turns into ["1","4","8"]
    fac = input()
    if fac == "quit":
        break
    print(scalar(vec,fac))