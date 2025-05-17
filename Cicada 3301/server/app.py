from flask import Flask, send_file, render_template_string, request

app = Flask(__name__)

# Desafio 1: Information Disclosure
@app.route('/poem1')
def serve_poem1():
    return send_file('challenges/Poem1/Poem1.html')

# Vulnerabilidade intencional: .git exposto
@app.route('/poem1/.git/<path:filename>')
def git_access(filename):
    return send_file(f'challenges/Poem1/.git/{filename}')

# Desafio 2: XSS
@app.route('/poem2', methods=['GET', 'POST'])
def xss_challenge():
    if request.method == 'POST':
        return render_template_string(f'<output>{request.form["input"]}</output>')
    return send_file('challenges/Poem2/Poem2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
