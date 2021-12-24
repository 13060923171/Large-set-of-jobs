#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from data import SourceData


app = Flask(__name__)


@app.route('/')
def index():
    data = SourceData()
    return render_template('index.html', form=data, title=data.title)



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False)
