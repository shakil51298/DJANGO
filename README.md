"# DJANGO" 

## ==> check python version :
		python --version
###### or
		python3 --version
## ==> check pip version :
		pip --version
## ==> Virtual Environment: 
		py -m venv myproject 
##### or
		python3 -m venv myproject 	
#### folder structure: 
        myproject 
            Include
            Lib
            Scripts
            pyvenv.cfg
## ==> go to this path : myproject\Scripts\activate.bat -- to activate Virtual Environment.
## ==> NOW INSTALL DJANGO PROJECT :
####     5.1 ==> run this command() while Virtual Environment is running :
			py -m pip install Django
###### or
			python3 -m pip install Django
####     5.2 ==> Check Django Version => 
			django-admin --version
####     5.3 ==> My First Project :
        Once you have come up with a suitable name for your Django project, like mine: myworld, 
        navigate to where in the file system you want to store the code (in the virtual environment), 
        and run this command in the command prompt: 
####    ==> Create project :
		django-admin startproject myworld
#### ==> Run the Django server:
		py manage.py runserver
##### or
		python manage.py runserver

## ==> Create an app : 
    	py manage.py startapp appname
##### or
		python3 manage.py startapp appname
    
