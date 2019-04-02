from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

header = """
    <!DOCTYPE html>
    <html>
        <header>
            <h1>My Awesome Website</h1>
        </header>
"""

signup_body = """
        <body>
            <h2>Signup Sheet</h2>
            <form action="/authenticate" method="post">
                <label>
                    Username: <input type="text" name="username" />
                </label>
                <label>
                    Password: <input type="password" name="password1" />
                </label>
                <label>Re-type Password: 
                    <input type="text" name="password2" />
                </label>
                <label>
                    E-mail Address: <input type="email" name="email" />
                </label>
            </form>
        </body>
"""

footer = """
        <footer>
        <p>The Experience Enterprises</p>
        </footer>
    </html>
"""

@app.route("/")
def index():
    return header + signup_body + footer

@app.route("/authenticate")
def validate():
    return True

app.run()