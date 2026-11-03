{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;\f1\fnil\fcharset0 Menlo-Italic;\f2\fnil\fcharset0 Menlo-Bold;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red144\green1\blue18;\red0\green0\blue117;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c6667\c53333;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Airbnb Price Prediction in Paris\cf0 \cb1 \strokec4 \
\

\f1\i \cb3 *Machine learning project \'b7 Universit\'e9 Paris-Saclay (2026)*
\f0\i0 \cb1 \
\
\cb3 ***\cb1 \
\
\cf2 \cb3 \strokec2 ## Overview\cf0 \cb1 \strokec4 \
\
\cb3 This project predicts the nightly price of a Paris Airbnb listing 
\f2\b **at the moment it goes online**
\f0\b0 , using only the information a new host can provide: location, size, amenities and host profile.\cb1 \
\
\cb3 The project uses real data: 37,363 short-term listings from the Inside Airbnb snapshot of Paris (September 2026). We compare median baselines, Ridge regression, k-nearest neighbours, random forest and XGBoost. Since hosts often publish many near-identical listings, models are always evaluated on 
\f2\b **hosts they have never seen**
\f0\b0 .\cb1 \
\
\cb3 ***\cb1 \
\
\cf2 \cb3 \strokec2 ## Key result\cf0 \cb1 \strokec4 \
\
\cb3 Evaluation on a held-out test set of 20% of hosts:\cb1 \
\
\cf2 \cb3 \strokec2 | Model | RMSE (log) | MAE (\'80) | R\'b2 |\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 |---|---:|---:|---:|\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 |\cf0 \strokec4  Global median \cf2 \strokec2 |\cf0 \strokec4  0.649 \cf2 \strokec2 |\cf0 \strokec4  163 \cf2 \strokec2 | -\cf0 \strokec4 0.02 \cf2 \strokec2 |\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 |\cf0 \strokec4  Median by arrondissement \cf2 \strokec2 |\cf0 \strokec4  0.606 \cf2 \strokec2 |\cf0 \strokec4  153 \cf2 \strokec2 |\cf0 \strokec4  0.11 \cf2 \strokec2 |\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 |\cf0 \strokec4  
\f2\b **XGBoost**
\f0\b0  \cf2 \strokec2 |\cf0 \strokec4  
\f2\b **0.391**
\f0\b0  \cf2 \strokec2 |\cf0 \strokec4  
\f2\b **102**
\f0\b0  \cf2 \strokec2 |\cf0 \strokec4  
\f2\b **0.63**
\f0\b0  \cf2 \strokec2 |\cf0 \cb1 \strokec4 \
\
\cb3 XGBoost reduces the error of the best baseline by about a third. The price is driven mainly by 
\f2\b **size and location**
\f0\b0 ; luxury listings are underestimated, as their standing is described in the text rather than in structured columns.\cb1 \
\
\cb3 Full methodology and analysis in the \cf5 \strokec5 [\cf0 \strokec4 report\cf5 \strokec5 ](report.pdf)\cf0 \strokec4 .\cb1 \
\
\cb3 ***\cb1 \
\
\cf2 \cb3 \strokec2 ## Repository structure\cf0 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 | File | Content |\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 |---|---|\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 |\cf0 \strokec4  \cf5 \strokec5 [\cf0 \strokec4 airbnb.ipynb\cf5 \strokec5 ](airbnb.ipynb)\cf0 \strokec4  \cf2 \strokec2 |\cf0 \strokec4  Data preparation, exploration and modelling \cf2 \strokec2 |\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 |\cf0 \strokec4  \cf5 \strokec5 [\cf0 \strokec4 report.pdf\cf5 \strokec5 ](report.pdf)\cf0 \strokec4  \cf2 \strokec2 |\cf0 \strokec4  Project report \cf2 \strokec2 |\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 |\cf0 \strokec4  \cf5 \strokec5 [\cf0 \strokec4 data.py\cf5 \strokec5 ](data.py)\cf0 \strokec4  \cf2 \strokec2 |\cf0 \strokec4  Downloads the data into \cf6 \strokec6 `data/`\cf0 \strokec4  and checks the MD5 \cf2 \strokec2 |\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 |\cf0 \strokec4  \cf5 \strokec5 [\cf0 \strokec4 requirements.txt\cf5 \strokec5 ](requirements.txt)\cf0 \strokec4  \cf2 \strokec2 |\cf0 \strokec4  Python dependencies (Python 3.11 or later) \cf2 \strokec2 |\cf0 \cb1 \strokec4 \
\
\cb3 To reproduce: \cf6 \strokec6 `pip install -r requirements.txt`\cf0 \strokec4 , \cf6 \strokec6 `python data.py`\cf0 \strokec4 , then run the notebook.\cb1 \
\
\cb3 ***\cb1 \
\
\cf2 \cb3 \strokec2 ## Technical stack\cf0 \cb1 \strokec4 \
\
\cb3 Python \'b7 pandas \'b7 scikit-learn \'b7 XGBoost \'b7 GeoPandas \'b7 Matplotlib \'b7 Jupyter\cb1 \
\
\cb3 ***\cb1 \
\
\cf2 \cb3 \strokec2 ## Credits\cf0 \cb1 \strokec4 \
\
\cb3 Data \'a9 \cf5 \strokec5 [\cf0 \strokec4 Inside Airbnb\cf5 \strokec5 ](https://insideairbnb.com/get-the-data/)\cf0 \strokec4 , used under \cf5 \strokec5 [\cf0 \strokec4 CC BY 4.0\cf5 \strokec5 ](https://creativecommons.org/licenses/by/4.0/)\cf0 \strokec4 . Personal data are dropped and all results are aggregated.\cb1 \
\
\cb3 ***\cb1 \
\
\cf2 \cb3 \strokec2 ## Contact\cf0 \cb1 \strokec4 \
\

\f2\b \cb3 **Henri Bellamy**
\f0\b0 \cb1 \
\cf5 \cb3 \strokec5 [\cf0 \strokec4 LinkedIn\cf5 \strokec5 ](https://www.linkedin.com/in/henri-bellamy-232b5b28a/)\cf0 \strokec4  \'b7 \cf5 \strokec5 [\cf0 \strokec4 henribellamy@icloud.com\cf5 \strokec5 ](mailto:henribellamy@icloud.com)\cf0 \cb1 \strokec4 \
}