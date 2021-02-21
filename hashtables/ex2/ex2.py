#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length-1)
    index=0

    for i in range(length):
        #insert items into hashtable
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        while True:
            if tickets[i].source == "NONE" and route[0] == None:
                #if the tickset has a source of None, it is the first, we put the destination first in route if route has None.
                print("Ticket source ", tickets[i].source)
                print("Route Index Value ", route)
                route[index] = tickets[i].destination
                index+=1
                print("Index", index)
            
            if i >0 and index<= i and index>0:
                #if we're past the first item,
                # and index is less than or = the current index
                # and the index is passed the first
                dest= hash_table_retrieve(hashtable, route[index-1]) 
                print(dest)#brings the value (destination) of the FIRST key (source)
                if hash_table_retrieve(hashtable, route[index-1]) != "NONE" and hash_table_retrieve(hashtable, route[index-1]) != None: #If it aint the last stop
                    route[index] = hash_table_retrieve(hashtable, route[index-1]) #set destination to the new index
                    print("Route: ",route)
                    index +=1 #increment the index again
                else:
                    # if there is no match, return
                    break
                    #STOP USING RETURNS!!!!!!!!!!!!
                    #WHEN YOU RETURN HERE YOU'RE ENDING EVERYTHIG AND IT NEVER RETURNS THE ROUTE!!!! JUST BREAK OUT OF THE LOOP
            else:
                # if all flights are done... kick rocks
                #WATCH YOUR INDENTATION, CAUSES A LOOP IF UNINDENTED
                break

    return route