import os

def compare_dir_layout(dir1, dir2):
    print('files in "' + dir2 + '" but not in "' + dir1 + '"')
    for (dirpath, dirnames, filenames) in os.walk(dir1):
        for filename in filenames:
            relative_path = dirpath.replace(dir1, "")
            if os.path.exists( dir2 + relative_path + '\\' +  filename) == False:
                print(relative_path, filename)
    return

compare_dir_layout('Control', 'AdBlock')