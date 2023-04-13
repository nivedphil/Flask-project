from flask import Flask, render_template

app = Flask(__name__)

DATA = [
  {
    "id":1,
    "Name": "Nived Philip Thomas",
    "Room-No.": 19,
    "Branch": "Mechanical Engineering"
  },
  {
    "id":2,
    "Name": "Jay Paresh savla",
    "Room-No.": 19,
    "Branch": "Artificial Intelligence"
  },
  {
    "id":3,
    "Name": "Anuraag BV",
    "Room-No.": 19,
    "Branch": "Computer Science Engineering"
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html", data=DATA)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)