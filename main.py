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


    return MainPath,subPath,_sub_sub_path


def sorting_array():
    MainPath,subPath,_sub_sub_path = skeleton_created()

    sorting_main = sort_array_main(MainPath)
    sorting_sub = sort_array_sub(subPath)
    sorting_sub_sub = sort_array_sub_sub(_sub_sub_path)

    return sorting_main,sorting_sub,sorting_sub_sub

def sort_array_main(main):
    _t = []
    for i in range(len(main)):
        _t.append(str(main[i]).split("/")[-1])
    Folder_name = _t
    return Folder_name
def sort_array_sub(sub):
    arr = []
    for i in range(len(sub)):
        _t = []
        for i2 in range(len(sub[i])):
            _t.append(str(sub[i][i2]).split("/")[-1])
        arr.append(_t)
    return arr

def sort_array_sub_sub(subsub):
    arr = []
    for i in range(len(subsub)):
        _t = []
        for i2 in range(len(subsub[i])):
            _t.append(str(subsub[i][i2]).split("/")[-1])
        arr.append(_t)
    return arr

def sort_subsub_for_sub(subsub,lensub,inter):
    subsubforsub = []

    for i in range(lensub):
        subsubforsub.append(subsub[i+inter])

    return subsubforsub

def CreatingADictionaryBasedOnSkeletonSorting():
    main,sub,subsub = sorting_array()
    dict_main = {}
    dict_main = add_dict_main(dict_main,main,sub,subsub)
    print(dict_main)

def add_dict_main(dict_main,main,sub,subsub):
    sub_main = add_dict_sub_main(sub,subsub)
    dict_main = dict.fromkeys(main,sub_main)

    return dict_main
def add_dict_sub_main(sub,subsub):
    submain={}
    for i in range(len(sub)):
        for i2 in range(len(sub[i])):
            submain[str(sub[i][i2])] = subsub[i2]


    return submain


CreatingADictionaryBasedOnSkeletonSorting()