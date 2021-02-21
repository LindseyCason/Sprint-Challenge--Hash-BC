# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

#If you're adding to the front, the runtime will be O(n) becuase you'll have to scoot everything down to fit and with adding to the end it'll be O(1) for adding and removing because nothing has to be moved unless there is no more room.
* What is the worse case scenario if you try to extend the storage size of a dynamic array?
#Worse case when there is no room and you extend is having to make a new array with new size and then have to copy over each item from the previous array to the new one. O(n)

**Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?**
Block chains are blocks of data that keep track of a series of transactions. The structure consists of:
 -An index number which can be initialized to whatever for the first one, this will increment per block.
 -A timestamp that will update each time a block is mined
 -A list of transactions which will update as things change
 -Proof, which will be a number that represents how many times it took to validate. Ex. If you're asking it to match 6 leading number of 0's, it will run through random combinations of numbers until it matches the first 6 numbers as 000000, the proof will be how many checks/guesses it took to match that. Because the numbers are random, this number should never be the same number twice.
 -Previous hash, every block will have a hash from the block before it, any change to a block before (amount, etc) will alter the hash, this will cause a conflict because the next block has an expected hash, you can tell that that chain has been altered if the hash in the next block does NOT match the previous blocks hash.  
 
*Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?*
The proof of work is hard to do but easy to verify. It uses a hash algorithm to create a hash which is displayed as a 64 digit hexidecimal number. You give a leading number of zeros you want matched to verify and after numerous random guess and checks, once a match is found, it is validated and coins are awarded. This protects the chain from attack because the server validates the solution of the algorithm, the proof and the hash of the previous block will then be saved in the new block. If something is changed in one of the blocks a NEW solution will be needed for validation and will in turn alter what is needed for validation.




## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine a coin before the end of lunch.                                                               | The student was able to mine a coin before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 100 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
