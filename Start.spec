# -*- mode: python -*-

block_cipher = None


a = Analysis(['Start.py'],
             pathex=['MainWindow.py', 'MainWindowUi.py', 'DirWindow.py', 'DirWindowUi.py', 'FileWindow.py', 'FileWindowUi.py', 'PaintWindow.py', 'PaintWindowUi.py', '/Users/mac/Desktop/git/muse'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += (('compress.png','/Users/mac/Desktop/git/muse/resources/images/compress.png', 'DATA'),
            ('edit.png','/Users/mac/Desktop/git/muse/resources/images/edit.png', 'DATA'),
            ('encrypt.png','/Users/mac/Desktop/git/muse/resources/images/encrypt.png', 'DATA'),
            ('new.png','/Users/mac/Desktop/git/muse/resources/images/new.png', 'DATA'),
            ('open.png','/Users/mac/Desktop/git/muse/resources/images/open.png', 'DATA'),
            ('paint.png','/Users/mac/Desktop/git/muse/resources/images/paint.png', 'DATA'),
            ('quit.png','/Users/mac/Desktop/git/muse/resources/images/quit.png', 'DATA'),
            ('refresh.png','/Users/mac/Desktop/git/muse/resources/images/refresh.png', 'DATA'),
            ('save.png','/Users/mac/Desktop/git/muse/resources/images/save.png', 'DATA'),
            ('save_as.png','/Users/mac/Desktop/git/muse/resources/images/save_as.png', 'DATA'),
            ('setting.png','/Users/mac/Desktop/git/muse/resources/images/setting.png', 'DATA'),
            ('tool.png','/Users/mac/Desktop/git/muse/resources/images/tool.png', 'DATA'),
            ('encrypt.jar','/Users/mac/Desktop/git/muse/resources/jar/encrypt.jar', 'DATA'),
            ('font.json','/Users/mac/Desktop/git/muse/resources/json/font.json', 'DATA'),
            ('setting.json','/Users/mac/Desktop/git/muse/resources/json/setting.json', 'DATA'))
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='Start.app',
             icon=None,
             bundle_identifier=None)
