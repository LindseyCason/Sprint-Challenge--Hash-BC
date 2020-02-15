import hashlib
import requests
import sys
from uuid import uuid4
from timeit import default_timer as timer
import random
import json


def proof_of_work(last_proof):


    start = timer()
    proof = 0

    print("Searching for next proof")
    block_string= f'(last_proof)'.encode() #ENCODE LAST PROOF WHICH IS PASSED IN
    hashed = hashlib.sha256(block_string).hexdigest() #HASH IT USING SHA256 AND THEN HEXIDIGEST MAKES IT A READABLE HASH

    while not valid_proof(hashed, proof): #THIS WHILE LOOP USES THE VALID PROOF FUNCTION WHICH WILL ENCODE THE PROOF THEN HASHES IT UNTIL IT MATCHES THE REQUIRED PARAMS WE GAVE IT. IN THIS CASE, MATCH THE FIRST 6 DIGIST WITH THE LAST 6 DIGITS
        proof +=1 #IF IT DOESN'T MATCH INCREASE THIS PROOF COUNT
        # print("increasing", proof)

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    guess = f"{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    # print("guess ", guess, "guess hash", guess_hash)

    return guess_hash[:6] == last_hash[-6:]


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        # node = "https://lambda-coin.herokuapp.com/api"
        node = "https://lambda-coin-test-1.herokuapp.com/api"

    coins_mined = 0
    print("COINS", coins_mined)

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
