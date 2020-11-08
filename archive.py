import shutil
import os
from pathlib import Path
from utils import cur_date_time
import encryption
import archive_stats


class Archive:
	def __init__(self, source=None, dest=None, format_=None):
		self._source_path = Path(source)
		self._source_parent = Path(source).parents[0]
		self._source_enc = Path(str(self._source_path)+'.enc')
		self._format = format_
		self._dest_parent = Path(dest)
		self._dest_dir_name = Path(cur_date_time() + '_' + str(self._source_path.name))
		self._dest_path = self._dest_parent.joinpath(Path(self._dest_dir_name))


	def archive_parent_path(self):
		parent_path = Path(self._dest_parent).joinpath(self._dest_dir_name)
		return parent_path


	def encrypt(self, key):
		'''Make encrypted copy of dir.
		'''
		shutil.copytree(self._source_path, self._source_enc)

		for root, dirs, files in os.walk(self._source_enc):
			for file in files:
				if file not in '.DS_Store':
					file_path = root + '/' + file
					encryption.file_encrypter(file_path, key)


	def generate_archive(self, secure=False):
		if secure is True:
			base_dir = self._source_enc.name
		else:
			base_dir = self._source_path
		
		shutil.make_archive(base_name=self._dest_path.joinpath(self._dest_path.name), 
							format=self._format,
							root_dir=self._source_parent, 
							base_dir=base_dir)

		try:
			shutil.rmtree(self._source_enc)
		except FileNotFoundError:
			pass


	def key_file(self, key, path):
		with open(str(path) + '_key.txt', 'w') as f:
			f.write(key)


	def publish(self, key=None, toc=True):
		'''One function for various archive types.'''
		os.makedirs(self._dest_path)
		child_dir = self._dest_path.joinpath(self._dest_dir_name)
		
		if toc is True:
			stats = archive_stats.ArchiveStats(self._source_path)
			with open(str(child_dir) + '.json', 'w') as f:
				f.write(stats.toc())

		if key:
			self.key_file(key=key, path=child_dir)
			self.encrypt(key)
			self.generate_archive(secure=True)
		else:
			self.generate_archive()

