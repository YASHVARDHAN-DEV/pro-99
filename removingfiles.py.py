import os
import shutil
import time

def main():
	deletedfolderscount = 0
	deletedfilescount = 0
	path = "/PATH_TO_DELETE"
	days = 31

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if time >= getfileorfolderage(root_folder):
				remove_folder(root_folder)
				deletedfolderscount += 1 
			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
			

		else:
			if time >= getfileorfolderage(path):

				remove_file(path)
				deletedfilescount += 1 

	else:
		print('"{path}" is not found')

	print("Total folders deleted: {deletedfolderscount}")
	print("Total files deleted: {deletedfilescount}")


def remove_folder(path):

	if not shutil.rmtree(path):
		print("{path} is removed successfully")

	else:
		print("Unable to delete the "+path)



def remove_file(path):
	if not os.remove(path):
		print("{path} is removed successfully")

	else:
		print("Unable to delete the "+path)


def getfileorfolderage(path):
	ctime = os.stat(path).st_ctime
	return ctime