from flask import Flask, request, jsonify
from db.connection import SessionLocal
from db.models.urls import URL


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def hello_world():
    print("Hello, World!")
    return "<p>Hello, World!</p>"


@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({
            "error": 'URL is required'
        }), 400

    db = SessionLocal()
    try:
        existing_url = db.query(URL).filter(
            URL.unshortened_url == data['url']).first()
        if existing_url:
            return jsonify({
                "shortened_url": existing_url.shortened_url
            })

        new_url = URL(unshortened_url=data['url'])
        new_url.generate_shortened_url()

        db.add(new_url)
        db.commit()
        db.refresh(new_url)

        return jsonify({
            "shortened_url": new_url.shortened_url
        })

    except Exception as e:
        db.rollback()
        return jsonify({
            "error": str(e)
        }), 500

    finally:
        db.close()
