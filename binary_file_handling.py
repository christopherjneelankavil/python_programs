data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
# try:
#     with open('example.bin','wb') as source_file:
#         source_file.write(data)
# except FileNotFoundError:
#     print('File not found')


# try: 
#     with open('example.bin','rb') as source_file:
#         print(source_file.read())

# except FileNotFoundError:
#     print('File not found')

# try :
#     with open('files\source_file.txt','r') as source_file:
#         content = source_file.read()
#         print(content)

#     with open('files\destination.txt','w') as destination_file:
#         destination_file.write(content)
# except FileNotFoundError:
#     print('File not found')

# try :
#     with open('files\source_file.txt','r') as source_file:
#         lines = source_file.readlines()
#         print(f'Number of lines in the file : {len(lines)}')
#         print(f'Sum of words {sum(len(lines.split()) for lines in lines)}')
#         print(f'Sum of characters {sum(len(lines) for lines in lines)}')

# except FileNotFoundError:
#     print('File not found')


try : 
    with open('example.txt','w+') as file:
        file.write('This is a test file')
        file.seek(0)
        print(file.read())
except FileNotFoundError:
    print('File not found')