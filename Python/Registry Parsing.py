
# coding: utf-8

# # Python & Windows Registry
# 
# As we know the registry has a ton of information - and using python we can begin to extract precise data and manipulate it to generate some great reports! Luckily, someone built a great library for reading artifacts from a registry file.
# 
# This library is called python-registry and can be found by searching pypi python-registry and installed on the commandline by typing `pip install python-registry`. 
# 
# *it requires the enum library as well
# 
# Make sure to install these dependencies in the Anaconda Python library installation directory
# ie. `C:\Anaconda\Lib\site-packages\Registry` and `C:\Anaconda\Lib\site-packages\enum`

# # Registry Structure
# 
# Registry hives have a defined structure
# 
# The file, and external container, is called a hive. Each hive contains the following data:
# - Root
#   - This is the base of the registry and keys and values
# - Key
#   - This is an entry in the registry that contains values. 
#   - It can also contain more keys
# - Subkey
#   - A key within a key
#   - This can be recursive
# - Value
#   - A set of information within a key
#   
# Let's make things more confusing...
# 
# ## Key Objects
# 
# Since a key can contain keys or values anything could be inside of it. This library handles this by allowing any value
#  or key to be called from a key object by using `.value('name of value')` to return a value by name or
# `.subkey('name of key')` to return a key by name. To get all of the available values, run `.values()` against the
# key object, and for the available subkeys, run `.subkeys()`. Both of these methods will return a list of value/key
# objects to then interract with further.
# 
# key = key object
# 
# ### Key Metadata
# - key.name() => Returns the name of the key
# - key.timestamp() => Returns a datetime object of the date information for the key
# - key.path() => returns full path of key
# - key.parent() => returns parent of current key (will error on root key)
# 
# ### Key Structure
# - key.value('value_name') => returns the specific value as called by name
# - key.subkey('subkey_name') => returns the specific subkey as called by name
# 
# 
# - key.values() => returns a list of the value objects
# - key.subkeys() => returns a list of subkeys as key objects
# 
# 
# - key.values_number() => returns an int of the number of values
# - key.subkeys_number() => returns an int of the number of subkeys
# 
# 
# - key.find_key('path of key') => provided a full path 
# 
# ## Value Objects
# 
# These objects represent the values within the keys. They are references by a name (`.name()`) or can prduce the
# value (`.value()`). These functions can get tricky as they are similar to the options available to the Key objects
# above. The data within a value can come in several forms, including int, str, hex, bin, unicode, and more. Be ready
# to handle some weird data when pulling information from the registry - especially from shadow volumes or recovered
# registry hives.
# 
# val = calue object
# 
# ### Value Metadata
# - val.name() => returns value name
# - val.value() => returns the value's value
# - val.value_type() => returns the data type of the value (as reference number)
# - val.value_type_str() => returns the data type as a human readable string

# In[ ]:

# Once installed, we can import it...
from Registry import Registry

# Once imported, we can give it a file to work with and create a registry object 
path_to_reg_hive = ''
registry = Registry.Registry(path_to_reg_hive)

print "======================="
print "Print names of all of the subkeys"
print "======================="

key_path = ''  # Path we want to open with the loop. When empty, it will use the root. Change to select a specific key

reg = registry.open(key_path)

# To explore potential Subkeys
for sub in reg.subkeys():
    print sub.name()

print "======================="
print "Print names of all of the values"
print "======================="

key_path = 'MountedDevices'

reg = registry.open(key_path)

for sub in reg.values():
    print sub.name()

    
print "======================="
print "For values in a key, prints the value name and value"
print "======================="

key_path = 'ControlSet001\\Control\\TimeZoneInformation'

reg = registry.open(key_path)

for sub in reg.values():
    # Some errors may occur within so we must wrap it with try/except to catch the errors
    try:
        # the code to try is placed here
        print sub.name() + ' => ' + str(sub.value())  # The value is not always a str - it can be an int, bool, etc.
        
    except UnicodeDecodeError, e:  # Specifying the error type will ensure other erros are handled differently
        # `e` is the information about the error that occured according to python
        print "Error Occured with key '" + sub.name() + "' => " + str(e)

        
        
print "======================="
print "Retreiving ints and non-string data"
print "======================="

key_path = 'Select'

reg = registry.open(key_path)

for sub in reg.values():
    if sub.name() == 'Current':
        print 'Current Control Set: ', sub.value()
    elif sub.name() == 'LastKnownGood':
        print 'Last Known Good Control Set: ', sub.value()
    elif sub.name() == 'Default':
        print 'Default Control Set: ', sub.value()
    elif sub.name() == 'Failed':
        print 'Failed Control Set: ', sub.value()
        
    


# So now that we have the basics down, lets do something meaningful with the system hive!

# In[ ]:

# Once installed, we can import it...
from Registry import Registry

path_to_reg_hive = ''
registry = Registry.Registry(path_to_reg_hive)


key_path = 'ControlSet00'  # Path we want to open with the loop. When empty, it will use the root. Change to select a specific key

# Open both
reg1 = registry.open(key_path + '1' + '\\enum\\USB') 
reg3 = registry.open(key_path + '3' + '\\enum\\USB')

# initalize variables
dict1 = dict()
dict3 = dict()
usb_diff = dict()
val_diff = dict()

# Collect data from ControlSet001
for sub in reg1.subkeys():
    l = list()
    for val in sub.subkeys():
        # Get serial numbers of USBS
        l.append(val.name())
        
    dict1[sub.name()] = l

# Collect data from ControlSet003
for sub in reg3.subkeys():
    l = list()
    for val in sub.subkeys():
        # Get serial numbers of USBS
        l.append(val.name())
        
    dict3[sub.name()] = l

# Perform comparison 
for usb1 in dict1.keys():
    if usb1 not in dict3.keys():
        usb_diff[usb1] = dict1[usb1]

# Print output
import pprint
print "========Different USBS========"
pprint.pprint(usb_diff)
print "========ControlSet001========="
pprint.pprint(dict1)
print "========ControlSet003========="
pprint.pprint(dict3)

dir(sub)


# # What's Next?
# 
# Now that the basics of registry parsing are complete, try to built a small tool that reads data from the registry and produces a report!
# 
# Here are a few ideas to get started:
# 
# - USB Reporter
# - MRU Parsing
# - System Information Report (ie. Timezones, OS info, etc.)
# - RunOnce Applications
# 
# There is pleanty of research done on the web that documents the artifacts needed to manually parse these artifacts - find it and automate it!
# 
# Congrats! You have completed the available tutorials and are ready to join the forensic community with Python scripting!
# 
