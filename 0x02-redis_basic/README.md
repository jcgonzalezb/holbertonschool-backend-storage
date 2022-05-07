# Python - Redis basic

## Description of the files inside this folder:

0. Task 0. A Cache class. In the constrtuctor method, store an instance of the Redis client as a private variable and flush the instance using flushdb.A store method that generates a random key (e.g. using uuid), store the input data in Redis using the random key. Returns the random key.
1. Task 1. A get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.Also, implement 2 new methods: get_str and get_int that will automatically parametrize Cache.get with the correct conversion function.
2. Task 2. A method that Counts how many times methods of the Cache class are called. Above Cache define a count_calls decorator that takes a single method Callable argument and returns a Callable. As a key, use the qualified name of method using the __qualname__ dunder method. Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.
3. Task 3. Define a call_history decorator to store the history of inputs and outputs for a particular function. In call_history, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively. call_history has a single parameter named method that is a Callable and returns a Callable. Decorate Cache.store with call_history.
4. Task 4. Implement a replay function to display the history of calls of a particular function. Use lrange and zip to loop over inputs and outputs.

All tasks are included in the exercise.py file.

## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Languages: Python 3.8.10, Redis server v=5.0.7
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>
<p align="left"> <a href="https://redis.io/" target="_blank" rel="noreferrer"> <img src="https://redis.com/wp-content/uploads/2021/08/redis-logo.png?&auto=webp&quality=85,75&width=500" alt="python" width="112" height="40"/> </a> </p>



## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
