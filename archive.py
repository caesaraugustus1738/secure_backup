import shutil
import os
from pathlib import Path
from utils import cur_date_time, PathStats
import json
import encryption


class Archive:
	def __init__(self, source=None, dest=None, format_=None):
		self._source_path = Path(source)
		self._source_parent = Path(source).parents[0]
		self._source_enc = Path(str(self._source_path)+'.enc')
		self._format = format_
		self._dest_parent = Path(dest)
		self._dest_dir = Path(cur_date_time() + '_' + str(self._source_path.name))
		self._dest_path = self._dest_parent.joinpath(Path(self._dest_dir))


	def archive_parent_path(self):
		parent_path = Path(self._dest_parent).joinpath(self._dest_dir)
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
			base_dir = self._source_encrypt.name
			base_name = self._dest_path.joinpath(self._dest_path.name)
		else:
			base_dir = self._source_path
			base_name = self._dest_path.joinpath(self._dest_path.name)

		shutil.make_archive(base_name=base_name, 
							format=self._format,
							root_dir=self._source_parent, 
							base_dir=base_dir)


	def publish(self, secure=False, key=None, toc=True):
		'''One function for various archive types.'''
		os.makedirs(self._dest_path)
		child_dir = self._dest_path.joinpath(self._dest_dir)
		
		if toc is True:
			with open(str(child_dir) + '.json', 'w') as f:
				f.write(self.toc())

		if secure is True:
			self.encrypt(key)
			self.generate_archive(secure=True, key=key)
		else:
			self.generate_archive()


# class ArchiveStats(Archive):
# 	def __init__(self, source=None, dest=None, format_=None):
# 		super().__init__(source, dest, format_)
# 		pass

class ArchiveStats():
	def __init__(self, source):
		self._source_path = source
		pass
		
		
	def tree_stats(self):
		stats = {}
		for root, dirs, files in os.walk(self._source_path):
			for file in files:
				path = root + '/' + file
				stats[path] = PathStats(path).get_stats()

			if not files:
				for dir_ in dirs:
					print(dir_)
					dir_path = root + '/' + dir_
					stats[dir_path] = PathStats(dir_path).get_stats()

		return stats


	def dir_stats(self):
		source_stats = PathStats(self._source_path).get_stats()
		stats = {str(self._source_path): source_stats}
		if secure is True:
			stats['encrypted'] = 'True'
		else:
			stats['encryped'] = 'False'

		return stats


	def toc(self, secure=False):
		'''Table of contents.'''
		source_stats = PathStats(self._source_path).get_stats()
		source = {str(self._source_path): source_stats}
		if secure is True:
			source['encrypted'] = 'True'
		else:
			source['encryped'] = 'False'

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

