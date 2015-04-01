
An Introduction to it All
=========================

Welcome to Python, IPython Notebook, And Python in Forensics! All three
of these topics will be covered in this notebook. If you have experience
with any, feel free to jump to others! If you feel comfortable in all
three, feel free to select a different notebook, such as timelines!

Intro to IPython Notebooks
==========================

There are 2 types in this document: Text Blocks and Code Blocks

The text blocks are prompts that describe the material. I am sorry about
typos (spell check doesnt work here)

Code blocks are python scripts, and they all work together! They can run
individually, though can also reference eachother. When in doubt, or if
an error occurs, try running all of the code blocks in order from top to
bottom to see if it resolves the error.

In addition, code blocks can be edited and, in some cases, you do have
to do some editing. After running, the output (if any) will display
below the segment (as will errors). If you cannot fix it, feel free to
ask me or to grab a fresh copy from github.

To run a code block, use the play button on the top bar

Python in Forensics
===================

I find the biggest difference between python scripting and python
scripting for forensics to be the use of 3rd party libraries and file
handling. As opposed to other uses of Python, we are concerned with file
metadata more than content, and when we are interested in content, we
are interested in the structure and metadata about the content as well.
With this, a lot of 3rd party libraries exist to allow us to look into
weird file types and begin to handle this data.

As you go through this: google is your best friend Here are some python
search tips: - Start every query with python - If it involves a specific
library, the name of it should be the second word - mention the data
type of the value that is causing the error - stackoverflow - superuser

ie. Python lxml cannot parse string value

When in doubt, paste the entire error If still nothing:
https://www.reddit.com/r/learnpython

Python basics
=============

I cannot do nearly as good of a job as Learn Python the Hard Way, so I
reccomend using their site to walk you through the basics. If you are
looking to use Python for Forensic purposes, I would reccomend the first
39 examples, should take around an hour or two to work through. The
remaining examples are important, though not as applicable (except for
objective stuff (sort of)).

Here is the link to the first example:
http://learnpythonthehardway.org/book/ex1.html

Quick intro to Python!
----------------------

Below is a code block with basic python items. Everything is documented
within so read it line by line. I will seperate different sections with
a new code block to make things easier to understand.

.. code:: python

    ##
    # Comments
    ##
    # To start, this is a comment, a comment is anything that follows a `#` symbol
    # Comments are great for documentation and excluding lines of code from running
    """ In addition, this is also a comment* and must start and end with: """
    ''' This is also a comment*.Comments using this method
    can expand over several lines
    this can be handy in commenting out code that you have written and dont want
    to run anymore (or for the moment)
    '''
    # The * will be explained in data types below, but they are commentsish
    
    # Always use comments to document, it makes everyone's life easier
    
    ##
    # Data Types
    ##
    
    str()  # a way to express a string
    'A string is any text (12345) that is surrounded with quotes'
    "Notice that a string is started and completed with qoutes"
    """This is also a string, and also the reason for the * earlier, since 
    code wrapped in the triple quotes turns into a string and is not executed, therefore acts as a comment
    """
    '''
    dont forget about this string type too
    '''
    
    # An integer is any number, expressed without quotes
    int() # A way to express an integer
    123
    5654654
    112000
    0001
    
    # A float is a number that has a decimal place
    float() # a way to express a float
    1231.24321
    87654.241354
    0.41654
    
    
    # With these data types, we can do all sorts of math
    123 * 345
    'string 1 ' + 'string 2'
    234.5 / 23.0
    
    # A Boolean is a True or False value and are expressed as such (case-sensative)
    # They can also be expressed in binary as 1 and 0 or True and Flase 
    bool() # A way to express a bool
    True
    False
    1
    0
    
    
    # We also have more complex data types....
    
    # Lists are a series of values comma seperated and surrounded by brackets
    list() # a way to express a list
    ['value1', 2, 'value3', 4.0]
    
    # To access items in a list, we can either iterate or call for them individually
    # To iterate, we need a loop, like for
    y = ['value1', 2]
    for item in y:
        item # is the value of the item in the list
        
    # To call a single value, we need to know it's location in the list
    y[0] # is equal to 'value1'
    y[1] # is equal to 2
    y[-1] # grabs the last item in the list and is equal to y[1]
    
    # Dictionaries are key:value pairs. Essentially allowing us to recall data
    # from an object that contain a lot of value. 
    # A key is the name you give, the value is what you assign to it.
    
    # If it is confusing, play with it
    # if it is still confusing, see http://learnpythonthehardway.org/book/ex39.html
    dict() # a way to exptess a dictionary
    {'key1': 'value1', 'key2':234, 234:4.0}
    
    ##
    # Variables
    ## 
    
    # A variable may be named anything that starts with a character a-z, A-Z, or _
    # To assign a value to a variable, use the `=`
    ants123 = 'bugs'
    people = 6
    _apples = 'red'
    reallylongvariablename = 324.2342
    thiSHASmiXedCaSe = '123123123123'
    ThisIs546789EasierToRead = 234
    _123 = '2376dfgxcvsd'
    
    # It is a good idea to use underscores or camelCase to name variables
    fileName = '1.txt'
    file_path = '/home/'
    
    
    ##
    # Evaluations
    ##
    
    # we can evaluate data using certain characters
    
    # to see if a value is the same as another...
    True == True
    'value 1' is 'value 1'
    
    # Or opposite
    'value 1' != 'value 2'
    True is not False
    
    2 > 0 # greater than 
    2 >=1 #greater than or equal to
    4 < 6 # less than
    4 <= 6 # less than or equal to
    
    # We can combine these statements with `and` or `or` statements
    
    True == True and 123 < 234
    True != False or 534 >= 234
    
    ##
    # Special Characters
    ##
    
    # If you wish to use a single or double quote within the value of a string
    # you must escape it using an `\`
    """in example, i cannot type \"\"\" without the `\` character in front of it
    otherwise it will end the string like this"""



