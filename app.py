from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load data
df = pd.read_csv("game_data.csv")
df = df.dropna(subset=['total_sales', 'genre'])
df['total_sales'] = df['total_sales'].astype(float)

@app.route('/', methods=['GET', 'POST'])
def index():
    genres = sorted(df['genre'].unique())
    selected_genre = request.form.get('genre')

    top_games = df.sort_values(by='total_sales', ascending=False).head(10)

    if selected_genre:
        recommended = df[df['genre'] == selected_genre].sort_values(by='total_sales', ascending=False).head(5)
        print(recommended.head())

    else:
        recommended = None

    return render_template("index.html", genres=genres, top_games=top_games, recommended=recommended)

# ai recommend
@app.route('/ai_recommend', methods=['GET', 'POST'])
def ai_recommend():
    df_indexed = pd.read_csv("game_index.csv")
    similarity = np.load("similarity_matrix.npy")
    games = df_indexed['title'].tolist()

    selected_game = request.form.get('game')
    if selected_game:
        idx = df_indexed[df_indexed['title'] == selected_game].index[0]
        scores = list(enumerate(similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
        recommendations = df_indexed.iloc[[i[0] for i in scores]]
    else:
        recommendations = None

    return render_template("ai_recommend.html", games=games, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
