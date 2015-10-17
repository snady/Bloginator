from flask import Flask, render_template, request, session, redirect
from backend import member_data, post_data

post_til = 10
i = 0
app=Flask(__name__)
@app.route('/')
@app.route('/home',methods=["GET","POST"])
def home():
    #Track whether the user has logged in
    if 'logged' not in session:
        session['logged']=False
    if request.method=="POST":
        post_data.addPost(request.form['story'],request.form['title'],session['username'])
    return render_template('home.html',s=session, i=i, post_til = post_til)

def post_count():
    i+=1
    return i < post_til
@app.route('/add_more_posts/')
def add_up():
    i=0
    post_til+=10
    return

@app.route('/login',methods=["GET","POST"])
def login():
    if 'logged' not in session:
        session['logged']=False
    #If the user is trying to log in, verify password
    if request.method=="POST":
        if (request.form['button']=="New Account"):
            if (member_data.filterUname(request.form['username'])):
                member_data.addMember(request.form['username'], request.form['password'])
                session['logged']=True
                session['username']=request.form['username']
                return redirect('/')
            else:
                return render_template('login.html',s=session,error="Username already taken")
        if (request.form['button']=="login"):
            if member_data.checkPass(request.form['username'], request.form['password']):
                session['logged']=True
                session['username']=request.form['username']
                return redirect('/')
            else:
                return render_template('login.html',s=session,error="Incorrect Username/Password")
    return render_template('login.html',s=session)

#When a user clicks a button to logout, direct them here, log them out and redirect them
@app.route('/logout')
def logout():
    session['logged'] = False
    return redirect('/login')

if __name__=="__main__":
    app.debug = True
    app.secret_key="Don't tell anyone!"
    app.run('0.0.0.0', port=8000)
