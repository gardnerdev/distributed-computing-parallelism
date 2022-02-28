[Explanation](https://medium.com/fintechexplained/advanced-python-concurrency-and-parallelism-82e378f26ced)




# multiprocessing cube
Simple multiprocessing example


# pipe communication
If two processes need to communicate, Pipe’s the best choice. A pipe can have two end-points where each has `send() 
and `recv()` methods. Data in a pipe could get corrupted if two processes (threads) read from or write to the same 
end-point simultaneously.
