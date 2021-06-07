# Reverse Polish Notation Calculator

Your assignment today is to implement a program that functions as a calculator. This won't be just any calculator, though, but a Reverse Polish notation calculator. There's a good chance you've never heard of this particular flavor of calculator, so here's a quick overview.

## Reverse Polish Notation

Many of us are solely used to entering computations into a calculator by putting an operation between two values. For example:  

| value | operation | value |
|:-----:|:---------:|:-----:|
|   3   |     +     |   4   |

However, there are other notations that can be used to express mathematical operations. Two of these are *prefix* and *postfix*. *Prefix* notation is also known as *Polish Notation*, and *postfix* notation is also known as *Reverse Polish* notation. Today we will be building a calculator that implements Reverse Polish Notation ([RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation)). For example, instead of writing `3 + 4` as we did above, we would write `3 4 +`, like this:  

| value | value | operation |
|:-----:|:-----:|:---------:|
|   3   |   4   |     +     |

This method of inputting computations actually makes it easier to write logic to perform the operations (for the computer, anyway). This is because the format lends itself to storing computations in a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)). A stack is a specific type of *queue* (know as last in, first out, or *LIFO*)  which only supports two types of operations - pushing and popping.

You can think of a stack as a list with less functionality. (**Note**: the [deque](https://docs.python.org/2/library/collections.html#collections.deque) class is the closest native Python class to a stack. When you go to implement you're version of an RPN calculator today, you can choose to use this class instead of a `list`, as it will technically give you speed gains on the pushing and popping operations you will need to perform) What an RPN calculator does is accept input one element at a time and push it onto the stack in turn. These elements can either be values or operations. In Python `list` lingo, pushing to the stack just means appending them to a `list`. When the user wants to perform an operation, the values necessary to perform the operation are [popped](https://docs.python.org/2/tutorial/datastructures.html) off the stack, in turn. The value resulting from that operation is then pushed back onto the stack. If it is the last value on the stack, then that value is returned. Otherwise, the process starts over again.


## RPN Example

Let's have a look at two examples. Say we want to calculate the result of the expression `(3 + 5) * (7 - 2)`. In RPN, that calculation can be written as `3 5 + 7 2 - *`. To input this calculation into a RPN calculator, one would enter those elements (in turn), and the corresponding operations would occur in the following order.

| Input |  Operation   |    Stack    |                   Other                   |
|:-----:|:------------:| ----------- |:-----------------------------------------:|
|   3   |  Push Value  | [ 3 ]       |                                           |
|   5   |  Push Value  | [ 3, 5 ]    |                                           |
|   +   |     Add      | [ 3, 5 ]    | Pop two values (3 then 5), push result, 8 |
|   7   |  Push Value  | [ 8 7 ]     |                                           |
|   2   |  Push Value  | [ 8, 7, 2 ] |                                           |
|   -   |    Subtract  | [ 8 5 ]     | Pop two values (7 and 2), push result, 5  |
|   *   |     Sum      | [ 8 5 ]     | Pop two values (8 and 5), push result, 40 |
|       |    Return    |   40        |                                           |



Let's have a look at a slightly more complex calculation: `6 + ((5 + 3) / 4) - 3`. In RPN, that calculation is written: `6 5 3 + 4 / + 3 -`. Step by step the calculation would look like this: 

| Input |  Operation   |    Stack    |                   Other                   |
|:-----:|:------------:| ----------- |:-----------------------------------------:|
|   6   |  Push Value  | [ 6 ]       |                                           |
|   5   |  Push Value  | [ 6, 5 ]    |                                           |
|   3   |  Push Value  | [ 6, 5, 3 ] |                                           |
|   +   |     Add      | [ 6, 8 ]    | Pop two values (3 then 5), push result, 8 |
|   4   |  Push Value  | [ 6, 8, 4 ] |                                           |
|   /   |    Divide    | [ 6, 2 ]    | Pop two values (8 then 4), push result, 2 |
|   +   |     Add      | [ 8 ]       | Pop two values (2 then 6), push result, 8 |
|   3   |  Push Value  | [ 8, 3 ]    |                                           |
|   -   |   Subtract   | [ 5 ]       | Pop two values (3 then 8), push result  5 |
|       |    Return    |   5         |                                           |



## RPN Calculator

Your assignment is to implement a calculator that operates with Reverse Polish notation. 

The following steps are suggestions, and while they could possibly make your journey through this programming assignment easier, they do not need to be followed. Remember, there are always multiple ways to solve programming problems. Sometimes there's an obvious solution, and sometimes not so much. Sometimes there's a more elegant solution, and sometimes they all function about the same. At a high level, the purpose of this lab is to have you work through a problem from start to finish so that you can get a good feel for what that process is like. In addition.


### Step 1: Interact with the Problem at a High Level

Take a look at wikipedia's description of the [algorithm](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Postfix_algorithm) for evaluating a string of operations in RPN. This is a great outline of what your program will need to be able to do. Follow along with the example, making sure you understand how the algorithm is evaluating the sequence and what the state of the stack is at each step.


### Step 2: Devise a Plan

With the RPN algorithm for computing a string of numbers and operations in mind, you're going to want to write a function that takes a string of characters and computes the result of the computation that the string of characters gives.

Consider how this problem can be broken down into smaller pieces that are easier to be solved. What will the big problem be? Consider making a function that will take a string of elements (separated by spaces) and evaluate them with a stack like storage procedure (LIFO queue). Some questions to ask yourself:

* What would that function look like? 
* What would you call it? 
* What parts of what it needs to do could be assigned to other functions? 
* What would they be called?
* What structure(s) are you going to use to store the data?

Once you answered some or all of the above questions, you are well on your way to writing some pseudocode.


### Step 3: Pseudocode

If you don't know what pseudocode is have a look at the file [Intro_to_pseudocode.md](Intro_to_pseudocode.md) inside this repo. 

After you've thought about the outline of the algorithm and how you will task out parts of it to functions, you are in a great position to begin pseudocoding. The nice thing about pseudocode in Python is that you can often write it in nearly accurate Python syntax. While variables you want to reference or functions you want to call might not exist yet, this isn't a problem because its just pseudocode! Then, when you want to go fill in the pseudocode and make it "real" code, you already have some lines that will work in Python. In addition, you should have great names for everything you'll need to name. For example, if I'm trying to solve a problem that needs to load a list of words, and then loop through that list and make a dictionary with the number of words of different counts, my pseudocode might look like the following:

```python
def get_word_count_dict():
    word_list = load_word_list()
    count_dict = make_count_dict()
    return count_dict


def load_word_list():
    with open get file(s):
        load words from files to list
    return word_list


def make_count_dict():
    for word in word_list:
        build up dictionary
    return dictionary
```

Now that this skeleton exists, it's easier to see what types of parameters each function will take, and think about how the whole program will flow. You might notice that both `load_word_list()` and `make_count_dict()` will need to accept parameters. Now that we've written this pseudocode, though, that's way easier to see than when you first thought about how to solve the problem.


### Step 4: Implement Real Code

At this point you should have a really good, nearly code-like structure for your program to create a function to calculate an RPN operation. Now you can go through and make the pseudocode working code by filling it in. Along the way, you'll start seeing places where you can make functions out of certain routines that do their own thing and/or are run in a loop, and that's great! You're well on your way to a working program.


### Step 5: Debug

Once you get your code to a state where it can run, you're at the point of debugging. There's a chance that you won't need to go through this step. However, it is much more likely that there will be some small error or something you didn't account for in your first solution.

Don't fret - this is part of the programming process, and even the best programmers have to debug their code. Embrace it. It means you're making mistakes and learning!

There are many methods by which you can debug. You can read through your code for syntax/logic errors, or you can print things out to make it easier to follow the flow of your program as it actually runs. You can also use the Python Debugger, or [pdb](https://docs.python.org/2/library/pdb.html) for short. This tool can be really helpful if you want to interact with your program similarly to the way you interact with IPython. `pdb` allows you to pause the Python interpreter while it is running your script. This gives you the opportunity to poke around and check the state of your program, the variables that exist, what their values are, etc, at any step. You can use `pdb` at any point in your programs execution (you just have to use it the right way). Check out this [blog post](https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/) for a great introduction on using this tool.


### Step 6: Building the User Interface

Now you have a function that will parse a string of operations. How will a user of your calculator interact with this function? Are they going to be prompted for input step by step, or do they have to give it to the function as a whole in the script? Have a look at the [input()](https://docs.python.org/2/library/functions.html#input) or [raw_input()](https://docs.python.org/2/library/functions.html#raw_input) built-in functions for receiving user input. 



## Further Exercises

At this point you should have a working Python script, that let's you enter a calculation in reverse polish notation and returns the result.
Congratulation!

If you're still motivated and want to improve your calculator there are several steps you can take to come closer to the functionality of a real calculator. 

### Additional step 1: Allowing for more calculations

Will the user be able to enter more than one calculation? If so, how can you use a loop to have your function called over and over? There's a tactic we use in Python when we can't foresee how long a loop is going to last - we'll use a `while True` statement and have logic in the loop determine when to `break` out of it. Since the `while True` will never trigger `False`, it will not end until it is manually broken out of.

Putting your function in a loop might change the way it needs to interact with the user. This change might involve printing a result in a different part of the program. It may involve changing what is returned from one of your functions to then be displayed. Again, there is no right answer - you'll just need to think critically about how your program is running. And test! Testing is what good programmers do, and they do it often.


### Additional step 2: Persist the Stack 

Getting full calculator-like functionality in your program requires a specific form of user input. Your program should work with getting the user input one number or operator at a time. If your calculator previously received the user input as a whole you will almost certainly have to change some implementation details of how your function evaluates RPN-strings since we now have to consider what's on the stack already. 

To get you started off on a potential foot, consider asking for user input in a `while True` loop that continually allows them to interact with the calculator in different ways.

The solution allows for operations to be pushed onto the stack indefinitely. When the user wants to evaluate the stack they merely have to enter nothing when prompted. Once the stack has been executed as fully as possible, the calculator will display the state of the stack. If at any time the user wants to see what's on the stack, they can enter `s`. If they want to clear the stack entirely, they can enter `c`. And if they want to quit the calculator they can enter `q`. Take a look at what interacting with a working solution could look like:

```
Operation(s)/Value(s): 4 5 +
Operation(s)/Value(s): s
Stack: 4.0, 5.0, +
Operation(s)/Value(s):  
Stack: 9.0
Operation(s)/Value(s): 7 sqrt
Operation(s)/Value(s): s
Stack: 9.0, 7.0, sqrt
Operation(s)/Value(s): 
Operation(s)/Value(s): s
Stack: 9.0, 2.64575131106
Operation(s)/Value(s): c
Operation(s)/Value(s): s
Stack: empty
Operation(s)/Value(s): q
```

### Additional step 3: Break your code!

Try to break your solution by entering calculations that make no sense. Can you make your program robust to these poorly/incorrectly formatted inputs? It's good to think about these things, though frequently it's very difficult to foresee all the possibilities of bad input.  


