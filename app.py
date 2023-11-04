from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Cologne, NRW',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Python Developer',
        'location': 'Frankfurt, Hesse',
        'salary': '€55,000'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'Cologne, NRW',
        'salary': '€60,000'
    },
    {
        'id': 4,
        'title': 'Angular Developer',
        'location': 'Dortmund, NRW',
        'salary': '€50,000'
    },
    {
        'id': 5,
        'title': 'M0bile App Developer',
        'location': 'Dortmund, NRW',
        'salary': '€60,000'
    },
]

@app.route("/")
def hello():
  return render_template("home.html", jobs = JOBS)
  
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
