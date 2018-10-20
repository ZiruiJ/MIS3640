import os
# print (os.getcwd())

# fout= open ('session14/output.txt', 'a' )  #file, could be not existed, and mode#

# line1= 'How many roads must a man walk down\n'
# fout.write(line1)
# line2= 'Before you call him a man?\n'
# fout.write (line2)
# fout.close()

# print(os.path.abspath('session14/output.txt'))  #exact location#
# print (os) ##自己补充###


def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    f_source= open (source, 'r')
    f_dest= open (dest, 'w')   #w is a type#

    for line in f_source:
        new_line= line.replace(pattern, replace)
        f_dest.write(new_line)


    f_source.close()
    f_dest.close()
#remember to close it after use it, avoid errors#



pattern = 'Jude'
replace = 'Jack'
source = 'output.txt'
dest = 'new_' + source
sed(pattern, replace, source, dest)   #实现不了#

# def walk(dirname):
#     """Prints the names of all files in 
#     dirname and its subdirectories.

#     dirname: string name of directory
#     """
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)

#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)

# folder= os.getcwd()

# walk(folder)

# #database should be a file to store data, and save the data into it. works like dictionary db student, student is the key#
# # we can check the value and key#

# import sqlite3
# db = sqlite3.connect('stocks.db')  #create a db#
# c = db.cursor()  #use as a mouth, read from the first line#
# c.execute('create table portfolio (symbol text, shares integer, price real)')
# db.commit()   #what's this??#

# stocks = [
#     ('GOOG', 100, 1093.05),
#     ('AAPL', 50, 217.68),
#     ('FB', 150, 155.42),
#     ('MSFT', 100, 109.03),
#     ('SNAP', 75, 6.88)
# ]
# c.executemany('insert into portfolio values (?,?,?)', stocks)
# db.commit()

# # for row in db.execute('select * from portfolio'):
# #     print(row)


# min_price = 150

# print('\nExpensive Stocks:')
# for row in db.execute('select * from portfolio where price > ?',
#                       (min_price,)):
#     print(row)

#save temporarily#

# import pickle

# # t1= [1,2,3]

# # f=open('save.p', 'wb')
# # s= pickle.dump(t1, f)
# # f.close

# t2= pickle.load (open('save.p', 'rb'))  #read byte
# print(t2)
