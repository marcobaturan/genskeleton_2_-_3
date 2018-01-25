#!/usr/bin/python3.6
# _*_import: utf-8 _*_

import os
import os.path


"""It is a program for meta-programming.

The most simple case of meta-programming is:
A program wich wrote other programs by self-generation
of schematical and skeletal code. And give a good skeletal
structure bassed in good practice. This script try to do this.

"""

def generator_skeleton_program():
    # Static variables.
    extension = ".py"
    documentation = '"""Put here the documentation. TODO:... Follow PEP8. """'
    # Dinamic variables.
    base_path = input("Enter the complete path where place the script: ")
    name_program = input("Enter a name for the program : ")
    author = input("Enter name of author program: ")
    date = input("Enter date in this format,../../....: ")
    # Generate archive.
    name = name_program + extension
    # Locate, put and open archive.
    path_file = os.path.join(base_path, name )
    # Write archive.
    file = open(path_file, "w")
    file.write("#!/usr/bin/env/python3.6" + os.linesep) 
    file.write("# _*_import: utf-8 _*_" + os.linesep)
    file.write("# Please, do not forget try comment and document under pep8." + os.linesep)
    file.write("# https://www.python.org/dev/peps/pep-0008/" + os.linesep) 
    file.write("_author_ = " +"'"+ author+"'" + os.linesep)
    file.write("_date_ = " +"'"+ date +"'"+ os.linesep)
    file.write("# imports" + os.linesep)
    file.write(documentation +"  # Documentation" + os.linesep)
    file.write("# https://devguide.python.org/documenting/ " + os.linesep)
    file.write("# gobal vars" + os.linesep)
    file.write("# class" + os.linesep)
    file.write("#   init function" + os.linesep)
    file.write("#   class inner function" + os.linesep)
    file.write("# heritage class" + os.linesep)
    file.write("#   heritage class functions" + os.linesep)
    file.write('if __name__ == "__main__":' + os.linesep)
    file.write('    # Erase pass and call class or functions here.' + os.linesep)
    file.write('    pass' + os.linesep)
    file.close()
    
if __name__ == "__main__":
    generator_skeleton_program()