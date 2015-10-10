from flask import Flask, render_template, request, session, redirect

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def about():
    #Track whether the user has logged in
    if 'logged' not in session:
        session['logged']=False
    return render_template('home.html',s=session)

@app.route('/login')
def login(error=None, methods=["GET","POST"]):
    #If the user is trying to log in, verify password
    if request.method=="POST":
        #This function is anticipated to come from chloe's work
        if database.verify(request.form['username'], request.form['password']):
            session['logged']=True
            return redirect('/')
        else:
            return render_template('login.html',s=session,error="Incorrect Username/Password")
    return render_template('login.html',s=session,error=None)

#When a user clicks a button to logout, direct them here, log them out and redirect them
@app.route('/logout')
def logout():
    session['logged'] = False
    return redirect('/login')

if __name__=="__main__":
    app.debug = True
    app.secret_key="Don't tell anyone!"
    app.run('0.0.0.0', port=8000)
