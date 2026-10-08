from flask import Flask, request, make_response
import os

app = Flask(__name__)

FLAG = "NIMIT{COOKIE_MONSTER}"


HTML_USER = """
<!DOCTYPE html>
<html>
<head>
    <title>NIMIT Dashboard</title>
    <style>
        body {
            background: #0b0f14;
            color: #e6edf3;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 100px;
        }

        .box {
            width: 500px;
            margin: auto;
            padding: 40px;
            background: #111820;
            border: 1px solid #263241;
            border-radius: 12px;
        }

        .warning {
            margin-top: 25px;
            padding: 15px;
            background: #241919;
            color: #ff7b72;
            border-radius: 8px;
        }

        .hint {
            margin-top: 20px;
            color: #8b949e;
        }
    </style>
</head>

<body>
    <div class="box">
        <h1>👤 User Dashboard</h1>

        <p>You are logged in as a normal user.</p>

        <div class="warning">
            Administrator privileges required.
        </div>

        <div class="hint">
            Your session information is stored by the browser.
        </div>
    </div>
</body>
</html>
"""


HTML_ADMIN = f"""
<!DOCTYPE html>
<html>
<head>
    <title>NIMIT Admin Portal</title>
    <style>
        body {{
            background: #0b0f14;
            color: #e6edf3;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 100px;
        }}

        .box {{
            width: 500px;
            margin: auto;
            padding: 40px;
            background: #111820;
            border: 1px solid #263241;
            border-radius: 12px;
        }}

        .flag {{
            margin-top: 25px;
            padding: 15px;
            background: #16251b;
            color: #7ee787;
            font-weight: bold;
            border-radius: 8px;
        }}
    </style>
</head>

<body>
    <div class="box">
        <h1>🔐 Administrator Dashboard</h1>

        <p>Administrator access granted.</p>

        <div class="flag">
            {FLAG}
        </div>
    </div>
</body>
</html>
"""


@app.route("/")
def index():
    role = request.cookies.get("role", "user")

    if role == "admin":
        return HTML_ADMIN

    response = make_response(HTML_USER)

    if "role" not in request.cookies:
        response.set_cookie("role", "user")

    return response


@app.route("/admin")
def admin():
    role = request.cookies.get("role", "user")

    if role == "admin":
        return HTML_ADMIN

    return """
    <h1>Access Denied</h1>
    <p>Administrator privileges required.</p>
    """, 403


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
