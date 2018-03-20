# rss_flask
## Get lastest new for 24hrs
* Here's the app
![alt text](https://github.com/kashkama/rss_flask/blob/master/app/static/images/getupto.png "Get uptodate information")
### Contributor
* Owen, 2018

## Instructions
* The app runs on a virtual env to get started type this in the terminal from the root directory.
```bash
$ sudo apt-get install python3.6-venv
$ python3.6 -m venv virtual
$ source virtual/bin/activate
$ deactivate # to deactivate when done with the app
```
* To get started just type this in the termial ``` $ pip install -r requirements.txt``` to install all dependencies.

* Run the app from the **_app_** directory and type this in the terminal ```$ python3.6 views.py```. Open a browser Chrome or Firefox and use the ```localhost:5000```

* The app uses API keys from [openweathermap](https://openweathermap.org/) and [openexchangerates](https://openexchangerates.org), so you have to create accounts to generate keys.
* In the **_app_** directory create an **_instance_** directory and add a **_config.py_** file in the latter directory. The file should store your keys as follows:

_config.py_
```python
WEATHER_API_KEY = "<api-key>"
CURRENCY_API_KEY = "<api-key>"
```
happy coding :-D
