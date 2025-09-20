from flask import Flask, render_template, request, redirect, url_for
from terminal.core import Terminal
from terminal.ai_parser import parse_nl_command

app = Flask(__name__)
term = Terminal()
history = []  # store command history

@app.route("/", methods=["GET", "POST"])
def index():
    global history
    if request.method == "POST":
        user_input = request.form.get("command", "").strip()
        if user_input:
            parsed = parse_nl_command(user_input)
            if parsed:
                cmd_to_run = parsed
                history.append(f"$ {user_input}   →   {parsed}")
            else:
                cmd_to_run = user_input
                history.append(f"$ {user_input}")

            try:
                output = term.execute(cmd_to_run)
                if output:
                    for line in output.split("\n"):
                        history.append(line)
            except Exception as e:
                history.append(f"Error: {e}")

        return redirect(url_for("index"))

    return render_template("index.html", history=history)


if __name__ == "__main__":
    app.run(debug=True)
