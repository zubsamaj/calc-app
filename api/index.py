from flask import Flask, render_template, request

test_var = 123456

auth_token = 'asvdjasbdvjhgty21312378sgdajsd'

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
   result = ''
   if request.method == "POST":
      try:
         expression = request.form["display"]
         # Evaluate the expression safely using eval
         result = eval(expression)
      except Exception as e:
         result = "Error"
   return render_template("index.html", result=result)

if __name__ == "__main__":
   app.run(host='0.0.0.0')