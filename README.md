# horse-racing-prediction
Horse racing prediction using machine learning mechanics and betting strategies.

## Data Consolidation Pipeline
We are analyzing horse racing, in our case we want the final data to be every attempt of every horse in every race.
Therefore we'll first fetch all the race results that took place in the last 15 years (11k). For each race, there will be 8-13 horses.
Take their results, combine with that race's background information (what's the course like, wet or dry, length of race..)
Finally for each data point we would also like to know the horse's stats. Therefore we'll have to crawl for the performance of the horse as well.
Finally combining them all together into a super dataset


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
