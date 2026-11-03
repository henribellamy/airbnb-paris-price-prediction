# Airbnb Price Prediction in Paris

*Machine learning project · Université Paris-Saclay (2026)*

***

## Overview

This project predicts the nightly price of a Paris Airbnb listing **at the moment it goes online**, using only the information a new host can provide: location, size, amenities and host profile.

The project uses real data: 37,363 short-term listings from the Inside Airbnb snapshot of Paris (September 2026). We compare median baselines, Ridge regression, k-nearest neighbours, random forest and XGBoost. Since hosts often publish many near-identical listings, models are always evaluated on **hosts they have never seen**.

***

## Key result

Evaluation on a held-out test set of 20% of hosts:

| Model | RMSE (log) | MAE (€) | R² |
|---|---:|---:|---:|
| Global median | 0.649 | 163 | -0.02 |
| Median by arrondissement | 0.606 | 153 | 0.11 |
| **XGBoost** | **0.391** | **102** | **0.63** |

XGBoost reduces the error of the best baseline by about a third. The price is driven mainly by **size and location**; luxury listings are underestimated, as their standing is described in the text rather than in structured columns.

Full methodology and analysis in the [report](report.pdf).

***

## Repository structure

| File | Content |
|---|---|
| [airbnb.ipynb](airbnb.ipynb) | Data preparation, exploration and modelling |
| [report.pdf](report.pdf) | Project report |
| [data.py](data.py) | Downloads the data into `data/` and checks the MD5 |
| [requirements.txt](requirements.txt) | Python dependencies (Python 3.11 or later) |

To reproduce: `pip install -r requirements.txt`, `python data.py`, then run the notebook.

***

## Technical stack

Python · pandas · scikit-learn · XGBoost · GeoPandas · Matplotlib · Jupyter

***

## Credits

Data © [Inside Airbnb](https://insideairbnb.com/get-the-data/), used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Personal data are dropped and all results are aggregated.

***

## Contact

**Henri Bellamy**
[LinkedIn](https://www.linkedin.com/in/henri-bellamy-232b5b28a/) · [henribellamy@icloud.com](mailto:henribellamy@icloud.com)
