from flask import Flask, render_template, url_for, request
from flask import redirect, flash, jsonify
from import_file_helpers import *

import csv, os

app = Flask(__name__)


data = []
data_file = open('ZAPATOSDAMA.CSV')
data_file_reader = csv.reader(data_file)
for row in data_file_reader:
    if data_file_reader.line_num != 1:
        data.append(row)
    else:
        header = row

vendor_data = []
data_file = open('VENDORMTDVSPRIOR.CSV')
data_file_reader = csv.reader(data_file)
for row in data_file_reader:
    if data_file_reader.line_num != 1:
        vendor_data.append(row)
    else:
        vendor_header = row

dept_by_month = []
data_file = open('PROFITDAMAS.CSV')
data_file_reader = csv.reader(data_file)
for row in data_file_reader:
    if data_file_reader.line_num == 1:
        dept_header = row
    elif data_file_reader.line_num not in [2,3,16]:
        dept_by_month.append(row)



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/datatables")
def datatables():
    return render_template('datatables.html', data=data,
                header=header)


@app.route("/applayout")
def applayout():
    return render_template('applayout.html')

@app.route("/blank_")
def blank_():
    return render_template('blank_.html')

@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/hchartable")
def hchartable():
    header3, data3 = import_file('DEPARTMENTMTDVSPRIOR.CSV')
    return render_template('hchartable.html',
        data=vendor_data, header=vendor_header,
        data2=dept_by_month, header2=dept_header,
        data3=data3, header3=header3)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)