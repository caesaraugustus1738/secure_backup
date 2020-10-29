from cryptography import fernet


def file_encrypter(file, key):
	'''Encrypts single file with symmetrical Fernet encryption.
	'''
	with open(file, 'rb') as f:
		file_contents = f.read()

	f_key = fernet.Fernet(key)
	encrypted_contents = f_key.encrypt(file_contents)

	with open(file, 'wb') as f:
		f.write(encrypted_contents)