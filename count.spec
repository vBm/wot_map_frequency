# -*- mode: python -*-

block_cipher = None

added_files = [
     ( 'helpers/maps.json', 'helpers' )
     ]

a = Analysis(['count.py'],
             pathex=['.'],
             binaries=None,
             datas=added_files,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='count',
          debug=False,
          strip=None,
          upx=False,
          console=True, icon='.//images//main.ico')
