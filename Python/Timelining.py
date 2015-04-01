
# coding: utf-8

# # About this script
# 
# This script is built to iterate across a directory and create a CSV timeline.
# 
# Using this iPython Notebook, you will be able to run the code in this webpage while following along with the tutorial.
# 
# Lets begin at the start of the script!
# 
# 

# # Starting a script
# 
# Every script should begin with the author's name, date, license, and small description. 
# 
# This information can be assigned to variables or in a comment block, either are sufficent.
# 
# If you plan on releasing several versions of the code, initializing a variable named version can be useful as well.
# 

# In[2]:

__author__ = 'Chapin Bryce'
__date__ = 20150322
__version__ = 0
__license__ = 'GPLv2'


# Great, our header is complete! Let's move on to starting the code.
# 
# To begin here, we should import libraries we will likely use. Though it does not make a big difference, importing
# only needed libraries is a great habit and can help reduce clutter that can cause more errors down the road.
# 
# For this script (creating a timeline) we should only need the `os` library for now. 
# 
# The os library is a standard library, meaning it is released with every installation of Python and available to all
#
# users. For the most part, it is standardized across versions as well, meaning that Python 2 and 3 should be able to
# run the same features. In addition, being a standardized library means that it has full documentation on Python's
# website. Though it may seem a bit cryptic at first, you will find it is usually better than 3rd party library
# documentation...I digress.
# 
# Lets import the `os` library:

# In[6]:

import os


# # Interracting with Files
# 
# Wasn't that easy - well lets step it up a little without the additional tangents.
# 
# Lets begin with a sample file to use as test data. 
# 
# If the setup was completed successfully, in your document's folder, there should be a folder
# named `IPython Notebooks/data`. Inside this directory should be `1.txt`, a small text file. We will be using
# this text file as sample data for now, so ensure you have it installed at that location.
# 
# **In this code block we are going to perform a few steps at once:**
# 
# 0. We will tell Python our username
# 1. Python will take our user name and plug it into the pre-made path to the file
# 2. We are going to have Python check if it exists at the path it determined and print True or Flase
# 3. If it does exist, we will have Python tell us the file's size, if it doesnt exist it will print `Sorry, we could not find the file`
# 
# 
# **Things to note:**
# 
# - the variable name `file` is reserved and should not be used

# In[22]:

username = '' # Enter your username here as it appears in `c:/users/`
file_of_interest = 'C:\\Users\\' + username + '\\Documents\\IPython Notebooks\\data\\1.txt'

it_does_exist =  os.path.exists(file_of_interest)

print it_does_exist

if it_does_exist:
    size = os.path.getsize(file_of_interest)
else:
    size = 'Sorry we could not find the file'

print size


# ## Let's take a closer look at File Metadata
# 
# Forensic examiners are obsessed with metadata, and rightfully so. There is a great deal of information available
# that many users who we investigate forget about and ~~we get to use it against them~~ we are able to leverage it
# in determining what happened.
# 
# In a timeline, metadata can be an important asset in determining the importance of a file. So let's take a look at
# a few basic metadata fields that are quite valuable.
# 
# #### File Name
# 
# This seems quite simple, and is. Though it is important in a timeline to have a field with a seperate column for the
#  file name so that it can be sorted on or used for easier detection.
# 
# #### File Path
# 
# Once again, this is another simple concept, though knowing the full file path is key in a preservation and analysis
# point of view.
# 
# #### File Size
# 
# We already know how to get this data!
# 
# #### MAC Times
# 
# Ah something a little more complex - right? Not really! This is also easy to acquire and format. We will use
# the `datetime` library to format the dates, as it is also a standard library. There are great 3rd party libraries
# that do better date formatting (like `python-dateutil`) but we will stick with less dependecy on new libraries
# for now
# 
# 

# In[ ]:

# File name
file_name = os.path.basename(file_of_interest)

print "File Name:\t" + file_name

# File Path
file_path = os.path.abspath(file_of_interest)

print 'File Path:\t' + file_path

# File Size - Add this in yourself (reference the previous example)
##
# TODO add in the code to get the file size
##

print 'File Size:\t' + file_size

# File Dates and Times
import datetime

# Setup formatting of retrieved dates in MM/DD/YYYY HH:MM:SS (ie. 03/02/2015 05:33:45)
##
# TODO Use the link below to add ` AM/PM` to the format 
# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
##
date_format = '%m/%d/%Y %I:%M:$S'

modified_time_raw = os.path.getmtime(file_of_interest)
accessed_time_raw = os.path.getatime(file_of_interest)
created_time_raw = os.path.getctime(file_of_interest)

# Now we will convert the strings into the formatted dates
# The datetime.datetime.fromtimestamp() is a function that reads an integer and converts it into a 'best guess' timestamp. 
modified_time_converted = datetime.datetime.fromtimestamp(modified_time_raw)
# Since the returned timestamp is now read by python, we need to tell it what format we would like to read it in. 
# To do this we will use the date_format that we specified earlier within the Strife Time or `strftime()` function to change 
# it to the correct format
modified_time = modified_time_converted.strftime(date_format)

