from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

Base = declarative_base()
URL = 'mssql+pyodbc://DESKTOP-N7F35MN\SQLEXPRESS/React_DB?driver=ODBC+Driver+17+for+SQL+Server'
conn = create_engine(URL)
Session = sessionmaker(bind=conn)
session = Session()

class Intern(Base):
    __tablename__ = "bplusm_interns"
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    salary = Column(String)
    age = Column(String)
    company = Column(String)

@app.route("/data" ,methods=["GET"])
def get_data():
    intern = session.query(Intern).all()
    interns_list = []
    for data in intern:
        datalist = {
            "Id":data.id,
            "Fname": data.fname,
            "Lname": data.lname,
            "Salary": data.salary,
            "Age": data.age,
            "Company": data.company
        }
        interns_list.append(datalist)
    return jsonify(interns_list)

@app.route("/data", methods=["POST"])
def add_data():
    data = request.json
    new_data = Intern(
        fname=data["Fname"],
        lname=data["Lname"],
        salary=data["Salary"],
        age=data["Age"],
        company=data["Company"]
    )
    session.add(new_data)
    session.commit()
    return jsonify({"message": "Data added successfully"})

@app.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    data = session.query(Intern).filter_by(id=id).first()
    session.delete(data)
    session.commit()
    return jsonify({"message": "Data deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
