
from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Inventory page
@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

# Sales page
@app.route('/sales')
def sales():
    return render_template('sales.html')

# Reports page
@app.route('/reports')
def reports():
    return render_template('reports.html')


# Launch the Flask application
if __name__ == '__main__':
    app.run(debug=True)

