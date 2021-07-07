from yafolder import YaFolder

token = ''

if __name__ == '__main__':
    ya = YaFolder(token)
    ya.get_files_list()
    ya.upload_folder('folder76y')
