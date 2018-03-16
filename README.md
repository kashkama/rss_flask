# rss_flask
## Get lastest new for 24hrs
### Contributor
* Owen, 2018

## Instructions
* To get started just type this in the termial ``` $ pip install```
* Run the app from the **_app_** directory and type this in the terminal ```python3.6 views.py```. Open a browser Chrome or Firefox and use the ```localhost:5000```

* The app uses API keys from [openweathermap](https://openweathermap.org/) and [openexchangerates](https://openexchangerates.org), so you have to create accounts to generate keys.
* In the _app_ directory create an _instance_ directory and add a _config.py_ file in the latter directory. The file should store your keys as follows:

_config.py_
```python
WEATHER_API_KEY = "<api-key>"
CURRENCY_API_KEY = "<api-key>"
```
happy coding :-D
