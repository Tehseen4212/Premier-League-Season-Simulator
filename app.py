import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Premier League Match Predictor",
    page_icon="⚽",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.header-box {
    background: linear-gradient(90deg,#38003c,#6c1d8f);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
}

.title {
    color: white;
    font-size: 42px;
    font-weight: bold;
    text-align: center;
}

.subtitle {
    color: white;
    text-align: center;
    font-size: 18px;
}

.metric-card {
    background: #ffffff;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

.prediction-card {
    background: #e8f5e9;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header-box">
    <div class="title">⚽ Premier League Match Predictor</div>
    <div class="subtitle">
        Predict Premier League match outcomes using historical performance data
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- LOAD FILES ----------------
model = joblib.load("premier_league_model.pkl")
team_strength = pd.read_csv("team_strength.csv", index_col=0)

# ---------------- TEAM ORDER ----------------
big6 = [
    "Arsenal",
    "Chelsea",
    "Liverpool",
    "Man City",
    "Man United",
    "Tottenham"
]

other_teams = sorted(
    [team for team in team_strength.index if team not in big6]
)

teams = big6 + other_teams

# ---------------- TEAM SELECTION ----------------
st.subheader("⚔️ Match Selection")

col1, col2 = st.columns(2)

with col1:
    home_team = st.selectbox(
        "🏠 Home Team",
        teams,
        index=0
    )

with col2:
    away_team = st.selectbox(
        "✈️ Away Team",
        teams,
        index=1
    )

# Prevent same team selection
if home_team == away_team:
    st.warning("Please select different teams.")
    st.stop()

st.divider()

# ---------------- TEAM STATS ----------------
st.subheader("📊 Team Strength Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### 🏠 {home_team}")

    st.metric(
        "Home Attack",
        f"{team_strength.loc[home_team,'HomeAttack']:.2f}"
    )

    st.metric(
        "Home Defense",
        f"{team_strength.loc[home_team,'HomeDefense']:.2f}"
    )

with col2:
    st.markdown(f"### ✈️ {away_team}")

    st.metric(
        "Away Attack",
        f"{team_strength.loc[away_team,'AwayAttack']:.2f}"
    )

    st.metric(
        "Away Defense",
        f"{team_strength.loc[away_team,'AwayDefense']:.2f}"
    )

# ---------------- COMPARISON GRAPH ----------------
st.subheader("📈 Team Comparison")

compare_df = pd.DataFrame({
    "Metric": ["Attack", "Defense"],
    home_team: [
        team_strength.loc[home_team, "HomeAttack"],
        team_strength.loc[home_team, "HomeDefense"]
    ],
    away_team: [
        team_strength.loc[away_team, "AwayAttack"],
        team_strength.loc[away_team, "AwayDefense"]
    ]
})

chart_df = compare_df.melt(
    id_vars="Metric",
    var_name="Team",
    value_name="Value"
)

fig = px.bar(
    chart_df,
    x="Metric",
    y="Value",
    color="Team",
    barmode="group",
    title="Attack & Defense Comparison"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------- PREDICTION ----------------
if st.button("🔮 Predict Match", use_container_width=True):

    home_attack = team_strength.loc[home_team, "HomeAttack"]
    home_defense = team_strength.loc[home_team, "HomeDefense"]

    away_attack = team_strength.loc[away_team, "AwayAttack"]
    away_defense = team_strength.loc[away_team, "AwayDefense"]

    features = [[
        home_attack,
        home_defense,
        away_attack,
        away_defense
    ]]

    prediction = model.predict(features)[0]

    if prediction == "H":
        result = f"🏠 {home_team} WIN"

    elif prediction == "A":
        result = f"✈️ {away_team} WIN"

    else:
        result = "🤝 DRAW"

    st.subheader("🏆 Match Prediction")

    st.markdown(
        f"""
        <div class="prediction-card">
        {result}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- PROBABILITIES ----------------
    probs = model.predict_proba(features)[0]
    chance_map = dict(zip(model.classes_, probs))

    home_prob = chance_map["H"] * 100
    draw_prob = chance_map["D"] * 100
    away_prob = chance_map["A"] * 100

    st.subheader("📊 Winning Chances")

    st.write(f"🏠 Home Win: {home_prob:.1f}%")
    st.progress(home_prob / 100)

    st.write(f"🤝 Draw: {draw_prob:.1f}%")
    st.progress(draw_prob / 100)

    st.write(f"✈️ Away Win: {away_prob:.1f}%")
    st.progress(away_prob / 100)

st.divider()

st.caption("Built using 16 seasons of Premier League historical data.")