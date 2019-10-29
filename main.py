from flask import Flask, request
from units import url_encode, get_v2ray, get_admin_not_shared, is_admin, get_ss

app = Flask(__name__)


@app.route("/edit", methods=["POST"])
def edit():
    pass


@app.route("/share", methods=["GET"])
def share():
    kind = request.args.get("kind")
    token = request.args.get("token")
    place = request.args.get("place")
    resp = {
        "v2ray": "",
        "ss": ""
        }
    if kind == "1":
        get_v2ray(token=token, response=resp)
        return url_encode(resp["v2ray"].encode("utf-8"))
    elif kind == "2":
        get_ss(token=token, response=resp)
        return url_encode(resp["ss"].encode("utf-8"))
    elif kind == "3":
        get_ss(token=token, response=resp)
        get_v2ray(token=token, response=resp)
        return url_encode("{}\n{}".format(resp["ss"], resp["v2ray"]).encode("utf-8"))


@app.route("/get", methods=['GET'])
def get():
    pass


@app.route("/admin", methods=["GET"])
def get_admin():
    token = request.args.get("token")
    if is_admin(token):
        d = get_admin_not_shared()
        return url_encode(d.encode("utf-8"))
    else:
        return "None"


if __name__ == '__main__':
    app.run()
