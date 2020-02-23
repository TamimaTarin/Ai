import random
x1=[9,8,7,6,5,4,3,2]
x2=[6,5,9,8,3,2,5,4]
x3=[3,2,5,4,7,6,9,8]
x4=[2,1,6,5,7,6,5,4]

def fitness(arr):
    return (arr[0]-arr[1]+arr[2]-arr[3]+arr[4]-arr[5]+arr[6]-arr[7])


print (fitness(x1))
print (fitness(x2))
print (fitness(x3))
print (fitness(x4))
def totalfitness():
    return (fitness(x1)+fitness(x2)+fitness(x3)+fitness(x4))
print (totalfitness())    
def probability(arr):
    
    return (4/totalfitness())
print (probability(x1))
print (probability(x2))
print (probability(x3))
print (probability(x4))
def selection(arr):
    x=[]
    x.append(random.uniform(0.0,1.0))
    x.append(random.uniform(0.0,1.0))
    x.append(random.uniform(0.0,1.0))
    x.append(random.uniform(0.0,1.0))
    print(x)

    
    for i in range(len(x)):
        if x[i]>=0.00 and x[i]<=0.25 :
            print ("x1")
            
        elif x[i]>=0.25 and x[i]<=0.50 :
            print("x2")
        elif x[i]>=0.50 and x[i]<=0.75:
            print("x3")
        else: 
            print ("x4")
    
##    print("Random number for x1 : ", random.uniform(0.0,0.25))
##    print("Random number for x2 : ", random.uniform(0.25,0.50))
##    print("Random number for x3 : ", random.uniform(0.50,0.75))
##    print("Random number for x4 : ", random.uniform(0.75,1.0))

selection(x1)    
   










##f1=(fitness(x1))
##f2=(fitness(x2))
##f3=(fitness(x3))
##f4=(fitness(x4))

