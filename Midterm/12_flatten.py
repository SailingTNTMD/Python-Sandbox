"""
Name: 12_flatten
Author: Lio Hong
Date: 20180726
Goal:
      Write a function to flatten a list. The list contains other lists, strings, or ints.
      For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into
      [1,'a','cat',2,3,'dog',4,5]
      I.E. transfers all entries from nested lists to main list.
Comments:
      Might have to use recursion for this.
      What's the base case then?
      A single list? Or an entry that is a list itself?
      Anyway, to insert the sublist entries we have list.insert(i,x)
      Might have to do some reverse-traversing to manage it though.

      Knowing this, the base case will be a list containing at least one sublist entry.
 
"""
aList = [88,[1,'a',['cat'],2],[[[3]],'dog'],4,5]
##OUTPUT =  [88,1,'a','cat',2,3,'dog',4,5]
def flatten(aList):
      ''' 
      aList: a list 
      Returns a copy of aList, which is a flattened version of aList 
      '''
      bList = aList
      
      for i in bList:
            print(i)
            if type(i) == int or type(i) == str:
                  continue
            elif type(i) == list:
                  for b in range(0,len(i)):
                        bList.insert(bList.index(i),i[b])

                  #Assumes there are no duplicate sublists
                  #Even if there were, only the leftmost would be removed.
                  bList.remove(i)
                  print(bList)
                  return bList

      

##      for j in aList:
##            print(j)
##            while type(j) == list:
##                  flatten(aList)
            
      
