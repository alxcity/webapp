from flask importr Flask,render_template
app=Flask(_name_)
@app.route('/')
def home():
  return render template('index.html',title="Home Page")
if __ name __ =='__ main __':
  app.run(host='127.0.0.1',port=8080,debug=True)
