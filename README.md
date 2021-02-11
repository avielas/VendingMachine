This project holds the training material required for the 'Basic Python' course that is provided to Intel employees,
through http://goto/saba.

It is a 1 day frontal workshop that walks through
[this presentation](docs/_static/Basic%20Python%20-%202018.pptx),
pausing at the end of each chapter to allow for students to perform the related exercises provided by this project.


Course prerequisites:

- [x] Install *Python* from https://www.python.org
    - Recommended version https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe
    - If you insist on python 2.7 then use https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi
- [x] Install *GIT*:

    1. [x] search in a web browser for "git install" or try out https://git-scm.com/downloads.
    2. [x] Download the version matching your OS and run the installer.
           Accepting all the proposed options is generally a good choice.

- [x] Install this project in 'editable mode' - by using this [code-dos[built-in script][InstallScript]] [^1]
  [ ] Install <file:///docs/_static/basic_python.bat>
- [x] Install *PyCharm* from https://www.jetbrains.com/pycharm.
      The [Educational Version](https://www.jetbrains.com/education/download/#section=pycharm-edu) 
      is free and highly recommended. [^2]

--------------------------------------

[^1]: You can also install this package manually by running from the command line:  
      ```
      py -3.6 -m pip install -e git+https://gitlab.devtools.intel.com/python_training/basic_python.git#egg=basic_python --src C:\Projects
      ```

[^2]: If you already have *PyCharm* installed then you can upgrade to the educational version simply by 
      [installing the EduTools plugin](https://www.jetbrains.com/help/education/install-edutools-plugin.html?section=PyCharm).
      However, this might not be accessible when connected through Intel's VPN.
      Please disconnect the VPN for installing the plugin and then reconnect.



[InstallScript]: docs/_static/basic_python.bat