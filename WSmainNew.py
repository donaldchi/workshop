import random
print("input nodes:")
n=input( )
print("input mean degree")
k=input( )
print("input probability")
p=input()
edgeList=[[]]
print "init start..."
for i in range(0,n):
   for j in range(i-k/2,i+k/2+1):
     if j<0:
       j=n+j
     if j>=n:
       j=j%n
     if abs(i-j)%(n-k/2)<=k/2 and i!=j:
           edgeList.append([i,j])
edgeList.remove([])   
print "init end..." 
print "compute start..."
for element in edgeList:
    start=element[0]
    end=element[1]
    #if start<end:
    if random.random()<p:
          newEnd=random.randint(0,n) #take by probability P
          #newEnd=newEnd%n
          if newEnd!=start and  [start,newEnd] not in edgeList:
            #index=edgeList.index(element)
            #edgeList.remove(element)
            #edgeList.insert(index,[start,newEnd])
            print str(start)+" "+str(newEnd) 
          else:
            print str(element[0])+" "+str(element[1])
    else:
      print str(element[0])+" "+str(element[1])
print "compute end..."
