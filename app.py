from flask import Flask, render_template, jsonify
from smart_bin import SmartBin

app = Flask(__name__)

# Create one instance of your bin to hold state while the app runs
bin_device = SmartBin(initial_level=45)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/status")
def status():
    bin_device.simulate_level_change()
    bin_device.simulate_motion()
    return jsonify({
        "bin": bin_device.get_status()
        # add "cleaner": cleaner_device.get_status(), etc. as modules come in
    })

if __name__ == "__main__":
    app.run(debug=True)