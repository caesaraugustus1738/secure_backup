import local_vars
import shutil
import os
from pathlib import Path
from cryptography import fernet

# print(Path(__file__).suffix)
def file_encrypter(file, key):
	'''Encrypts single file with symmetrical Fernet encryption.
	'''
	with open(file, 'rb') as f:
		file_contents = f.read()

	f_key = fernet.Fernet(key)
	encrypted_contents = f_key.encrypt(file_contents)

	with open(file, 'wb') as f:
		f.write(encrypted_contents)

class Archive:
	def __init__(self, source=None, dest=None, format_=None):
		self._source = Path(source)
		self._source_encrypt = Path(str(self._source)+'_encrpyt')
		self._source_parent = Path(source).parents[0]
		self._source_dir = Path(source).name
		self._format = format_
		self._dest = Path(dest)
		os.chdir(self._source_parent)
		print(os.getcwd())


	def encrypt_source(self, key):
		'''Copy archive source in place and encrypt files.
		'''

		# Copy source dir
		shutil.copytree(self._source, self._source_encrypt)

		# # Walk and encrypt
		for root, dirs, files in os.walk(self._source_encrypt):
			for file in files:
				if file not in '.DS_Store':
					file_path = root + '/' + file
					file_encrypter(file_path, key)


	def archive(self):
		shutil.make_archive(base_name=self._dest, 
							format=self._format,
							root_dir=self._source_parent, 
							base_dir=self._source_dir)
	

	def secure_archive(self, key):
		self.encrypt_source(key)

		shutil.make_archive(base_name=self._dest, 
							format=self._format,
							root_dir=self._source_parent, 
							base_dir=self._source_encrypt.name)

		os.removedirs(self._source_encrypt)




	# def unarchive(self):
		# Unpack the archive
		# shutil.unpack_archive(filename=backup_dest, extract_dir=unpack_dir, format='zip')

# Encryption walk
# for root, dirs, files in os.walk(str(backup_root/backup_dir)+'_encrypt'):
# 	for file in files:
# 		if file not in '.DS_Store':
# 			with open(Path(root + '/' + file), 'rb') as f:
# 				file_contents = f.read()
# 			encrypted_contents = f_key.encrypt(file_contents)
# 			with open(Path(root + '/' + file), 'wb') as f:
# 				f.write(encrypted_contents)