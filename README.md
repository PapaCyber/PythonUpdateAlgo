# Algorithm for file updates in Python

## Project description
In this project, access to company data is controlled through an allowed list of IP addresses. `Allow_list.txt` contains approved IP addresses. There are also IP addresses that are in the `remove_list`. I’ve created an algorithm to remove restricted IP addresses from the `Allow_list.txt` file when IP addresses from the `Allow_list` become restricted. 

## Open the file that contains the allow list
To get started I imported the file. I’ve created a variable named `import_file` and included the file name of the `allow_list.txt` file, and also included the variable `remove_list` for restricted IP addresses.

<img src="https://imgur.com/CJGdOfh.png" height="100%" width="100%"/>

I used the `with` statement along with the  `open()` function to open the file. 

There are two parameters, the variable `import_file` and `r` to indicate that I want to read the file. Additionally, I used the `as`  keyword to store the `open()` function as a variable named `file`.

## Read the file contents
To read the file, I used the `.read()` function to convert the file into a string and store it in a variable named `ip_addresses`. 

<img src="https://imgur.com/m2VhTNS.png" height="100%" width="100%"/>

This code allows me to open the `allow_list.txt` file and read it, using the variable `ip_addresses`. By converting the file into a string format, I can extract data from the file.

## Convert the string into a list.
To remove restricted IP addresses I need to convert the string into a list.

I used the `.split()` function to separate the string of `ip_addresses` with white space to make it easier to remove restricted IP addresses. I also incorporated this function into the variable `ip_addresses`.

<img src="https://imgur.com/cYKgigK.png" height="100%" width="100%"/>

## Iterate through the remove list

I used the iterative statement `for` to loop over the list of approved `ip_ addresses` to remove restricted IP addresses from the loop variable named `element`,  in the `remove_list`. The `in` keyword indicates to iterate through the sequence of IP addresses within the `remove_list`.

<img src="https://imgur.com/riyG6Rv.png" height="40%" width="40%"/>

## Remove IP addresses that are on the remove list
The algorithm needs to extract IP addresses from the `remove_list`  and use that data to determine what IP addresses need to be deleted from the approved  `ip_addresses` list. To do this I made a conditional statement.

<img src="https://imgur.com/VdrpqWJ.png" height="60%" width="60%"/>

I used the conditional statement `if` to evaluate if there are IP addresses that are from the `remove_list`, which is the variable named `element`. I used the `.remove()` function to remove restricted IP addresses (`element`) from the approved list of  `ip_addresses`.

## Update the file with the revised list of IP addresses 
Finally, the allow list file needs to be updated after removing restricted IP addresses. To do this I need to convert the list back into a string so I used the `.join()` function so it can be written into the text file.

<img src="https://imgur.com/jkQoyQf.png" height="100%" width="100%"/>

Since the file is now a string, I can open the file and use the  `.write()` function to replace the contents of `ip_addresses` which is the `allow_list.txt` file. I used the white space string `\n` to instruct Python to make a new line between IP addresses.

<img src="https://imgur.com/2OuZ1SV.png" height="60%" width="60%"/>

Previously I used the `r` sting keyword to read the file when it is opened, now I changed it to the `w` string keyword to indicate I want to write the file after changing its contents.

## Summary
This concludes my file update algorithm with Python. I used this algorithm to remove IP addresses that were in the `remove_list` variable from the `allow_list.txt` file which contained approved IP addresses. The algorithm involved opening the file, converting it to a string so it could be read, and then converting the string into a list so it could be stored in the variable `ip_addresses`. Then I used an iterative statement to iterate through IP addresses from the `remove_list` to identify what element from the `allow_list.txt` file needed to be removed and  updated. I used the `.remove()` function for the removal of restricted IP addresses. After removing these IP addresses, I used the `.join()` function to convert ip_addresses back into a string so I could rewrite the file `allow_list.txt` with an updated list of IP addresses.
