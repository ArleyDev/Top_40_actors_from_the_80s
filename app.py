from flask import Flask,request,render_template,jsonify,redirect
from Models import db, cuarenta

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///C:/Users/Jilmer Moreno/Desktop/ActorsFromEightiesV3/database/cuarenta.db"



app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

#Con la siguiente línea la aplicación sabe con que base de datos conectar
db.init_app(app)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/api/searchactor',methods=['POST'])
def buscarActor():
    nombre=request.form['nombre']
    #actoractriz=cuarenta.query.filter_by(nombre=nombre).first()
    actoractriz=cuarenta.query.filter(cuarenta.nombre.like(f"%{nombre}%")).first()
    # Aquí requiero que si actoractriz no tiene ningún valor (no se encontró) devuelva un mensaje de no encontrado
    if not actoractriz:
        return "Lo siento tu actor/actriz no se encuentra en los cuarenta más destacados" 
    else:
            
        return render_template("searchactor.html",actoractrizPlaceholder=actoractriz)




    

if (__name__) == '__main__':
    app.run(debug=True)
