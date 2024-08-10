from app import app

if __name__ == "__main__":
    debug = app.config["DEBUG"]
    app.run(debug=debug)
