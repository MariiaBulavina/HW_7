from setuptools import setup, find_namespace_packages


setup(name='clean_folder',
      version='0.0.1',
      entry_points={'console_scripts':['clean_folder=clean_folder.sort:main']}
      )