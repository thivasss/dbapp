#Error me sxolia sta ellinka opote greeklish :S
#Sto ksekinima tis ergasias pistevame oti tha ginei me sqlalchemy... welp den isxuei alla emine to onoma.


#importing pragmata kai thaumata
from flask import Flask, render_template, request, url_for, redirect;
#Diaxorizoume ta application mas apo ton vasiko codika pou anoigei i python gia na einai pio clean. Python initialization einai sto app.py
from app import app;
#Xrisimopoioume sqlite3 san vasi
import sqlite3

#Database creation. To treksame mia fora gia na dimiourgithei kainouria vasi databank. Epita den xriazete
#conx = sqlite3.connect('databank.db')
#c=conx.cursor()
#Episis one time run gia tin dimiourgia tou pinaka 
#c.execute('''CREATE TABLE infos (uname, weight,height, age)''')

#ROUTES FOR THE HTMLS

#Sundesi / me to home.html
@app.route('/')
def home():
    return render_template('home.html');

#Sundesi mainapp
@app.route('/mainapp', methods = ['GET','POST'])
def mainapp():
    return render_template('mainapp.html')


    


#I selida mainapp katefthinei edw pera meso {{ url_for('subm') }}
@app.route('/subm', methods = ['POST','GET'])       
def subm():
    if request.method == 'POST':
      try:
          #metaferoume to input tou xristi se variables p mporei na anagnorisei i python meso jinja 
         weight = request.form['weight'];
         age = request.form['age'];
         uname = request.form['uname'];
         height = request.form['height'];
         #sindesi stin vasi wste na ta apothikefsoume monima.
         

    #     cal = (10*weight)+(6.25*height)-(5*age);

         conx = sqlite3.connect("databank.db")
         c = conx.cursor()
         c.execute("INSERT INTO infos (weight,age,uname,height) VALUES (?,?,?,?)",(weight,age,uname,height))
         conx.commit()
         msg = "Record successfully added"
      except:
         conx.rollback()
         msg = "error in insert operation"  
      finally:
         return render_template('result.html', msg = msg)
         conx.close()
    
#selida meso tis opoias mporoume na doume oti uparxei mesa stin vasi
@app.route('/database')
def database():
   conx = sqlite3.connect("databank.db")
   conx.row_factory = sqlite3.Row
   
   c = conx.cursor()
   c.execute("SELECT * FROM infos")
   
   rows = c.fetchall(); 
   return render_template("database.html",rows = rows)

#@app.route('/result')
  #  def result():
   #     render_template('result.html')

      

