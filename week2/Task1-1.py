import hashlib
from flask import Flask, render_template, request

max_nonce = 2 ** 32


def proof_of_work(header, difficulty_bits):
    target = 2 ** (256 - difficulty_bits)

    for nonce in range(max_nonce):
        hash_result = hashlib.sha256((str(header) + str(nonce)).encode("utf-8")).hexdigest()

        if int(hash_result, 16) < target:
            return (hash_result, nonce)

    return nonce


def calculate(d):
    hash_result = ''
    new_block = 'test block with transactions' + hash_result
    hash_result, nonce = proof_of_work(new_block, d)

    return [str(hash_result), str(nonce)]


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == "POST":
        inp = request.form["in"]
        s = calculate(int(inp))
        s = "Hash result: {} Nonce: {}".format(*s)
        return s
    else:
        return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)
