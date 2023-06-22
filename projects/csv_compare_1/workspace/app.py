from flask import Flask, render_template, request, send_file
import pandas as pd
import io
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    file1 = request.files['file1']
    file2 = request.files['file2']
    df1 = pd.read_csv(file1, encoding='utf-8')
    df2 = pd.read_csv(file2, encoding='utf-8')
    result = compare_files(df1, df2)
    return result.to_html()

def compare_files(df1, df2):
    common_columns = set(df1.columns) & set(df2.columns)
    common_columns.discard('Column ID')
    df1.set_index('Column ID', inplace=True)
    df2.set_index('Column ID', inplace=True)
    differences = df1[common_columns].compare(df2[common_columns])
    return differences

@app.route('/export', methods=['POST'])
def export_results():
    export_format = request.form['export_format']
    differences = request.form['differences']
    if export_format == 'csv':
        return export_csv(differences)
    elif export_format == 'pdf':
        return export_pdf(differences)
    elif export_format == 'word':
        return export_word(differences)

def export_csv(differences):
    output = io.StringIO()
    writer = csv.writer(output)
    for row in differences:
        writer.writerow(row)
    output.seek(0)
    return send_file(output, attachment_filename='differences.csv', as_attachment=True)

def export_pdf(differences):
    # Implement PDF export functionality
    pass

def export_word(differences):
    # Implement Word export functionality
    pass

if __name__ == '__main__':
    app.run(debug=True)
