# Update a file through a python algorithm 
# In this organization restricted content is controlled with an allow list of IP addresses. The "allow_list.txt" identifies the IP addresses that need the access to the content
# removed. This algorithm updates the file and removes the IP that no longer have access.

# Open the file with the allow list.
# I'll name the "allow_list.txt" file as the "import_file" variable.
import_file = "allow_list.txt"


# Opened the file with "with" statement and .open() to read the contents. "with" help manage the resources by closing the file after exiting the statement. The using the "as" keyword
# to assign a variable named file storing the output of .open()
with open(import_file, "r") as file:
    
    # Storing the imported file in a variable with .read() convering the file into a string and allowing me to read it utilize its content.
    ip_addresses = file.read()

# Converting the string into a list to be able to remove individual IP addresses. .split() converts the contents on a string into a list, by default .split() splits the text by
# whitespace into list elements. After splitting the string I save the output back into the "ip_addresses" variable.
ip_addresses = ip_addresses.split()

# Iterating through the remove list with a for loop