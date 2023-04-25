# 44. Write a Python program to locate Python site-packages.

import site; 
print(site.getsitepackages())

# what are site packages in python and what do they do?
# site-packages is the target directory of manually built Python packages. 
# When you build and install Python packages from source 
# (using distutils, probably by executing python setup.py install), 
# you will find the installed modules in site-packages by default.
# what is its relevance to pip install?

# There are standard locations:

# Unix (pure)1: prefix/lib/pythonX.Y/site-packages
# Unix (non-pure): exec-prefix/lib/pythonX.Y/site-packages
# Windows: prefix\Lib\site-packages
# 1 Pure means that the module uses only Python code. Non-pure can contain C/C++ code as well.
# site-packages is by default part of the Python search path, so modules installed there can be imported easily afterwards.
# https://stackoverflow.com/questions/31384639/what-is-pythons-site-packages-directory#:~:text=site%2Dpackages%20is%20the%20target,in%20site%2Dpackages%20by%20default.