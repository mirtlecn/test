from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # 获取 JSON 数据
    data = request.get_json()

    # 打印接收到的 JSON 数据
    print(json.dumps(data, indent=4))

    # 返回一个响应
    return "Webhook received", 200

if __name__ == '__main__':
    # 在 0.0.0.0 上绑定 444 端口，使其可以通过公网访问
    app.run(host='0.0.0.0', port=444)
