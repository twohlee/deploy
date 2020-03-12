# 서비스

from flask import Flask

app = Flask(__name__) # 플라스크 객체 만들기 

@app.route('/')
def home():
    return 'aws 홈페이지'

if __name__ == '__main__':
    app.run(debug=True)



