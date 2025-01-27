import os

# create a new directory

# try:
#     new_folder = 'new_folder'
#     os.mkdir(new_folder)
# except FileExistsError:
#     print(f"Folder {new_folder} already exists")



# items_of_parent_folder = os.listdir('.')
# print(items_of_parent_folder)
# items_of_sub_folder = os.listdir('./files')
# print(items_of_sub_folder)

dir_name = 'folder'
file_name = 'file.txt'

full_path = os.path.join(dir_name, file_name)
print(full_path)
cwd_path = os.path.join(os.getcwd(),dir_name,file_name)
print(cwd_path)