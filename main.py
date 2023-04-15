import docx
import os

file_name = ".docx" # file to modify
path = "Downloads\\"
dl = os.path.join(os.path.expanduser("~"), path)
doc = docx.Document(dl+file_name)

# can modify if necessary
start = 1
curr_stop = 1
num = "0" # element to place inside table cell
intstate = 0

# variables to modify
stop = 2 # add 1 to the actual stopping point (steps + 1)
column = 0 # specify which column to edit, starting with 0
column_size = 0 # add 1 to the actual column size
steps = 1 # how many iterations before changing num
table1 = doc.tables[0] # specify what table to edit, starting with 0

while stop != column_size:
    if curr_stop == stop:
        start += steps
        stop += steps
        intstate += 1
    if intstate % 2 == 0:
        num = "0"
    else:
        num = "1"
    for row in range(start, stop):
        table1.cell(row, column).text = num
        curr_stop += 1
    
doc.save(dl+file_name)    