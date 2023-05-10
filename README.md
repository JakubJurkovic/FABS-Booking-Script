# Fabs booking script
##### This is a simple python based script to book your gym slot!

- Project discontinued as booking is no longer needed :)

### Version 0.8

# Installation 
#### Requirements
| Libraries | Download |
| ------ | ------ |
| Python | www.python.org |
| Edge Driver | www.developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| Selenium | www.pypi.org/project/selenium/ |
| Pause | www.pypi.org/project/pause/ |

#### Command Line Instructions
Run these commands in your command line **after** installing Python
```sh
pip install selenium
pip install pause
pip install webdriver-manager
```

To update from 0.7 to 0.7.1+, run following
```sh
pip install --upgrade selenium
pip uninstall msedge-selenium-tools
pip install webdriver-manager
```
and possibly check for an update for your Edge Driver

#### Setting up the script
Update the path so it matches the location of where you downloaded Edge Driver
``` python
PATH = "C:\Program Files (x86)\msedgedriver.exe" # Update for your Edge driver
```

And update these according to your credentials and preferences
```python
username = "username" # Your login
password = "password" # Your password
facility = "facility" # "gym" or "pool" or "wogym"
slot = 3 # slot number, indexing starts at 1
```


## License

MIT

**Free Software, Hell Yeah!**
