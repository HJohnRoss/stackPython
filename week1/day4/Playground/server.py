from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def main():
    return render_template("index.html") #cant set num = to something or 
  # or an if statement to have 3 show for /play and for loop for else
  
@app.route('/play/<int:num>')
def addBox(num):
    return render_template("index.html", num=num)

# how to plug in classes into divs


if __name__ == "__main__":
    app.run(debug=True)
