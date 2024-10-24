from flask import render_template, Flask , request
import grules

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data= request.form.get('cal_display')
        result= grules.Operacion(data)
        return render_template('index.html',result=result, input=data)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)