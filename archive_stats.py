import os
import json
from utils import PathStats 


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

