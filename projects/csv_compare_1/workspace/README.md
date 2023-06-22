I will be using Python with Flask for the web app and pandas for CSV file manipulation. Here are the core classes, functions, and methods that will be necessary:

1. `app.py`: Entry point for the Flask web app
   - `index()`: Renders the main page with file selection and submit button
   - `upload_files()`: Handles file uploads and initiates the comparison process
   - `compare_files()`: Compares the uploaded CSV files and returns the differences
   - `export_results()`: Exports the comparison results in the selected format (CSV, PDF, or Word)

2. `templates/index.html`: Main HTML template for the web app
   - File selection functionality
   - Submit button
   - Console window for progress and interaction
   - Placeholder for logo

3. `static/css/styles.css`: CSS styles for the web app

4. `requirements.txt`: Lists the required Python packages

5. `README.md`: Provides instructions for installation and usage

Now, I will provide the content of each file.

app.py
