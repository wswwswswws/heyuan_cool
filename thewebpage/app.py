from flask import Flask, render_template, jsonify, request
from mysql import insert
from gevent import pywsgi
import flask

# 创建一个Flask应用程序
app = flask.Flask(__name__)

@app.route('/')
def index():
    a = "《西游记》"  # 你可以根据需要设置变量的值
    return render_template('index.html', a=a)

@app.route('/2.html')
def page2():
    return render_template('2.html')

@app.route('/update_cell_value')
def update_cell_value():
    new_value = "《白蛇传》"  # 你可以根据需要设置新的值
    return jsonify({"new_value": new_value})

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()

        insert(data)
        # 在这里处理接收到的数据，可以将数据存储到数据库或进行其他操作
        # 示例：将数据打印到控制台


        # 返回一个简单的成功响应
        return jsonify({'message': 'Form data received successfully!'})

    except Exception as e:
        print('Error:', str(e))
        return jsonify({'error': 'An error occurred while processing the form data.'}), 500

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0',80),app)
    print('sb')
    server.serve_forever()
    print('dsb')

# 河源
#公 47.115.205.240
#私 172.25.254.214

#杭州
#公 无
#私 172.29.91.209