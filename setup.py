import sys
try:
    import py2exe
except:
    raw_input('Please install py2exe first...')
    sys.exit(-1)

from distutils.core import setup

sys.argv.append('py2exe')

setup(
    options={
        'py2exe': {'bundle_files': 1, 'compressed': True}
    },
    console=[{
        'script': "count.py"
    }],
    zipfile=None,
)