import pickle

class ReadWrite:
    def __init__(self): pass
    def SearchLine(Path:str, line:str):
        file  = open(Path,"r")
        lines = file.readlines()
        if line in lines:
            file  . close()
            return 0
        else:
            return 1

    def RemoveLine(path:str, target_line):
        with open(path, "r") as file_input:
            with open(path, "w") as output:
                for line in file_input:
                    if line.strip("\n") != target_line:
                        output.write(line)

    def WriteTextData(Path:str, Data:str):
        file  = open(Path,"w")
        file  . write(Data)
        file  . close()

    def AppendTextData(Path:str,Data:str):
        file  = open(Path,"a")
        file  . write(Data)
        file  . close()

    def AppendLineText(Path:str,Data:str):
        file  = open(Path,"a")
        file  . write('\n'+Data)
        file  . close()

    def ReadLines(Path:str):
        file  = open(Path,"r")
        lines = file.readlines()
        file  . close()
        return lines

    def AppendData(Path:str, Data):
        file  = open(Path,"ab")
        pickle. dump(Data,file)
        file  . close()

    def WriteData(Path:str, Data):
        file  = open(Path,"wb")
        pickle. dump(Data,file)
        file  . close()

    def ReadData(Path:str):
        f    = open(Path,"rb")
        data = pickle.load(f)
        f    . close()
        return data
