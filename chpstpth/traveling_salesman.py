'''

import timeit
#from functools import cache
import sys
sys.setrecursionlimit(5000)

#@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

if __name__ == '__main__':
    print(timeit.timeit("factorial(10)", setup="from __main__ import factorial"))
    
    '''
import math
import random
import datetime
#import matplotlib.pyplot as plt

#Distance between two point
def distance(point1, point2):
    return (point2[0]-point1[0])**2 + (point2[1]-point1[1])**2

#Distance between two point
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class TSP_TimeTraveler():
    def __init__(self, dataval=None):
        self.count = 0
        self.position = None
        self.length = 0

    def get_position(self):
        return self.position

    def next_city(self):
        self.position = self.position.nextval
        return self.position

    #adding a city to the current route with Time traveler Algorithm :
    def add_city(self, point):
        print("point"+str(point))
        node = Node(point)
        if self.count <=0 :
            self.position = node
            print("node"+str(node.dataval)+", "+str(node.nextval))
        elif self.count == 1 :
            node.nextval = self.position
            self.position.nextval = node
            self.length = 2*distance(self.position.dataval,node.dataval)
            print("node"+str(node.dataval)+", "+str(node.nextval))
        else : 

            #Creating the traveler
            traveler = self.position

            c = traveler.dataval #current position
            n = traveler.nextval.dataval #next position

            #Calculating the length of adding the city to the path
            Min_L = self.length-distance(c,n)+distance(c,node.dataval)+distance(node.dataval,n)
            Min_Node = traveler

            traveler = traveler.nextval

            while traveler != self.position :
                c = traveler.dataval #current position
                n = traveler.nextval.dataval #next position

                #Calculating the length of adding the city to the path
                L = self.length-distance(c,n)+distance(c,node.dataval)+distance(node.dataval,n)

                #Searching the path to the of city with minimum length
                if L < Min_L :
                    Min_L = L
                    Min_Node = traveler

                traveler = traveler.nextval


            #Adding the city to the minimum path
            node.nextval = Min_Node.nextval
            Min_Node.nextval = node
            self.length = Min_L

        #Incrementing the number of city in the route
        self.count = self.count + 1

    #Get the list of the route
    def getRoute(self):
        result = []

        traveler = self.position
        result.append(traveler.dataval)

        traveler = traveler.nextval

        while traveler != self.position :
            result.append(traveler.dataval)
            traveler = traveler.nextval

        result.append(traveler.dataval)

        return result

    def Solve(self, Set_points):
        print("Solving TSP")

        #For calculating execution time
        time_start = datetime.datetime.now()

        #Copy the set points list
        points = Set_points.copy()

        #Transform the list into set
        points = set(tuple(i) for i in points)

        #Add 
        while len(points)>0 :
            print("Points left : ", len(points),'              ', end="\r")
            point = points.pop()
            self.add_city(point)

        result = self.getRoute()

        #For calculating execution time
        time_end = datetime.datetime.now()
        delta = (time_end-time_start).total_seconds()

        print("Points left : ", len(points),' Done              ',)
        print("Execution time : ", delta, "secs")

        return result

#######################
#Testing the Algorithm#
#######################

#Size of the set
size = 9

#Generating a set of random 2D points
points = []
for i in range(size):
    points.append((random.uniform(0, 100),random.uniform(0, 100)))

#Solve TSP
TSP = TSP_TimeTraveler()

route = TSP.Solve(points)
'''
#Plot the solution
plt.scatter(*zip(*points),s=5)
plt.plot(*zip(*route))
plt.axis('scaled')
plt.show()
'''