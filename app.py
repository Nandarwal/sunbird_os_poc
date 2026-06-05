from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    host="localhost",
    database="intern_assessment",
    user="quiz_admin",
    password="SecretPassword123"
)

@app.route('/register', methods=['POST'])
def register():

    try:

        data = request.json

        phone = data['phone_number']
        password = data['password']

        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO users
            (phone_number, password_hash)
            VALUES (%s,%s)
            """,
            (phone, password)
        )

        conn.commit()

        return jsonify({
            "success": True
        })

    except Exception as e:

        print(e)

        return jsonify({
            "success": False
        })
    
@app.route('/login', methods=['POST'])
def login():

    data = request.json

    phone = data['phone_number']
    password = data['password']

    cur = conn.cursor()

    cur.execute(
        """
        SELECT id
        FROM users
        WHERE phone_number=%s
        AND password_hash=%s
        """,
        (phone, password)
    )

    user = cur.fetchone()

    if user:

        return jsonify({
            "success": True,
            "user_id": user[0]
        })

    return jsonify({
        "success": False
    })

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    cur = conn.cursor()

    phone_number = data['phone_number']
    quiz_id = data['quiz_id']
    quiz_name = data['quiz_name']
    score = data['score']
    total_questions = data['total_questions']

    cur.execute("""
        INSERT INTO quiz_results
        (phone_number, quiz_id, quiz_name, score, total_questions)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        phone_number,
        quiz_id,
        quiz_name,
        score,
        total_questions
    ))

    conn.commit()

    return jsonify({"status": "saved"})


if __name__ == '__main__':
    app.run(port=5000, debug=True)

#comment
