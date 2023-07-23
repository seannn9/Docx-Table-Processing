import docx
import os

# Edit docx tables that contains patterns

file_name = "" # file to modify
path = "Downloads\\" # change for different file location
dl = os.path.join(os.path.expanduser("~"), path)
doc = docx.Document(dl+file_name)

# can modify if necessary
start = 1 # specify which row to start with
curr_stop = 1
num = "0" # element to place inside table cell
intstate = 0

# variables to modify
table1 = doc.tables[10] # specify what table to edit, starting with 0
column_size = 17
column = 0 # specify which column to edit, starting with 0
steps = 8 # how many iterations before changing num
stop = 9 # add 1 to the actual stopping point (steps + 1)


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