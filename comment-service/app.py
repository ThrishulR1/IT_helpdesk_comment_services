from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_NAME = "comments.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id INTEGER,
        comment TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# GET COMMENTS
@app.route('/comments/<int:ticket_id>', methods=['GET'])
def get_comments(ticket_id):
    conn = get_connection()
    comments = conn.execute(
        "SELECT * FROM comments WHERE ticket_id = ?",
        (ticket_id,)
    ).fetchall()

    conn.close()

    return jsonify([dict(c) for c in comments])


#  ADD COMMENT
@app.route('/comments/<int:ticket_id>', methods=['POST'])
def add_comment(ticket_id):
    data = request.json
    comment = data.get('comment')

    conn = get_connection()
    conn.execute(
        "INSERT INTO comments (ticket_id, comment) VALUES (?, ?)",
        (ticket_id, comment)
    )
    conn.commit()
    conn.close()
   

    return {"message": "Comment added successfully"}


if __name__ == '__main__':
    init_db()
    app.run(port=5001, debug=True)