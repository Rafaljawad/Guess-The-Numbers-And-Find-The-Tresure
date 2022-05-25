from flask import Flask, render_template
import random

app=Flask(__name__)
@app.route('/<int:num>')
def random_choice(num):
    random_num= random.randrange(1, 5)
    print(random_num)
    return render_template('index.html',num=num,random_num=random_num)

if __name__=='__main__':
    app.run(debug=True)