.. parsed-literal::

    'in example, i cannot type """ without the `\\` character in front of it\notherwise it will end the string like this'



More advanced things
--------------------

.. code:: python

    ##
    # Printing
    ##
    
    print 'it is as easy as saying `print` at the start of the statement'
    print ' you can print strings, ints, floats, lists, dictionaries....'
    print 1238768123
    print 234927432.234234234
    print 'you can print the product' + ' of equasions'
    print 234234/2342
    print 'woah the comment doesn\'t print' # see?
    print 'you can usually print 2 data types if you use commas', 123978687, ' see?'
    print 'it is better if we convert it to a string and add it though ' + str(123)
    print '123123' # this is a string of numbers
    print int('123123'), ' <= These are ints now'
    
    
    ##
    # Loops
    ##
    
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # There are 2 useful types of loops
    
    for number in list_of_numbers:
        # here is where we can do something with the number
        print number
        
    counter = 0
    size_of_list = 8
    while counter < size_of_list:
        list_of_numbers[counter]
        counter += 1 # Add 1 to the counter
        
    
    ##
    # Functions
    ##
    
    # This is cool stuff
    """
    Ok, so you are writing code and realize that you will want to use the same
    bit over and over - right? we use a function for this.
    
    """
    
    def double_the_number(number):
        """
        This function is specified by the `def` followed by the name of the function
        followed by `()` that contain any values that the function needs to run.
        
        Code inside the function needs to be nested with a tab otherwise it wont 
        run inside of it (plus it looks nice)
        """
        new_number = number * 2
        
        #The `return` statement returns the value 
        return new_number
    
    # To call a function, we call it by name, and pass the value
    double_the_number(5)
    
    # if we assign it to a variable, then we can use the returned data
    double = double_the_number(67)
    print double
    

.. parsed-literal::

    it is as easy as saying `print` at the start of the statement
     you can print strings, ints, floats, lists, dictionaries....
    1238768123
    234927432.234
    you can print the product of equasions
    100
    woah the comment doesn't print
    you can usually print 2 data types if you use commas 123978687  see?
    it is better if we convert it to a string and add it though 123
    123123
    123123  <= These are ints now
    1
    2
    3
    4
    5
    6
    7
    8
    134
    
