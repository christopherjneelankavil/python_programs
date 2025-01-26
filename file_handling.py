# try:
#     with open('example.txt','r') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('File not found')

# try: 
#     with open('example.txt','r') as file:
#         for line in file:
#             print(line.strip())
# except FileNotFoundError:
#     print('File not found')

# try : 
#     with open('example.txt','w') as file:
#         file.write('This is a test file')
#         file.write('\nHello World')

# except FileNotFoundError:
#     print('File not found')


# try:
#     with open('example.txt','a') as file:
#         file.write('\nThis is a test file')
#         file.write('\nAppend operation is taking place')
# except FileNotFoundError:
#     print('File not found')


lines = ['First line\n','Second line\n','Third line\n']
# try : 
#     with open('example.txt','a') as file:
#         file.writelines(lines)

# except FileNotFoundError:   
#     print('File not found')

try:
    with open('example.txt','a') as file:
        for line in lines:
            file.write(line)
except FileNotFoundError:
    print('File not found')