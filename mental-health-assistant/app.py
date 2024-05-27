from flask import Flask, request, render_template, jsonify
from transformers import pipeline
import database

app = Flask(__name__)

# Inicializar o banco de dados
with app.app_context():
    database.init_db()

# Carregar o pipeline de análise de sentimentos do Hugging Face
sentiment_analyzer = pipeline('sentiment-analysis')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data['text']
    user_id = data['user_id']
    result = sentiment_analyzer(text)[0]
    sentiment = result['label']
    
    # Salvar a entrada no banco de dados
    conn = database.get_db_connection()
    conn.execute('INSERT INTO entries (user_id, date, text, sentiment) VALUES (?, datetime("now"), ?, ?)',
                 (user_id, text, sentiment))
    conn.commit()
    conn.close()
    
    return jsonify(result)

@app.route('/entries/<int:user_id>')
def get_entries(user_id):
    conn = database.get_db_connection()
    entries = conn.execute('SELECT * FROM entries WHERE user_id = ?', (user_id,)).fetchall()
    conn.close()
    return jsonify([dict(entry) for entry in entries])

if __name__ == '__main__':
    app.run(debug=True)
