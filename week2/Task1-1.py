import hashlib
import time
from flask import Flask, render_template, request, redirect, url_for

max_nonce = 2 ** 32  # 4 billion


def proof_of_work(header, difficulty_bits):
    target = 2 ** (256 - difficulty_bits)
    for nonce in range(max_nonce):
        hash_result = hashlib.sha256((str(header) + str(nonce)).encode("utf-8")).hexdigest()

        if int(hash_result, 16) < target:
            print("Success with nonce ", nonce)
            print("Hash is ", hash_result)
            return (hash_result, nonce)

    print("Failed after {} (max_nonce) tries".format(nonce))
    return nonce


#if __name__ == '__main__':
def main(d):

    nonce = 0
    hash_result = ''

    difficulty = 2 ** d

    print("")
    print("Difficulty: {} ({} bits)".format(difficulty, d))

    print("Starting search...")

    start_time = time.time()

    new_block = 'test block with transactions' + hash_result

    hash_result, nonce = proof_of_work(new_block, d)

    end_time = time.time()

    elapsed_time = end_time - start_time

    print("Elapsed time: {} seconds".format(elapsed_time))

    if elapsed_time > 0:
        hash_power = float(int(nonce) / elapsed_time)
        print("Hashing power: {} hashes per second".format(hash_power))

    return str(hash_result) + "\n" + str(nonce)


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == "POST":
        t_login = request.form["login"]
        s = main(int(t_login))
        return s
    else:
        return render_template("input.html")

if __name__ == "__main__":
    app.run(debug=True)
