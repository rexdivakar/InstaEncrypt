[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Table of Contents
* [About the tool](#about-the-tool)
  * [Built With](#built-with)
* [Getting started](#getting-started)
  * [Prerequisites](#prerequisites)
  
## About the Tool
This is an Open Source [AES Standard encrytion][0] tool.
<br>
A file for storing the encryption key(s) for file(s)/folder(s) encrypted using the tool is automatically created in the current working directory.
<br>
*Always make sure to backup the encryption key if not the files cannot be reverted back....!!!*

## Built With
* [Python][1]

## Getting Started
To run the tool locally, 
* Clone the repository. For instructions to [clone][2] the repo proceed [here][3].
* Follow these steps on your *OS*
  * *On Linux* : Open the terminal and make sure that the present working directory(folder) is the same as the directory containg the *File_Encryptor.py* file. Check this using the following command
```
pwd
```
It will display the path of the current working directory. To display the files/folders in the working directory use the command
```
ls
```
To execute the program file use the command :
```
python3 File_Encryptor.py
```
### Prerequisites
* Python3<br>
It is preinstalled in Ubuntu 20.04. To check the version use command :
```
python3 --version
```
If it is not preinstalled for some reason, proceed [here][4] and download as per requirement.
* requirements.txt<br>
Run the following command in terminal to download the required packags for running the tool locally : 
```
pip install -r requirements.txt
```

[contributors-shield]: https://img.shields.io/github/contributors/rexdivakar/Fi1e-EncRypt0R.svg?style=flat-square
[contributors-url]: https://github.com/rexdivakar/Fi1e-EncRypt0R/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rexdivakar/Fi1e-EncRypt0R.svg?style=flat-square
[forks-url]: https://github.com/rexdivakar/Fi1e-EncRypt0R/network/members
[stars-shield]: https://img.shields.io/github/stars/rexdivakar/Fi1e-EncRypt0R.svg?style=flat-square
[stars-url]: https://github.com/rexdivakar/Fi1e-EncRypt0R/stargazers
[issues-shield]: https://img.shields.io/github/issues/rexdivakar/Fi1e-EncRypt0R.svg?style=flat-square
[issues-url]: https://github.com/rexdivakar/Fi1e-EncRypt0R/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[0]:https://www.comparitech.com/blog/information-security/what-is-aes-encryption/
[1]:https://www.python.org/
[2]:https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github
[3]:https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[4]:https://www.python.org/downloads/