##
# TODO Add in created and accessed times
##

print 'Modified Time:\t' + modified_time
##
# TODO Add in created and accessed times
##



# ### Outputting the data
# 
# Now that we have collected the data, let's start by creating some output for an examiner to read!
# 
# Though we can display information in the command prompt using print, it can be a pain to read. The purpose of
# using python is to increase the usability of the data, so let's do that.
# 
# A CSV document is litterally comma seperated values, meaning we can draft this easily. To do this, we need to
# open a new file for output and write to it. This is also very easy in python.
# 

# In[ ]:

# We will write to 'data/report.csv' and the mode is 'w' or write. 
# For more IO modes, checkout https://docs.python.org/2/tutorial/inputoutput.html
file_out = open('data/report.csv', 'w')

##
# TODO add the remaining column names as a comma-seperated list.
#  The columns shoudl be ordered: Name, Size, M, A, C, Path
## 
columns = 'File Name, File Size,'

# Lets write the columns as our first line
file_out.write(columns)

# Now let's gather the collected data into a single line, following the order of the columnes

##
# TODO Complete the line with the data ordered to match the columns
##

line = file_name + ',' + file_size + ','

##
# TODO Write the line to the file
##



# Now that the line is written to the file, lets close the file so we can save it and open it with Excel
file_out.close()



# Go ahead and open the file in Excel now!
# 
# Good Work! But we are not done
# 
# A timeline of 1 file is not very useful - right? So lets make one that crawls through a directory to give us a
# file listing!
# 

# ## Recursing through files
# 
# Once again, the `os` library comes in handy with it's walk function. Walking allows us to explore a subdirectory
# and access all of the files and directories within it!
# 
# This can get confusing quickly, so we are going to take it slow to start...
# 
# 1. Declare the path we wish to recurse through
# 2. Use the `os.walk()` function to iterate through and handle the file recursion for us
# 3. Us a `for` loop to interpret the data returned from `os.walk()`
#   - This function returns 3 elements for us to work with
#     - `root`: the absolute file path to the current directory being explored
#     - `directories_in_root`: a list of directories found at the current root
#     - `files_in_root`: a list of files found at the current root

# In[33]:

import os

# We are initializing a list variable so we can store information about each file we recurse through.
file_list = list()

username = 'cbryce' # Add in your username to set the proper directory for now

# Notice the `//`, this is because, as seen earlier with `\t` the `\` character is used to mark special items in strings.
# To use a litteral `\` we must escape it, using `\`, resulting in `\\`

rpath = 'C:\\Users\\'+username+'\\Documents\\IPython Notebooks'

# The below `for` statement is used to iterrate through data. In this case, the for statement is iterrating through
# data that is returned
# from the use of the `os.walk()` function. 

# Another note: 
# The tabs in python are very important, ensure that all actions you wish to occur within the loop are visually
# indented to show!
for root, directories_in_root, files_in_root in os.walk(rpath):
    # Now we are inside the current root directory. 
    # Inside this we have a list of Directories and a list of files (like a normal explorer view)
    
    # To iterate through the list of files, we have to use another `for` loop
    for file_entry in files_in_root:
        # Here we are able to look into each file individually
        # At this point we can do whatever we want to the individual file and ensure the same process 
        # happens to all files in all subdirectories
        
        print 'File Name: ' + file_entry  # This prints the file name only
        print 'File Root: ' + root  # The path to the root entry
        print 'File Path: ' + os.path.join(root, file_entry)  # This also prints the full path and is a *better* way to join file paths
        print '-----------------------'
        # Using the list we initialized earlier, lets add the data we gathered to it
        file_list.append(file_entry)
        
# Now let's take a look at the list we made
print "File List:", file_list            

# Finally, lets use a for loop to modify the information from the list
for entry in file_list:
    print 'Collected Entry: ' + entry


# # Putting it all together - Making a timeline script!
# 
# Here we go - we are about to put all of this information together into a single script to create a SUPER TIMELINE!
# 
# I know there are a lot of steps below, but take them 1 at a time!
# 
# In the below code block:
# 
# 0. Pick a path to recurse over and create an empty list
# 1. add in the recursion for that path using a `for` loop and `os.walk()` as highlighted above
# 2. within the loop, add the file metadata code from earlier
#   - write this data into a comma seperated string
#   - Append this string of data into a list
# 3. after the loop completes, setup an output file to write to
# 4. write the column names as a comma seperated string to the outputted file
# 5. start a for loop that iterated through the list
#   - for each string in the list, write it to the output file
# 6. close the file in Python
# 7. Open the file in Excel! Good Job!

# In[ ]:

## Put your code in here! Good luck and take it 1 step at a time!



