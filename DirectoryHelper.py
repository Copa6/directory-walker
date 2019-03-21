import os

def get_dir_list(path, n=1, new_dir=None, main_dir_list=[], create_subdirs=False, print_dirs=False):

	"""
	Print naems of all directories and contained directories/files in a given file path
	Parameters:
		path: string. Path to the directory where the search is to be performed
		n: int. Number of tab spaces to be put before printing. To give a structured look to the output
		new_dir: string. Used in recursive calls to remove the new directory name found in the folders 
	"""
	# main_dir_list = []
	dir_list = []
	for entry in os.scandir(path):
		# if a new directory is found, call recursively to keep going deeper into subfolders until there are no directories, such that all files are printed
		# else print file naem
		if entry.is_dir():
			new_dir = '/' + entry.name
			path += new_dir
			if print_dirs:
				print('\t'*(n-1) + path)
			n +=1 
			dir_list = get_dir_list(path, n, new_dir, main_dir_list=main_dir_list, create_subdirs=create_subdirs)
			path = ''.join(path.rsplit(new_dir, 1)) #remove the last occurance of the new directory, to go one directory up and continue search
		else:
			new_dir = None
			if print_dirs:
				print('\t'*n + str(entry.name))
			dir_name = path +('/') +  str(entry.name)
			dir_list.append(dir_name)

	if create_subdirs:
		main_dir_list.append(dir_list)
	else:
		main_dir_list += dir_list

	ret_val = dir_list if new_dir is not None else main_dir_list
	return ret_val



def get_file_name_from_path(file_path):
	file_name = os.path.basename(file_path)
	path = os.path.dirname(file_path)
	extension = os.path.splitext(file_path)[1]
	return path, file_name, extension

get_dir_list("path/to/directory")