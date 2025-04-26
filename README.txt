# Game Ranking and Recommendation System

This is a simple Flask web application that allows users to view the top 10 best-selling video games and receive game recommendations based on selected genres.

## 📁 Project Structure

├── app.py                  ← Main Flask application
├── game_data.csv           ← Dataset (video game sales)
├── model_train.py           # AI model training script  
├── game_index.csv           # Game metadata used for recommendations  
├── similarity_matrix.npy    # Precomputed similarity matrix  
├── static/
│   └── genre_chart.png     ← Visualization chart (genre total sales)
├── templates/
│   └── index.html          ← Webpage template
│   └── ai_recommend.html    # AI recommendation page template  
└── README.txt              ← This instruction file

---

## 💻 How to Run the Project

### 1. Install Required Packages

Open your terminal or command prompt and run:

pip install flask pandas


### 2. Train the AI Model

If you want to regenerate the recommendation model:

python model_train.py

### 3. Run the Web Application

In the terminal, navigate to the project folder and execute:

python app.py

If successful, you’ll see:

 * Running on http://127.0.0.1:5000

Open this address in your browser.

Created by: Shih-Yao Cheng
Course: CPSC 8740 – Final Project

