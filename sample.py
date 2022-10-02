import os
class Files:
    def get_files(self):
        files = os.listdir('public')
        i = 1
        files_dict = dict()
        for j in files:
            files_dict[i] = j
            i = i+1
        return files_dict


