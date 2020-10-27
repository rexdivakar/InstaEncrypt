from setuptools import setup, find_packages
from os import path
import os.path

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

# Get the long description from the README file
with open("README.md", encoding="utf-8") as f:
    read_file = f.read()
    
with open("requirements.txt", encoding="utf-8") as f:
    req_file = f.read().split('\n')   

 
setup(
  name='InstaEncrypt',
  version='1.0',
  description='Instantly Encrypts ur file',
  long_description=read_file,
  long_description_content_type='text/markdown',
  url='https://github.com/rexdivakar/Fi1e-EncRypt0R',  
  author='Sanchit Jain, Divakar R',
  author_email='sanchitjain1996@gmail.com, rexdivakar@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='AES Encryption System', 
  packages=['InstaEncrypt'],
  install_requires=req_file
)