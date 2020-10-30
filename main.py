import archive as archive


# Retreive key
with open('key.txt') as f:
	key = f.read().encode()


# Create Archive object
backup = archive.Archive(source='/Users/georgeaugustustully/Documents/coding/projects/test_backup_proj',
					dest='/Users/georgeaugustustully/Library/Mobile Documents/com~apple~CloudDocs/backup/',
					format_= 'zip')

stats = archive.ArchiveStats(source='/Users/georgeaugustustully/Documents/coding/projects/test_backup_proj')

# backup_stats = 

print(backup._source_path)
print(stats._source_path)


# Create unsecure archive
# archive.publish()

# Create secure archive
# arch.secure_archive(key)




















