# horse-racing-prediction
Horse racing prediction using machine learning mechanics and betting strategies.



# Set Up

on linux:
```python
python3 -m venv venv
source venv/bin/activate
pip install -r requirement.txt
```

in .env:
```
TARGET_URL=<target url>
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
