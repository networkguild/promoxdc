# proxmoxdc
### Requirements
* Python 3.10
* Pip

### Install pipenv, needed packages and create virtual env
* pip install pipenv
* pipenv install

### Install packages only in dev environment
* pipenv install --dev

### Lauch virtual env
* pipenv shell

### Run one command from virtual env
* pipenv run python src/main.py

### How to get container data
* Add USERNAME and PASSWORD environment variables
```
export PASSWORD=password
export USERNAME=username
```
* Get config
```
python src/lxc-proxy.py -g -i hosts.ini
```
* Get stats
```
python src/lxc-proxy.py -gs -i hosts.ini
```
