from flask import Flask, render_template, Markup, request
import random
MyApp = Flask(__name__)


@MyApp.route("/")
def template():
	return render_template("index.html")

	
if __name__ == "__main__":
        MyApp.run()
