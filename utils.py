import time
import os
from stat import S_ISDIR

def cur_date_time():
	return time.strftime('%Y_%m_%d_%H:%M:%S')


class PathStats:
	'''Various stats of a path.'''
	def __init__(self, path):
		self._is_dir = "is_dir"
		self._size = "size"
		self._d_created = "date_created"
		self._d_modified = "date_modified"
		self._path = path

		contents = {}
	

	def get_stats(self):
		stats = self.empty_stats()

		stats[self._size] = self.size(self._path)
		stats[self._d_created] = self.date_created(self._path)
		stats[self._d_modified] = self.date_modified(self._path)
		stats[self._is_dir] = self.dir_check(self._path)

		return stats


	def empty_stats(self):
		stat_keys = [self._is_dir, 
						self._size, 
						self._d_created, 
						self._d_modified]
		stat_dict = {}
		for key in stat_keys:
			stat_dict[key] = ""	

		return stat_dict


	def date_created(self, path):
		'''Date created in yyyy_mm_dd_hh:mm:ss.'''
		stats = os.stat(path)
		return time.strftime("%Y_%m_%d_%H:%M:%S", time.gmtime(stats.st_birthtime))


	def date_modified(self, path):
		'''Date modified in yyyy_mm_dd_hh:mm:ss.'''
		stats = os.stat(path)
		return time.strftime("%Y_%m_%d_%H:%M:%S", time.gmtime(stats.st_mtime))


	def size(self, path):
		'''Size in bytes.'''
		stats = os.stat(path)
		return stats.st_size


	def dir_check(self, path):
		'''Is path a dir.'''
		mode = os.stat(path).st_mode
		if S_ISDIR(mode):
			return "True"
		else:
			return "False"





