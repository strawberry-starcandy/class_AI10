from flask import Flask, render_template, request
import datetime


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    now = datetime.datetime.now()
    now_text = now.strftime('%Y-%m-%d')
    htm_result = ''
            
            
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            htm_result = '''
            <h3>test</h3>'''
            if request.form.get('date_start') != None:
                htm_result += request.form.get('date_start') + '''
                    <table>
                    {% for member in members %}
                        <tr>
                            <td>{{ member.id }}</td>
                            <td>{{ member.name }}</td>
                            <td>{{ member.email }}</td>
                            <td>{{ member.phone }}</td>
                            <td>{{ member.start }}</td>
                            <td>{{ member.end }}</td>
                        </tr>
                    {% endfor %}
                    </table>
                    '''
        else:
            htm_result=''
        
    htm = '''<!doctype html>
            <html lang="ko">
              <head>
              <meta charset="utf-8">
                <title>News Viewer</title>
                <style>
                  * {
                    font-size: 16px;
                    font-family: Consolas, sans-serif;
                  }
                </style>
              </head>
              <body>
                <form method='post'>
                  <p>
                      <input type="date" name='date_start' value=''' + now_text + ' max=' + now_text + '''>
                      <input type="date" name='date_end' value=''' + now_text + ' max=' + now_text + '''>
                      <button type="button" name='search' onclick=alert(date_start.value)>조회</button>
                      <button type="submit" value="VALUE1" name='action1'>submit</button>
                  </p>
                </form>
                <form>
                    <p>
                    ''' + htm_result + '''
                    </p>
                
                </form>
              </body>
            </html>'''
            
    return htm

if __name__ == '__main__':
    app.run(debug=True)