from flask import Flask, render_template
app = Flask(__name__)


# def main():
#     return render_template("index.html", num=3) #cant set num = to something or 
#   or an if statement to have 3 show for /play and for loop for else
  
# def addBox(num):
#     return render_template("index.html", num=num)

# how to plug in classes into divs


# you can add muliple routs to 1 function! (set var's = something)
@app.route('/play')
@app.route('/play/')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<string:color>')
def add_bg_color(num=3, color="#9EC5F7"):
    return render_template("index.html", num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
