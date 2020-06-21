## Install Anaconda in window 
Firstly Install [Anaconda](https://docs.anaconda.com/anaconda/install/windows/) into your Machine

## Setting up Code Editor
I perfer, You should use [Visual Studio Code editor](https://code.visualstudio.com/docs/?dv=win32user) and setting up the python development environment by following [link](https://code.visualstudio.com/docs/python/python-tutorial)

## Install kivy
For Installing Kivy follow the [link](https://kivy.org/doc/stable/installation/installation-windows.html)

## Build Project
For Ubuntu user only, Install buildozer into your machine
Command for installing buildozer

 ```
 git clone https://github.com/kivy/buildozer.git
 cd buildozer/
 sudo python3 setup.py install`
```
To initialise project for build go to project directory, type command

```
buildozer init
```

for building, type command

```
buildozer android debug deploy run
```

Note: Java compiler is reqired for building project. To install javac, type command

```
sudo apt install openjdk-8-jdk-headless
```

for check sucessful of javac type

```
javac -version
```
