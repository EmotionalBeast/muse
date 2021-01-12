# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2021/01/12 09:45


import sys
from pathlib import Path

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    bundle_dir = Path(sys._MEIPASS)
else:
    bundle_dir = Path(__file__).parent

#json配置文件位置
FONT_JSON_PATH = str(Path.cwd()/bundle_dir/"resources/json/font.json")
SETTING_JSON_PATH = str(Path.cwd()/bundle_dir/"resources/json/setting.json")

#加密包位置
ENCRYPT_JAR_PATH = str(Path.cwd()/bundle_dir/"resources/jar/encrypt.jar")

#图片位置
NEW_PNG = str(Path.cwd()/bundle_dir/"resources/images/new.png")
EDIT_PNG = str(Path.cwd()/bundle_dir/"resources/images/edit.png")
ENCOM_PNG = str(Path.cwd()/bundle_dir/"resources/images/EnCom.png")
ENCRYPT_PNG = str(Path.cwd()/bundle_dir/"resources/images/encrypt.png")
MV_PNG = str(Path.cwd()/bundle_dir/"resources/images/MV.png")
OPEN_PNG = str(Path.cwd()/bundle_dir/"resources/images/open.png")
PAINT_PNG = str(Path.cwd()/bundle_dir/"resources/images/paint.png")
QUIT_PNG = str(Path.cwd()/bundle_dir/"resources/images/quit.png")
REFRESH_PNG = str(Path.cwd()/bundle_dir/"resources/images/refresh.png")
RESIZE_PNG = str(Path.cwd()/bundle_dir/"resources/images/resize.png")
SAVE_AS_PNG = str(Path.cwd()/bundle_dir/"resources/images/save_as.png")
SAVE_PNG = str(Path.cwd()/bundle_dir/"resources/images/save.png")
SETTING_PNG = str(Path.cwd()/bundle_dir/"resources/images/setting.png")
TOOL_PNG = str(Path.cwd()/bundle_dir/"resources/images/tool.png")