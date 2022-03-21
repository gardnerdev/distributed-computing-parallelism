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

## Array
A list of values can be shared amongst multiple processes. 
Array() initializes an empty array possessing int data type having a length 3. 
The array has been looped over by adding 1 to every element in it.

You can use arr in a different process, just as Value. This essentially is the concept of shared memory.

Note: `‘d’` indicates double-precision float, and `‘i’` (in Array(“i”, 3)) indicates a signed integer.




# How to Implement Server Process

A server process is the main process that gets triggered on the commencement of a Python program. Other processes could utilize its objects for manipulation. A manager object of the class Manager() controls a server process. Manager() supports multiple data types such as list, dict, Lock, RLock, Semaphore, BoundedSemaphore, Namespace, Condition, Event, Queue, Value, and Array.


```
python3 server-process.py
```

Shared Memory vs. Server Process:

    * Manager() supports a variety of data types in comparison with shared memory
    * Processes can share a single manager on different computers over a network
    * A server process is slower than shared memory


# Using Pool

The Pool class in multiprocessing can handle an enormous number of processes. It allows you to run multiple jobs per process (due to its ability to queue the jobs). The memory is allocated only to the executing processes, unlike the Process class, which allocates memory to all the processes. The Pool class takes the number of worker processes to be present in the pool and spawns the processes

Launching many processes using the Process class is practically infeasible as it could break the OS. Hence comes Pool which shall handle the distribution of jobs to and collection of results from all the spawned processes in the presence of a minimal number of worker processes (most preferably, the number of worker processes is equal to CPU cores).


Pool class comes with six valuable methods:

* apply() method blocks the primary process until all the processes are complete.
It accepts multiple arguments, maintains the order of the result, and isn’t concurrent



* apply_async() - A callback function in apply_async() can be used to return the value immediately 
after its execution is complete. This method maintains the order of the result and supports concurrency.
You can use wait() to block the asynchronous calls



* map_async() - Unlike map(), map_async() is non-blocking (and maintains the order of the result).



* imap() - Unlike map(), imap() doesn’t wait for all the results and returns an iterator (not a list).



Dockerfiles common for all projects:
- **Dockerfile.deployer** - Image used in GitLab CICD to communicate with AWS. Contains awscli. Image stored in GitLab registry. Avaiable tags: develop/master.
- **Dockerfile.poetry** - Base image for Kubeflow jobs. Contains poetry and python. Should be used as an input for project-specific dockerfiles. Image stored in GitLab registry. Avaiable tags: develop/master.



    ``` 
    curated/Dockerfile                                  python:3.8-slim-buster                                     
    libraries/Dockerfile                                gtm/core/data_products/python:3.8-slim-buster              
    libraries/kfp/Dockerfile                            python:3.8.12-bullseye                                     
    personify/personify_nba/Dockerfile                  python:3.8-slim-buster                                     
    commondbt/Dockerfile                                gtm/core/data_products/python:3.8-slim-buster                   
    ├──argo/workflows/Dockerfile                        gtm/core/data_products/python-poetry-tox:develop                
    ├──dockerfiles/Dockerfile.poetry                    python:3.8-slim-buster                                          
    └──dockerfiles/Dockerfile.deployer                  python:3.8-slim                                                 
    projects                                                                                                            
    └──business-effectiveness/pkg/common/Dockerifle     $BASE_IMAGE                                                     
    └──personify/pkg/                                                                                                   
    ├──visit-recommender/Dockerfile.visit-recommender   gtm/core/data_products/python-poetry-tox:develop                
    └──content-recommender                                                                                           
    |  ├──Dockerfile.content-recommendation             gtm/core/data_products/content-recommendation-base:latest       
    |  └──Dockerfile.content-recommendation-base        gps/personify/kf-pipelines/pipelines-base:latest                
    └──internal-content-recommender                                                                                  
        └──Dockerfile.internal-content-recommender      gtm/core/data_products/python-poetry-tox:develop                
    argo                                                                                                                
    └──Dockerfile.aws_kubectl                           registry.code.roche.com/gtm/core/data_products/aws_cli:latest   
    ```                        



| Registry                                                    |  Tags |
|gtm/core/data_products/argo-workflows                        |  7    |
|gtm/core/data_products/content-recommendation                |  6    |
|gtm/core/data_products/personify/visit-recommender           |  11   |
|gtm/core/data_products/content-recommendation-base           |  7    |
|gtm/core/data_products/business-effectiveness-common         |  10   |
|gtm/core/data_products/personify/internal-content-recommender|  9    |
|gtm/core/data_products/python                                |  1    |
|gtm/core/data_products/dbt_curated                           |  2    |
|gtm/core/data_products/dbt_argo_common                       |  3    |
|gtm/core/data_products/deployer                              |  1    |
|gtm/core/data_products/hcp-linking/twitter                   |  1    |
|gtm/core/data_products/aws_cli                               |  1    |
|gtm/core/data_products/python-poetry-tox                     |  2    |
|gtm/core/data_products/aws_kubectl                           |  1    |
|gtm/core/data_products/dbt_personify_nba                     |  2    |




Platform

|    location                                                |      Base image                 |      comment                |
|  k8s/eks/assets/notebook-server/Dockerfile                 |      $BASE_IMAGE                |                             |
|  data_lake/code_artifacts/lambda/                          |                                 |                             |
|  ├── dealforma_curation/Dockerfile                         |public.ecr.aws/lambda/python:3.8 |                             |  
|  └── eneric_file_loader/Dockerfile                         |public.ecr.aws/lambda/python:3.8 |                             |



| Registry                         | Tags |
| gtm/core/platform/aws-cli/cache  | 33   |
| gtm/core/platform/aws-cli        | 2    |
