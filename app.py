from flask import Flask, request, send_file, render_template
import pdfkit
import tempfile

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/html-to-pdf', methods=['POST'])
def html_to_pdf():
    html_content = request.data.decode()
    try:
        temp = tempfile.NamedTemporaryFile(delete=False)
        pdfkit.from_string(html_content, temp.name, options={'quiet': ''})
        return send_file(temp.name, mimetype='application/pdf', as_attachment=True)
    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
