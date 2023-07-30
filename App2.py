# import App
# from flask import Flask, jsonify
# from flask_cors import CORS


# app = Flask(__name__)
# CORS(app,resources={r"/data/*": {"origins": "http://localhost:3000"}})

# @app.route("/data")
# def new_data():
#     data = App.get_data()
#     return jsonify(data)

# @app.route("/data/<int:id>")
# def delete_data(user_id):
#     data=session.query(Intern).filter_by(id=user_id).first()
#     session.delete(data)
#     session.commit()

# if __name__ == '__main__':
#     app.run()
