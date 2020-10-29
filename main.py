# import local_vars
from pathlib import Path
import archive as arch
from pprint import pprint as pp
import os


# Retreive key
with open('key.txt') as f:
	key = f.read().encode()


# Create Archive object
arch = arch.Archive(source='/Users/georgeaugustustully/Documents/coding/projects/test_backup_proj',
					dest='/Users/georgeaugustustully/Library/Mobile Documents/com~apple~CloudDocs/backup/',
					format_= 'zip')

# Create unsecure archive
arch.unsecure_archive()

# Create secure archive
# arch.secure_archive(key)




















