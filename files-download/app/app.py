import os
from flask import Flask, render_template, send_file, abort

app = Flask(__name__)

# Set the path to the directory containing the PDF files
app.config['PDFS_DIR'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'pdfs'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/downloads')
def downloads():
    # Get the list of PDF files in the directory
    pdfs_dir = app.config['PDFS_DIR']
    pdfs = [f for f in os.listdir(pdfs_dir) if f.endswith('.pdf')]

    # Render the downloads template with the list of PDF files
    return render_template('downloads.html', pdfs=pdfs)

@app.route('/downloads/<path:filename>')
def download_file(filename):
    # Get the path to the PDF file
    pdf_path = os.path.join(app.config['PDFS_DIR'], filename)

    # Return a 404 error if the file doesn't exist
    if not os.path.isfile(pdf_path):
        return abort(404)

    # Return the file as a Flask send_file response
    return send_file(pdf_path, attachment_filename=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
