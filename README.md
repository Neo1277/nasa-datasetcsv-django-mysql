# Planetary systems #

This Django application loads a nasa planetary systems dataset in csv format taken from [NASA’s Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/index.html "nasa") into a MySQL database. Notice that I added three columns related to the Star name when downloading the csv file from NASA’s Exoplanet Archive. The csv file is provided in this repository, the file name is: PS_2021.01.08_12.13.30.csv

## Installation ##
*   First create a MySQL database named "planetary_systems" 
*   To connect the Django application with the MySQL database, go to the settings.py file, which is located in the directory nasa_datasetcsv_django_mysql/nasa_datasetcsv_django_mysql and in DATABASES dictionary, configurate the cretentials, host and so on.
*   Create a virtual enviroment for the django dependencies [Link official documentation](https://docs.djangoproject.com/en/3.1/intro/contributing/#getting-a-copy-of-django-s-development-version "djangoenviroment")
*   Activate the enviroment and go to the backend_django folder and install the Django dependencies with the following command using the requirements.txt file which has the dependencies
	* ### `pip install -r requirements.txt`
*   To create the tables on the database, on the nasa_datasetcsv_django_mysql folder run the following commands (python or python3 depends on your configuration when the enviroment variable on the system was set up)
	* ### `python manage.py makemigrations`
	* ### `python manage.py migrate`
*   To load the csv dataset into the MySQL database, go to the nasa_datasetcsv_django_mysql folder and run
	* ### `python manage.py runscript many_load`

## How to run it ##
*   Go to the nasa_datasetcsv_django_mysql folder and run
	* ### `python manage.py runserver`