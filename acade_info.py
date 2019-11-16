from flask import Flask, request, jsonify


ERROR_MESSAGE = '네트워크 접속에 문제가 발생하였습니다. 잠시 후 다시 시도해주세요.'


app = Flask(__name__)


# 피자 주문 스킬
@app.route('/info', methods=['POST'])
def order():

    # 메시지 받기
    req = request.get_json()

    academicInfo = req["action"]["detailParams"]["학사정보"]["value"]
    #infoURL = req["action"]["detailParams"]["sys_text"]["value"]
    infoURL = "여기"
    
    if len(pizza_type) <= 0 or len(address) <= 0:
        answer = ERROR_MESSAGE
    else:
        answer = academicInfo + "에 대한 정보는" + infoURL + "에서 찾을수 가 있네요"

    # 메시지 설정
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


# 메인 함수
if __name__ == '__main__':

    app.run(host='0.0.0.0', threaded=True, debug = True)