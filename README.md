2020/02/25:
1、静态素材图片增加filter字段，rotation字段。（滤镜和旋转角度）
	rotation: 顺时针旋转 -180到180,使用角度

2、动态素材文字增加textSpacing, lineSpacing, angle, startFrame(开始帧), sourcePath, type : animation_text

3、静态素材文字增加textSpacing, lineSpacing, angle

4、version: "1.1"

5、静态素材滤镜：
	filter: 滤镜名字
	filterStrength:0 ～ 100

	textSpacing公式:	蓝湖值 / 100
	lineSpacing公式: 当前值 / 默认值（自动）默认为1

2020/03/09
1、加入新增字段
2、自动获取生成动效素材目录
3、mv素材的生成加密，压缩
4、UI布局，重构构思

Homebrew安装：
/bin/zsh -c "$(curl -fsSL https://gitee.com/cukai/HomebrewCN/raw/master/Hombrew.sh)"

相关库：
PyQt5 shutil pillow json 

2020/04/21
1、汉化
2、对齐方式

2020/05/07
1、自由添加删除表格一行数据
2、背景有颜色值（16进制RGB）
3、"background_line_color": "",


打包：
使用pyinstaller打包

	1、终端进入项目文件假
	2、执行命令（--add-data 加入资源文件夹，-F 指定启动文件位置 -w 无黑窗log， -i 指定图片文件）
	pyinstaller --add-data="resources:resources" -F -w -i ./Muse.icns ./Muse.py
	
	3、清空上次打包缓存
		删除build dist文件夹
		删除Muse.spec文件夹

7z 切换(mac 默认配置，不必更改)

	windows环境下：
		MainWindow.py 1302行的 MAC_7z 改为 WIN_7z
