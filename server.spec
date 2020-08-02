# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['server.py'],
             pathex=['D:\\project\\python3\\hpCfd'],
             binaries=[
                 ('.\\exec\\main.exe', 'exec'),
                 ('.\\exec\\grid_check.exe', 'exec'),
                 ('.\\exec\\Inlet_nonUniform_check.exe', 'exec'),
                 ('.\\venv\\Lib\\site-packages\\flask_migrate\\templates\\flask\\alembic.ini.mako', 'flask_migrate\\templates\\flask'),
                 ('.\\venv\\Lib\\site-packages\\flask_migrate\\templates\\flask\\env.py', 'flask_migrate\\templates\\flask'),
                 ('.\\venv\\Lib\\site-packages\\flask_migrate\\templates\\flask\\README', 'flask_migrate\\templates\\flask'),
                 ('.\\venv\\Lib\\site-packages\\flask_migrate\\templates\\flask\\script.py.mako', 'flask_migrate\\templates\\flask'),
             ],
             datas=[],
             hiddenimports=['logging.config'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='server',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='logo.ico')
