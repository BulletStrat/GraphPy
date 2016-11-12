# -*- mode: python -*-

block_cipher = None


a = Analysis(['UserInterface.py'],
             pathex=['E:\\Programming-Python\\PycharmProjects\\ProjectSilver'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='UserInterface',
          debug=False,
          strip=False,
          upx=True,
          console=False , version='version.txt', icon='app.ico')
