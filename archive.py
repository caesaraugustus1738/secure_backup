import local_vars
import shutil
import os
from pathlib import Path
from secure_backup_utils import cur_date_time, PathStats
import json
import encryption

# print(Path(__file__).suffix)


class Archive:
	def __init__(self, source=None, dest=None, format_=None):
		self._source_path = Path(source)
		self._source_dir = Path(source).name
		self._source_parent = Path(source).parents[0]
		self._source_encrypt = Path(str(self._source_path)+'_encrpyt')
		self._format = format_
		self._dest_parent = Path(dest)
		self._dest_dir = cur_date_time() + '_' + str(self._source_dir)
		self._dest_path = self._dest_parent.joinpath(Path(self._dest_dir))


	def archive_parent_path(self):
		parent_path = Path(self._dest_parent).joinpath(self._dest_dir)
		return parent_path


	def make_encrypted_copy(self, key):
		'''Make encrypted copy of dir.
		'''

		# Copy source dir
		shutil.copytree(self._source_path, self._source_encrypt)

		# # Walk and encrypt
		for root, dirs, files in os.walk(self._source_encrypt):
			for file in files:
				if file not in '.DS_Store':
					file_path = root + '/' + file
					encryption.file_encrypter(file_path, key)


	def toc(self):
		'''Table of contents.'''
		source_stats = PathStats(self._source_path).get_stats()
		source = {str(self._source_path): source_stats}
		all_files = {}

		for root, dirs, files in os.walk(self._source_path):
			for file in files:
				path = root + '/' + file
				all_files[path] = PathStats(path).get_stats()

			if not files:
				for dir_ in dirs:
					dir_path = root + '/' + dir_
					all_files[dir_path] = PathStats(dir_path).get_stats()

		toc = {'archive_source': source, 'archive_contents': all_files}

		return json.dumps(toc, indent=2)


	def unsecure_archive(self):
		os.makedirs(self._dest_path)
		os.chdir(self._source_path)

		shutil.make_archive(base_name=self._dest_path.joinpath(self._dest_dir), 
							format=self._format,
							root_dir=self._source_parent, 
							base_dir=self._source_dir)

		
		os.chdir(self._dest_path)

		with open(self._dest_dir + '.json', 'w') as f:
			f.write(self.toc())
	

	def secure_archive(self, key):
		self.go_to_parent_dir()
		self.make_encrypted_copy(key)

		shutil.make_archive(base_name=self._dest, 
							format=self._format,
							root_dir=self._source_parent, 
							base_dir=self._source_encrypt.name)

		os.chdir(self._dest_path)

		with open(self._dest_dir + '.json', 'w') as f:
			f.write(self.toc())
			
		shutil.rmtree(self._source_encrypt)