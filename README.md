# horse-racing-prediction
Horse racing prediction using machine learning mechanics and betting strategies.

## Data Consolidation Pipeline
We are analyzing horse racing, in our case we want the final data to be every attempt of every horse in every race.
Therefore we'll first fetch all the race results that took place in the last 15 years (11k). For each race, there will be 8-13 horses.
Take their results, combine with that race's background information (what's the course like, wet or dry, length of race..)
Finally for each data point we would also like to know the horse's stats. Therefore we'll have to crawl for the performance of the horse as well.
Finally combining them all together into a super dataset

## Final Dataset Description

The final dataset 78320 generated by the GitHub scraper contains detailed information about horse races over the last 15 yeras. Below is a description of each column included in the dataset:

| Column Name        | Description                                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------------------|
| `Position`         | The finishing position of the horse in the race.                                                            |
| `HorseNumber`      | The number assigned to the horse for the race.                                                              |
| `HorseName`        | The name of the horse, including its identifier in parentheses.                                             |
| `Jockey`           | The name of the jockey who rode the horse.                                                                  |
| `Trainer`          | The name of the horse's trainer.                                                                            |
| `ActWeightIncr`    | The actual weight increment of the horse, adding the weight of jockey and equipments.                       |
| `HorseWeight`      | The weight of the horse.                                                                                    |
| `GatePosition`     | The starting gate position of the horse.                                                                    |
| `WinningMargin`    | The distance by which the horse won, if applicable.                                                         |
| `FinishTime`       | The time it took for the horse to finish the race.                                                          |
| `WinOdds`          | The bet of the horse.                                                                                       |
| `Contenders`       | The total number of contenders in the race.                                                                 |
| `URL`              | A URL linking to additional information about the horse.                                                    |
| `Distance`         | The distance of the race, measured in meters.                                                               |
| `CourseState`      | The condition of the racecourse during the race.                                                            |
| `Course`           | The type and specific track of the racecourse.                                                              |
| `PrizeMoney`       | The total prize money the horse has won.                                                                    |
| `Rating`           | The official rating of the horse.                                                                           |
| `Gold`             | The number of first-place finishes the horse has achieved.                                                  |
| `Silver`           | The number of second-place finishes the horse has achieved.                                                 |
| `Bronze`           | The number of third-place finishes the horse has achieved.                                                  |
| `TotalMatches`     | The total number of races the horse has participated in.                                                    |
| `WinRate`          | The win rate of the horse, calculated as the number of wins divided by the total number of races.           |
| `BirthPlace`       | The birthplace of the horse.                                                                                |

### Example Data

Below is a sample of the dataset for illustration purposes:

| Position | HorseNumber | HorseName | Jockey | Trainer | ActWeightIncr | HorseWeight | GatePosition | WinningMargin | FinishTime | WinOdds | Contenders | URL | Distance | CourseState | Course | PrizeMoney | Rating | Gold | Silver | Bronze | TotalMatches | WinRate | BirthPlace |
|----------|-------------|-----------|--------|---------|----------------|-------------|--------------|----------------|-------------|---------|------------|-----|----------|-------------|--------|-------------|--------|------|--------|--------|---------------|---------|------------|
| 1        | 11.0        | 我跑得 (CJ031) | 鄭雨滇   | 何良      | 114            | 981         | 10           | -              | 1:40.77  | 2.7     | 12         | /racing/information/Chinese/Horse/Horse.aspx?HorseId=HK_2007_J031 | 1650     | 好地          | 草地 - "A" 賽道 | 1407400.0   | 12.0   | 2.0  | 6.0    | 3.0    | 36.0          | 0.3056  | 紐西蘭    |
| 2        | 8.0         | 名利好 (CH144) | 都爾     | 胡森      | 121            | 956         | 9            | 頸位            | 1:40.84  | 12.0    | 12         | /racing/information/Chinese/Horse/Horse.aspx?HorseId=HK_2006_H144 | 1650     | 好地          | 草地 - "A" 賽道 | 457200.0    | 28.0   | 0.0  | 2.0    | 2.0    | 24.0          | 0.1667  | 英國      |
| 3        | 6.0         | 龍子 (CJ204) | 韋達     | 霍利時    | 125            | 1009        | 6            | 2              | 1:41.08  | 4.5     | 12         | /racing/information/Chinese/Horse/Horse.aspx?HorseId=HK_2007_J204 | 1650     | 好地          | 草地 - "A" 賽道 | 1000238.0   | 20.0   | 2.0  | 0.0    | 5.0    | 36.0          | 0.1944  | 紐西蘭    |

# Dataset Visualization
After data processing and removing the unncessary / missing fields, this are the findings we get:
![Birthplace](images/birthplaces.png)
![correlation](images/correlation.png)
![horseweight](images/horseweight.png)


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

## Running The Code
Just go to `fetching.ipynb` to run it manually. It will be in Traditional Chinese version, if you want english version youll have
to adjust the params manually.
If you want to get the full set of dataset, please reach out to us privately.


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
