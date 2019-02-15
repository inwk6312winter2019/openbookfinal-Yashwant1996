file =open(r"access.log","r")
for line in file:
 line_array = line.split(" ")
print (line_array[0])
