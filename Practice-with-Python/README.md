Description of exercises
--------------------------------

####**p1_cadenas.py:**
Writings functions given a string and a character:

* Insert the character between each letter of the string. Eg 'separate' and ',' should return
'S, e, p, a, r, a, t, e'

* Replace all spaces by the character. Eg 'my file texto.txt' and '_'
should return 'mi_file_texto.txt'

* Replace all digits in the character string. Eg 'password is: 1540' and
'X' should return 'password is: XXXX'

* Insert a character each 3 digits in the string. Ex. '2552552550' and '.' Should
return '255.255.255.0'

####**p2.py:**
Write functions that given two strings:

* Indicate if the second string is a substring of the first string. For example,
'String' is a substring of 'substring'.

* Return is earlier in alphabetical order. For example, if you receive 'kde' and 'gnome' must return 'gnome'.
Tuples and Lists

####**p3_tuplas.py and p4_tuplas.py:**
* Write a function that takes a tuple of names and each name print the message Dear <name>, vote for me.

* Write a function that takes a tuple of names, an origin position p and a number n, and print the previous message for the n names found from the p position.

* Modify the above functions to take into account the gender of the recipient, to this end, shall receive a tuple of tuples, containing the name and gender.

####**busqueda.py:**
Write a function that receives a search string and a list of tuples (fullname, telephone), and search through the list, all entries that contain the full name of the received string (can be the first, last or only a part of any of them). It should return a list of all tuples found.

####**Diccionario.py:**
Write a program to be asking the user to enter nombres. If the name is on the agenda (implemented with a dictionary), should show the phone and optionally allow modify if not correct.
If the name is not found, should be allowed to enter the corresponding phone.
The user can use the string "*" to exit the program.

####**botellaYcorcho.py:**
* Write a cork class that contains an attribute bodega (string with the name of the winery).

* Write a bottle class containing a cork attribute with a reference to cork lid, or None if it is uncovered.

* Write a corkscrew class that has a method to uncover you receive a bottle, you pull the cork and a reference to the cork out is saved.

* Adding a cleaning method, remove the cork corkscrew.

####**Ejercicio1.py:**
Write functions giving a string as a parameter:

* Print the first two characters.

* Print the last three characters.

* Print the chain every two characters. Ex .: 'recta' should print 'rca'

* The chain in reverse. Ex .: 'Hola mundo!' Should print '! Odnum aloh'

* Print the chain in one direction and in reverse. Eg 'reflejo' prints 'reflejoojelfer'.

####**Ejercicio2.py:**
Write a function that receives a tuple of elements and indicate if they are ordered from lowest to highest or not.

####**Ejercicio3.py:**
Write a function that receives an unordered list and an element that:

* Locate all the items matching the passed parameter and returns the number of matches found.

* Find the first occurrence of the element in the list and return its position.

* Using the above function, search all items matching the passed parameter and returns a list of positions.

####**Ejercicio4.py:**
Write a function that takes a list of tuples, and returns a dictionary where the keys are the first elements of the tuples, and the values ​ are listed with the second elements.
For example:
l = [('Hola', 'Don Pepito'), ('Hola', 'Don Jose'), ('Good', 'day')]
print tuplas_a_diccionario(l)
It should show: {'Hola': ['Don Pepito', 'Don Jose'], 'Good': ['day']}


