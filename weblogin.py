from flask import Flask, render_template, request, redirect, url_for
import pymysql

def chkPsw(name):
    coon = pymysql.connect(host="127.0.0.1", user="dan", password="3224", db="broadcastdb", port=3306)
    cursor = coon.cursor()
    cursor.execute('select password from user where username = "%s" ' % name)
    return cursor.fetchall()


app = Flask(__name__)
@app.route("/", methods=['POST', 'GET'])
def home():
    error = False
    nameValue = '请输入用户名'
    pswValue = '请输入密码'
    pswType = 'text'
    if request.method == 'POST':
        password = chkPsw(request.form['lname'])
        if request.form['lpsw'] == password[0][0]:
            return redirect('http://www.baidu.com/')
        else:
            error = True
            nameValue = request.form['lname']
            pswType = 'password'
            pswValue = ''
    return render_template('login.html', error=error, nameValue=nameValue, pswValue=pswValue, pswType=pswType)

if __name__ == "__main__":
    app.run(debug=True)