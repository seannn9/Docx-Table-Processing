import docx
import os

file_name = "newtables.docx"
path = "Downloads\\"
dl = os.path.join(os.path.expanduser("~"), path)
doc = docx.Document(dl+file_name)

start = 1
stop = 2 # add 1 to the actual stopping point
curr_stop = 1
num = "0"
intstate = 0
column = 3 # specify which column to edit, starting with 0
row_size = 17 # add 1 to the actual column size
steps = 1 #
table1 = doc.tables[2] # specify what table to edit, starting with 0

while stop != row_size:
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