# -*- coding: utf-8 -*-
"""
    flask-fillin-test-app
    ~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2012 by Christoph Heer.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/login-form", methods=["GET", "POST"])
def login_form():
    msg = None
    if request.method == "POST":
        if not 'username' in request.form:
            msg = "Missing username"
        if not 'password' in request.form:
            msg = "Missing password"

        if not msg:
            msg = "Welcome " + request.form.get('username')

    return render_template("login_form.html", msg=msg)

@app.route("/hidden-field-form", methods=["GET", "POST"])
def hidden_field_form():
    msg = None
    if request.method == "POST":
        if not 'hidden_field' in request.form:
            msg = "Missing the hidden field"
        else:
            msg = "Hidden field received"

    return render_template("hidden_field_form.html", msg=msg)

@app.route("/checkbox-field-form", methods=["GET", "POST"])
def checkbox_field_form():
    msg = None
    if request.method == "POST":
        if request.form.get('checkbox_field', False):
            msg = "Checkbox checked"
        else:
            msg = "Checkbox did not check"

    return render_template("checkbox_field_form.html", msg=msg)

@app.route('/link')
def link():
    return render_template('link.html')

if __name__ == "main":
    app.run()
