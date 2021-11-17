#15. An array contains color names. Create a program that writes the contents of an array to a text file. Put each color on a separate line.
colors = ['red ', 'white ', 'black ', 'blue ']
with open('daun26.txt','a') as file:
    for i in colors:
        file.write(i+ '\n')
        
file.close()


