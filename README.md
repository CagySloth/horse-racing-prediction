# horse-racing-prediction
Horse racing prediction using machine learning mechanics and betting strategies.



# Set Up

on linux:
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirement.txt
```

on windows:
```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

in .env:
```
TARGET_URL=http://101.78.205.36/racing/information/Chinese/Racing/LocalResults.aspx
RESULTS_FOLDER=results/
```

# Development

## Linting
After you code, before you push you should lint your code to keep the formatting readable and consistent
This command will automatically format your scripts. which is good enough
```bash
sh script/lint.sh --in-place
```
if you want extra formatting suggestions:
```bash
sh script/lint.sh
```
