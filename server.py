from flask import Flask, send_from_directory, redirect, url_for

app = Flask(__name__)

# --- Redirect the root URL directly to the PDF ---
@app.route("/")
def index():
    # When someone opens the site, redirect straight to the PDF
    return redirect(url_for('serve_pdf'))

# --- Serve the PDF file ---
@app.route("/pdf")
def serve_pdf():
    # Opens the PDF directly in the browser (no forced download)
    return send_from_directory(".", "Iprochem_Kovkaz_LLC_Landing_Final.pdf")

# --- Main entry point ---
if __name__ == "__main__":
    print("✅ Iprochem Kovkaz PDF server running at http://localhost:8080")
    app.run(host="0.0.0.0", port=8080)


