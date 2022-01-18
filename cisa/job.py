import json
from flask import Flask
from flask_cors import CORS
from fetch_data import FectchData

app = Flask(__name__, static_url_path="")
CORS(app)

@app.route('/')
def index():
    f = FectchData('https://www.cisa.gov/uscert/ics/advisories')
    f.get_data()
    f.get_all_urls(2)
    final = f.get_data_from_all_links()
    return json.dumps(final)

if __name__ == "__main__":
    app.run(debug=True)