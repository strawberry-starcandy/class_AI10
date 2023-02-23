from flask import Flask, render_template, request
import datetime
import mysql

# In[4]:


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    error = None
    
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        
        conn = mysql.connection
        cursor = conn.cursor();
        
        sql = f"select id from users where 
        
        cursor.excute(sql)
        
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        for row in data:
            data = row[0]
        
        if data:
            session['login id'] = id
            return redirect(url_for('home', name, 
    return render_template('main.htm')


if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:




