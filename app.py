from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    'ID': 1,
    'TITLE': 'Data Analyst',
    'LOCATION': 'Nairobi, Kenya',
    'SALARY': 'Ksh. 80,000' 
  },
   {
    'ID': 2,
    'TITLE': 'Data Scientist',
    'LOCATION': 'Nakuru, Kenya',
    'SALARY': 'Ksh. 100,000' 
  },
   {
    'ID': 3,
    'TITLE': 'Front-End Engineer',
    'LOCATION': 'Mombasa, Kenya',
    'SALARY': 'Ksh. 90,000' 
  },
   {
    'ID': 4,
    'TITLE': 'Back-End Engineer',
    'LOCATION': 'Remote',
    'SALARY': 'Ksh. 120,000' 
  },
]
@app.route("/")
def hello_world():
  return render_template("home.html", 
                         jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host= '0.0.0.0', debug=True)
