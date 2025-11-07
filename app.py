# docker test
# 7/11/2025, by ugxd
# i sometimes use this account, go to bann6r for more

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "hey bro this is running in docker!!1!"

@app.route('/test')
def test():
    # This uses an external library to prove dependencies work
    response = requests.get('https://api.github.com')
    return f"da github api status is {response.status_code}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**requirements.txt**:
```
flask==3.0.0
requests==2.31.0
