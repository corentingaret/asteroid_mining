# Data mining of asteroids data
- Description: Estimate the total quantity of resources available in accessible asteroids
- Data Source: 
    JPL database: https://ssd.jpl.nasa.gov/sbdb_query.cgi#x
    Asterank complete database named asterank: https://github.com/typpo/asterank
    CNEOS accessible asteroids database: https://cneos.jpl.nasa.gov/nhats/

- My objective was to determine the total quantity in kg of different resources in accessible asteroids, after being inspired by the asterank project availbale on GitHub.
- I estimate the mass of each accessible asteroid and compute the quantity of resources from the asteroid' spectral classification.  

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

# Install

Go to `https://github.com/{group}/asteroid_mining` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/asteroid_mining.git
cd asteroid_mining
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
asteroid_mining-run
```
