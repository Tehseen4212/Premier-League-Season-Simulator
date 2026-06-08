# ⚽ Premier League Match Predictor

An interactive football analytics application that predicts Premier League match outcomes using historical EPL data and team performance metrics.

## 📌 Project Overview

This project analyzes 16 seasons of Premier League data (2010–11 to 2025–26) to estimate the outcome of upcoming fixtures.

The application calculates team strength metrics from historical performance and provides match predictions along with win probabilities for both teams and draw scenarios.

## 🚀 Features

* Predict Premier League match outcomes
* Interactive Streamlit web application
* Team strength comparison dashboard
* Win probability visualization
* Historical performance-based analysis
* User-friendly match selection interface

## 📊 Dataset

The project uses Premier League match data covering 16 seasons:

* Seasons: 2010–11 to 2025–26
* Total Matches: 6,000+ matches
* Teams Covered: 41 Premier League clubs

### Available Match Statistics

* Full-Time Result
* Goals Scored
* Half-Time Result
* Shots & Shots on Target
* Fouls
* Corners
* Yellow Cards
* Red Cards

## ⚙️ Feature Engineering

Custom team strength metrics were created from historical match performance:

* Home Attack Strength
* Home Defense Strength
* Away Attack Strength
* Away Defense Strength

These metrics are used to compare teams and generate match predictions.

## 🖥️ Application Preview

The Streamlit application allows users to:

1. Select a Home Team
2. Select an Away Team
3. Compare team strengths
4. Generate a match prediction
5. View win probability estimates

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* Plotly

## 📂 Project Structure

```text
Premier-League-Season-Simulator/
│
├── data/
├── app.py
├── premier_league.ipynb
├── premier_league_model.pkl
├── team_strength.csv
└── README.md
```

## 🔮 Future Improvements

* Recent form analysis
* Head-to-head statistics
* Expected Goals (xG) integration
* League table simulation
* Live data integration
* Cloud deployment

## 📜 Disclaimer

Predictions are generated using historical performance patterns and are intended for educational and analytical purposes only.
