import local_vars
import shutil
import os
from pathlib import Path
from cryptography import fernet


				# Generate a key and write it to a text file
				# key = fernet.Fernet.generate_key()
				# with open('key.txt', 'wb') as f:
				# 	f.write(key)

				# # Read key
				# with open('key.txt', 'rb') as f:
				# 	key = f.read()

				# # Create message
				# with open('message.txt', 'w') as f:
				# 	f.write('My name is George Augustus Tully.')

				# # Read message into memory
				# with open('message.txt') as f:
				# 	msg = f.read()

				# # Convert msg to bytes
				# b_msg = msg.encode()

				# # Plug symmetric private key into Fernet function
				# f_key = fernet.Fernet(key)

				# # Use method of Fernet object to encrypt message
				# encrypted_msg = f_key.encrypt(b_msg)

				# # Decrypt message
				# decrypted_msg = f_key.decrypt(encrypted_msg)


				# print(encrypted_msg, '\n', decrypted_msg)
				# print(decrypted_msg == encrypted_msg)



backup_dest = Path('/Users/georgeaugustustully/Desktop/test_backup/bu_t2.zip')
backup_root = Path('/Users/georgeaugustustully/Documents/coding/projects')
backup_dir = Path('test_backup_proj/')
unpack_dir = Path('/Users/georgeaugustustully/Desktop/test_unpack/')

# print(backup_root/backup_dir)
# print(os.getcwd())
# os.chdir(backup_root/backup_dir)
# print(os.getcwd())

cwd = Path(os.getcwd())
print('cwd -', cwd)
parent_dir = cwd.parent

backup_dir_temp = Path(backup_root/backup_dir)



# Copy dir to back up
try:
	shutil.copytree(src=backup_root/backup_dir, dst=str(backup_root/backup_dir)+'_encrypt')
except FileExistsError:
	pass

with open('key.txt') as f:
	key = f.read().encode()

f_key = fernet.Fernet(key)

for root, dirs, files in os.walk(str(backup_root/backup_dir)+'_encrypt'):
	for file in files:
		if file not in '.DS_Store':
			with open(file, 'rb') as f:
				file_contents = f.read()
			encrypted_contents = f_key.encrypt(file_contents)
			with open(file, 'wb') as f:
				f.write(encrypted_contents)
			# with open(root + '/' + file) as f:
			# 	print(f.read())
		# print(root + '/' + file)

# Perform archive
# shutil.make_archive(base_name=backup_dest, format='zip',
# 	root_dir=root_dir, base_dir='tfl_updates/')

# Unpack the archive
# shutil.unpack_archive(filename=backup_dest, extract_dir=unpack_dir, format='zip')

















