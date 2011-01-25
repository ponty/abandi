from abandi.path import path
import cli4func
import logging

def searchExe(dir, gamename, extensions):
    def exeFilter(name):
        return path(name).ext.lower().strip('.') in extensions

    files = list(path(dir).walkfiles())
    exeList = filter(exeFilter, files)
    return chooseGameExe(exeList, gamename)

def chooseGameExe(exeList, gamename):
    logging.debug("game executables:")
    logging.debug(exeList)

    exe = None
    if len(exeList) == 0   :
        exe = None
    elif len(exeList) ==  1   :
        exe = exeList[0]
    else   :
        newList = excludeSetup(exeList)
        logging.debug("after filter:")
        logging.debug(newList)
        if len(newList) == 1  :
            exe = newList[0]
        else      :
            exe = checkGameName(newList, gamename)
            if not exe:
                def keyFunc1(s):
                    return -len(s)
                #def keyFunc2(s):
                #    return s.lower().replace("exe", "1").replace("com", "2").replace("bat", "3")

                newList.sort(key=keyFunc1)
                #newList.sort(key=keyFunc2)

                logging.debug("after sort:")
                logging.debug(newList)

                logging.debug("choosing first")
                exe = newList[0]

    logging.debug("choosing:")
    logging.debug(exe)

    return exe

def checkGameName(exeList, gamename):
    name = gamename.lower()
    for file in exeList :
        fname = path(file.lower()).stripext().basename()
        if fname in name:
            logging.debug(fname + " found in " + name)
            return file
    return None

EXCLUDE_LIST = "install setup soundset dos4gw help sound reset"

def excludeSetup(exeList):
    #filterDef = EXCLUDE_LIST
    filterList = EXCLUDE_LIST.split(" ")
    newList = []
    for file in exeList:
        ok = True
        for filter in filterList :
            fname = path(file.lower()).stripext().basename()
            if filter in fname:
                ok = False
        if ok:
            newList.append(file)
    return newList

cli4func.main(searchExe)
