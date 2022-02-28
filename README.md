[Explanation](https://medium.com/fintechexplained/advanced-python-concurrency-and-parallelism-82e378f26ced)




# multiprocessing cube
Simple multiprocessing example


# pipe communication
If two processes need to communicate, Pipe’s the best choice. A pipe can have two end-points where each has `send() 
and `recv()` methods. Data in a pipe could get corrupted if two processes (threads) read from or write to the same 
end-point simultaneously. That's why queue is one of the solutions.

# queue
To store the output of multiple processes in a shared communication channel, a queue can be used. 
For instance, assume that the task is to find the cubes of the first ten natural numbers followed by adding 1 to each number.

Define two functions sum() and cube(). Then define a Queue (q) and call cube() function followed by the add() function


# How to Implement Shared Memory
Taking a cue from Queue, Shared Memory stores the shared data among the processes seamlessly. It can be of two types: Value or Array.


## Value
The number 4 is passed as an argument to the function cube(). value attribute fetches the actual value of the Value, num. The modified number is later sent to the cube() function. The final double-cubed number is then reflected in the print statement.