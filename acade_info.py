from flask import Flask, request, jsonify


ERROR_MESSAGE = '��Ʈ��ũ ���ӿ� ������ �߻��Ͽ����ϴ�. ��� �� �ٽ� �õ����ּ���.'


app = Flask(__name__)


# ���� �ֹ� ��ų
@app.route('/info', methods=['POST'])
def order():

    # �޽��� �ޱ�
    req = request.get_json()

    academicInfo = req["action"]["detailParams"]["�л�����"]["value"]
    #infoURL = req["action"]["detailParams"]["sys_text"]["value"]
    infoURL = "����"
    
    if len(pizza_type) <= 0 or len(address) <= 0:
        answer = ERROR_MESSAGE
    else:
        answer = academicInfo + "�� ���� ������" + infoURL + "���� ã���� �� �ֳ׿�"

    # �޽��� ����
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    return jsonify(res)


# ���� �Լ�
if __name__ == '__main__':

    app.run(host='0.0.0.0', threaded=True, debug = True)