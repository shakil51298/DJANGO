"# DJANGO" 

1 => python --version
2 => pip --version
3 => Virtual Environment -=> py -m venv myproject
        myproject 
            Include
            Lib
            Scripts
            pyvenv.cfg
4 => go to this path : myproject\Scripts\activate.bat -- to activate Virtual Environment
5 => NOW INSTALL DJANGO PROJECT
     5.1 => run this command(py -m pip install Django) while Virtual Environment is running
     5.2 => Check Django Version => django-admin --version
     5.3 => My First Project
        Once you have come up with a suitable name for your Django project, like mine: myworld, 
        navigate to where in the file system you want to store the code (in the virtual environment), 
        and run this command in the command prompt: 
            ==> django-admin startproject myworld
6 => Run the Django Project --: py manage.py runserver

7. ==<  Create an app
    7.1 => py manage.py startapp appname