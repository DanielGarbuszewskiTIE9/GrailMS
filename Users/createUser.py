def createUser(name):
    import shutil

    src = "C:/GrailMS/defaultData/UserTemp"
    path = f"Users/{name}"

    shutil.copytree(src,path)