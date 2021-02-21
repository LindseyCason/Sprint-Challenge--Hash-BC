#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    #Array of weights
    #Length of array of weights
    #weight limit
    index1=0
    index2=1

    """
    YOUR CODE HERE
    """
    # if length == 1:
    #     return None

    # while index2 <= length:
    #     print("i1", index1, "i2", index2)
    #     print("EXPECTED LIMIT", limit)
    #     if index1 <= length-1:
    #         print("weights i1",weights[index1], "weights i2",weights[index2])
    #         if weights[index1] + weights[index2] == limit: #If there is a match
    #             print("MATCH ", weights[index1], "+", weights[index2], "=", (weights[index2] + weights[index1]))
    #             if weights[index1]> weights[index2]:
    #                 return(index1, index2)
    #             else:
    #                 return(index2,index1)
    #         if weights[index1] + weights[index2] != limit: #If they do not match
    #             print("old i2", index2)
    #             index2=index2+1 #increase index and try again
    #             print("new i2", index2)

    #         if index2 == length-1:
    #             index1 += 1
    #             index2 =0
    # else:
    #     return None

    for item in range(length):
        #num_needed is the number we need to add to the weights[index] to == limit
        num_needed= limit - weights[item]

        if hash_table_retrieve(ht, num_needed) is not None: # if the key with that num exists
            num=hash_table_retrieve(ht, num_needed)
            print("num needed", num_needed)
            print("num", num)
            print("item", item)
            if hash_table_retrieve(ht, num_needed)> item:
                return(hash_table_retrieve(ht, num_needed),item)
            else:
                return(item, hash_table_retrieve(ht, num_needed))
        
        hash_table_insert(ht, weights[item], item)#insert items into HT
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
