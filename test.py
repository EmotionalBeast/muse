#coding: utf-8
import os, subprocess,json
from pathlib import Path
# def unzip(path):
#     for root,dirs,files in os.walk(path):
#         for file in files:
#             if file[-2:] = "7z":
#                 command = "7z x " + "root" + "/" + "file" + "root" + "/in"
#                 subprocess.call(command, shell=True)
#     print("全部解压完成！")

# def modifyTemplate(path):
#     pathOut = path + "/out"
#     for root, dirs, files in os.walk(pathOut):
#         for file in files:
#             if file = "template.json":
#                 filePath = root + "/" + file
#                     with open(filePath, "r") as f:
#                         jsonStr = f.read()
#                         dict = json.loads(jsonStr, strict = False)
#                     dict["background"] = "FFFFFF"
#                     with open(filePath, "w") as f:
#                         jsonStr = json.dumps(dict, sort_keys=True, indent=2, ensure_ascii=False)
#                         f.write(jsonStr)
#     print("替换完成！")

# def encrypt():
#     command = "java -jar encrypt.jar " + "./in " + "./out"
#     subprocess.call(command, shell=True)
#     print("解密完成！")

                        

if __name__ == "__main__":
    # path = os.path.join(os.getcwd(), "in", "out")
    text = "beat"
    with open("./resources/json/setting.json", "r") as lf:
        jsonStr = lf.read()
        dic = json.loads(jsonStr, strict = False)
    path = os.path.join(Path(dic["directory"]), text, "in")

    print(path)
    # unzip(path)
    # encrypt()
    # modifyTemplate(path)
