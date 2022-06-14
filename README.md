# This is WHAT, a python mask faux programming language
things
# Keywords
- Declaring variables

To declare a variable, type '#' for an integer, or '*' for a string. Then,
type your variable name, followed by angle brackets, where you put
in variable contents.

Examples:

'#.myinteger<12>' creates a variable 'myinteger' that has a value of 12.

'*.mystring<Hello!>' creates a variable 'mystring' that has a value of
'Hello!'

This makes the language statically typed.

- Printing

To print to the console, type 'P' followed by a period. Then put in angle
brackets. To use a variable, type '$' followed by the variable. 
Otherwise just pass in plain text.

Examples:

'P.<Hello World!>' prints 'Hello World!' to the console.

If we create a variable, '*.hello<Hello World!>', this creates a variable
with the value 'Hello World!'. Then, we can print it with
'P.<$hello>', which has the same effect.

- If statements

To create an if statement, 