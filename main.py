import os

path_test = "/home/drawmang/disk-z/DigitRock Models Backup"


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def skeleton_created():
    MainPath = get_subfolder_paths(path_test)
    subPath = []
    _sub_sub_path = []

    for i in range(len(MainPath)):
        subPath.append(get_subfolder_paths(MainPath[i]))

        for i2 in range(len(subPath[i])):
            _sub_sub_path.append(get_subfolder_paths(subPath[i][i2]))
        _sub_sub_path.remove(_sub_sub_path[i])

    return MainPath,subPath,_sub_sub_path


def sorting_array():
    MainPath,subPath,_sub_sub_path = skeleton_created()
    print(_sub_sub_path)
    sorting_main = sort_array_main(MainPath)
    sorting_sub = sort_array_sub(subPath)
    sorting_sub_sub = sort_array_sub_sub(_sub_sub_path)
    print(sorting_sub_sub)
    print("-----")
    print(sorting_main[0])
    print(sorting_sub[0])
    print(sorting_sub_sub[0],sorting_sub_sub[1])

def sort_array_main(main):
    _t = []
    for i in range(len(main)):
        _t.append(str(main[i]).split("/")[-1])
    Folder_name = _t
    return Folder_name
def sort_array_sub(sub):
    arr=[]
    _t = []
    for i in range(len(sub)):
        _t = []
        for i2 in range(len(sub[i])):
            _t.append(str(sub[i][i2]).split("/")[-1])
        arr.append(_t)
    return arr

def sort_array_sub_sub(subsub):
    arr = []
    _t = []
    for i in range(len(subsub)):
        _t = []
        for i2 in range(len(subsub[i])):
            _t.append(str(subsub[i][i2]).split("/")[-1])
        arr.append(_t)
    return arr


sorting_array()


