# whenever we use print() method, it automatically adds a newline character
    # into the output (\n).

a = [1, 2, 3, 4, 5]

for number in a:
    print(number, end=" -> my own line terminator\n")

print("<br/>")


'''
\n -> is called a newline character. This is valid in all the programming languages

Python, Java, GoLang, JavaScript, C, C++ ....
'''

'''
1
2
3
4
5

1 -> my own line terminator
2 -> my own line terminator
3 -> my own line terminator
4 -> my own line terminator
5 -> my own line terminator

<br/> -> HTML tag. HTML tags will not work in Python code
HTML -> Hyper Text Markup Language (Scripting Languages)
'''