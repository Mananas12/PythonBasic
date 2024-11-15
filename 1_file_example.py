file1 = open('example.txt', 'w')
print('File Name: ', file1.name)
print('File open mode: ', file1.mode)
print('Readable: ', file1.readable())
print('Writeable: ', file1.writable())

def get_status(f):
    if (f.closed != False):
        return 'Closed'
    else:
        return 'Open'
    
print('File Status: ', get_status(file1))
file1.close()
print('File Status: ', get_status(file1))