# Fabs booking script
##### This is a simple python based script to book your gym slot!

# Installation 
#### Requirements
| Libraries | Download |
| ------ | ------ |
| Python | www.python.org |
| Edge Driver | www.developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| Selenium | www.pypi.org/project/selenium/ |
| Edge Tools | www.pypi.org/project/msedge-selenium-tools/ |
| Pause | www.pypi.org/project/pause/ |

#### Command Line Instructions
Run these commands in your command line **after** installing Python
```sh
pip install selenium
pip install msedge-selenium-tools
pip install pause
```

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
