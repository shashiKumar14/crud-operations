from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
import mysql.connector

app =Flask(__name__)
app.config['MYSQL_HOST']='localhost'#db['mysql_host']
app.config['MYSQL_USER']='root'#db['mysql_user']
app.config['MYSQL_PASSWORD']='Shashi@14'#db['mysql_password']
app.config['MYSQL_DB']='flaskapp'#'localhost'db['mysql_db']

mysql=MySQL(app)

@app.route("/",methods=['GET','POST'])
def create():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails['name']
        email=userDetails['email']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email) VALUES(%s,%s)",(name,email))
        mysql.connection.commit()
        cur.close()
        return redirect('/read')
    return render_template('index.html')

@app.route('/read')
def read():
    cur=mysql.connection.cursor()
    resultvalue=cur.execute("SELECT * FROM users")
    if resultvalue>0:
        userDetails=cur.fetchall()
        return render_template('user.html',userDetails=userDetails)

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method=='POST':
        userDetails=request.form
        name=userDetails['name']
        email=userDetails['email']
        cur=mysql.connection.cursor()
        cur.execute("UPDATE users set name=%s where email=%s",(name,email))
        mysql.connection.commit()
        cur.close()
        return redirect('/read')
    return render_template('index.html')

@app.route('/delete/<string:name>',methods=['POST','GET'])
def delete(name):
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE name=%s",(name,))
    mysql.connection.commit()
    cur.close()
    return redirect('/read')
    # return render_template('index.html')







if __name__ == '__main__':
    app.run(debug=True)
