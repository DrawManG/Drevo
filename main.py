import os
from sys import platform




class type_2():
    def pather():
        if platform == "linux" or platform == "linux2":
            DirPath = "/home/drawmang/disk-z/DigitRock Models Backup/"
        elif platform == "win32":
            DirPath = "Z:\\DigitRock Models Backup\\"
        return DirPath
    DirPath = pather()

    def search_folders(path,index):
        msv = []
        realmsv = []
        if index == 1:
            obj = os.scandir(path)
            for entry in obj:
                if entry.is_dir() or entry.is_file():
                    msv.append(entry.name)
            realmsv.append(msv)
            return realmsv
        if index == 0:
            obj = os.scandir(path)
            for entry in obj:
                if entry.is_dir() or entry.is_file():
                    msv.append(entry.name)
            return msv

    def join():
        DirPath = type_2.DirPath
        #lvl1 = type_2.search_folders(DirPath,0)

        #i1 = 0
        #i2 = 0
        #lvl2 = []
        #lvl3 = []

        #while i1 < (len(lvl1)):
        #    type = type_2.search_folders(DirPath + lvl1[i1],1)
        #    for i in range(len(type)):
        #        lvl2.append(type[i])
        #        print(DirPath+lvl1[i1]+"/"+lvl2[i1][i2])
        #    i1+=1

        type_2.list_files(DirPath)

    def list_files(startpath):
        import os
        base = []
        lvl3 = {}
        os.chdir(startpath)
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                #print(os.path.join(root, name))
                pass
            for name in dirs:
                base.append(os.path.join(root, name))
        for i in range(len(base)):

            now_data = base[i]
            now_del = now_data.count('/')
            #if now_del == 1:
            #    print(base[i])
            #if now_del == 2:
            #    print(base[i])
            if now_del == 3:
                real_base = base[i].replace("./","")
                try:
                    lvl3[real_base.split("/")[0]] += "/"+ real_base.split("/")[1]

                except:
                    lvl3[real_base.split("/")[0]] = real_base.split("/")[1]
        print(lvl3)











type_2.join()

class DictForQTreeView():
    global DirPath, TakeSubfolders, BuildingAnArraySkeleton, SortingAnArray, Sorting_1lvl_main, Sorting_2lvl_Sub, Sorting_3lvl_SubSub, CreatingTheFinalDictionary, CreatingADictionaryForTheFinalDictionary
    def pather():
        if platform == "linux" or platform == "linux2":
            DirPath = "/home/drawmang/disk-z/DigitRock Models Backup/"
        elif platform == "win32":
            DirPath = "Z:\\DigitRock Models Backup\\"
        return DirPath

    DirPath = pather()

    def TakeSubfolders(folder_path) -> list:


        LVLmain = [f.path for f in os.scandir(folder_path) if f.is_dir()]

        return LVLmain

    def BuildingAnArraySkeleton():

        Dir_1lvl_main = TakeSubfolders(DirPath)
        Dir_2lvl_sub = []
        Dir_3lvl_subsub = []

        for i in range(len(Dir_1lvl_main)):
            Dir_2lvl_sub.append(TakeSubfolders(Dir_1lvl_main[0]))


            for i2 in range(len(Dir_2lvl_sub[i])):
                Dir_3lvl_subsub.append(TakeSubfolders(Dir_2lvl_sub[i][i2]))

        return Dir_1lvl_main, Dir_2lvl_sub, Dir_3lvl_subsub

    def SortingAnArray():
        MainPath, Sub_path, Subsub_path = BuildingAnArraySkeleton()

        sorting_main = Sorting_1lvl_main(MainPath)
        sorting_sub = Sorting_2lvl_Sub(Sub_path)
        sorting_sub_sub = Sorting_3lvl_SubSub(Subsub_path)

        return sorting_main, sorting_sub, sorting_sub_sub

    def Sorting_1lvl_main(main):
        temp = []

        for i in range(len(main)):
            if platform == "linux" or platform == "linux2":
                temp.append(str(main[i]).split("/")[-1])
            elif platform == "win32":
                temp.append(str(main[i]).split("\\")[-1])

        Folder_name = temp

        return Folder_name

    def Sorting_2lvl_Sub(sub):
        arr = []

        for i in range(len(sub)):
            temp = []
            for i2 in range(len(sub[i])):
                if platform == "linux" or platform == "linux2":
                    temp.append(str(sub[i][i2]).split("/")[-1])
                elif platform == "win32":
                    temp.append(str(sub[i][i2]).split("\\")[-1])
            arr.append(temp)

        return arr

    def Sorting_3lvl_SubSub(subsub):
        arr_subsub = []

        for i in range(len(subsub)):
            temp = []
            for i2 in range(len(subsub[i])):
                if platform == "linux" or platform == "linux2":
                    temp.append(str(subsub[i][i2]).split("/")[-1])
                elif platform == "win32":
                    temp.append(str(subsub[i][i2]).split("\\")[-1])
            arr_subsub.append(temp)

        return arr_subsub

    def SortingSubsubForSub(subsub, lensub, inter):
        subsub_for_sub = []

        for i in range(lensub):
            subsub_for_sub.append(subsub[i + inter])

        return subsub_for_sub

    def CreatingADictionaryBasedOnSkeletonSorting():
        main, sub, subsub = SortingAnArray()
        dict_main = CreatingTheFinalDictionary(dict_main={}, main=main, sub=sub, subsub=subsub)
        print(dict_main)
        return dict_main

    def CreatingTheFinalDictionary(dict_main, main, sub, subsub,):
        sub_main = CreatingADictionaryForTheFinalDictionary(sub, subsub)
        dict_main = dict.fromkeys(main, sub_main)

        return dict_main

    def CreatingADictionaryForTheFinalDictionary(sub, subsub):
        submain = {}
        for i in range(len(sub)):
            for i2 in range(len(sub[i])):
                submain[str(sub[i][i2])] = subsub[i2]

        return submain


#DictForQTreeView.CreatingADictionaryBasedOnSkeletonSorting()