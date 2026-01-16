import pandas as pd
df = pd.read_csv("IPL_case_study\ipl_data.csv")
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.head())
print(df.tail())
print(df.info())

print(df["match_id"].fillna(549,inplace=True))
print(df["season"].fillna(df["season"].mode()[0],inplace=True))
print(df["city"].fillna(df["city"].mode()[0],inplace=True))
print(df["team1"].fillna("unknown",inplace=True))
print(df["team2"].fillna("unknown",inplace=True))
print(df["winning_team"].fillna("unknown",inplace=True))
print(df["player_of_match"].fillna("unknown",inplace=True))
print(df["venue"].fillna(df["venue"].mode()[0],inplace=True))
runs_scored_round = round(df["runs_scored"].mean())
print(df["runs_scored"].fillna(runs_scored_round,inplace=True))
wickets_round = round(df["wickets"].mean())
print(df["wickets"].fillna(wickets_round,inplace=True))

print(df.isnull().sum())

# ANALYSIS
# matches per season
print("matches per season",df["season"].value_counts())

# Top match count season
print("Top match count season",df["season"].value_counts().idxmax())

# Top match won by each team
print("Count of winning match",df["winning_team"].value_counts())

# Avg runs scored per season
print(df.groupby("season")["runs_scored"].mean())

# venue wise match count
print(df["venue"].value_counts())

# venue wise avg runs
print(df.groupby("venue")["runs_scored"].mean())

# city wise match count
print(df["city"].value_counts())

# city wise avg runs
print(df.groupby("city")["runs_scored"].mean())

# winning-team with highest avg run
print(df.groupby("winning_team")["runs_scored"].mean().idxmax())

# Top 3 venues
print(df["venue"].value_counts().head(3))