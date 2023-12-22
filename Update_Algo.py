# Assign 'import_file' to the name of the file

import_file = "allow_list.txt"

# Assign 'remove_list' to list of IP addresses that no longer need access.

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build a 'with' statement to read the file.

with open("import_file", "r") as file:

# Use the '.Read()' function to convert file to a string and store it in a variable named 'ip_addresses'

ip_addresses = file.read()

# Convert ip_addresses from a string into a list using the '.split()' function.

ip_addresses = ip_addresses.split()

# Build iterative statement
# Name loop variable 'element'
# Loop through 'remove_list'

for element in remove_list:

    # Create conditional state to evaluate if 'element' in 'ip_addresses'

        if element in ip_addresses:

                # use the '.remove()' function to remove
                # elements from 'ip_addresses'

                    ip_addresses.remove(element)

# Convert 'ip_addresses' back to a string so that it can be written into the text file

ip_addresses = "\n".join(ip_addresses)

# Build 'with' statement to rewrite the original file

with open (import_file, "w") as file:

    # Rewrite the file, replacing its contents with 'ip_addresses'

    file.write(ip_addresses)