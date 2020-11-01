from setuptools import setup, find_packages
 
setup(name='algorith',
      version='0.0.2',
      url='https://github.com/ryu577/algorithms',
      license='MIT',
      author='Rohit Pandey',
      author_email='rohitpandey576@gmail.com',
      description='Add static script_dir() method to Path',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)

