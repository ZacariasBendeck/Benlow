from app import app
from flask import Flask, render_template, url_for, request
from flask import redirect, flash, jsonify
from import_file_helpers import *


import csv, os

print 'The server has reloaded!!!'



header, data = import_file('ZAPATOSDAMA.CSV')
vendor_header, vendor_data = import_file('VENDORMTDVSPRIOR.CSV')
# data1, data2 = import_file_sort_top_10('DEPARTMENTMTDVSPRIOR.CSV')


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
    header, data = import_file('ZAPATOSDAMA.CSV')
    return render_template('datatables.html', data=data,
                header=header,
                scripts='tables_scripts')

@app.route("/monicadatatables")
def monicadatatables():
    header, data = import_file('REPORTEMAMI.CSV')
    return render_template('datatables.html', data=data,
                header=header,
                scripts='tables_scripts')


@app.route("/monicadatatablesU")
def monicadatatablesU():
    header, data = import_file('MAMIMTDU.CSV')
    title = 'MONICA TEMPORADA U OTONO 2015'
    return render_template('datatables.html',
                data=data, header=header,
                scripts='tables_scripts',
                title=title)

@app.route("/monicadatatablesV")
def monicadatatablesV():
    header,data = import_file('MAMIMTDV.CSV')
    title = 'MONICA TEMPORADA V NAVIDAD 2015'
    return render_template('datatables.html',
                data=data, header=header,
                scripts='tables_scripts',
                title=title)




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
    return render_template('hchartable.html',
        data=vendor_data, header=vendor_header,
        data2=dept_by_month, header2=dept_header,
        scripts=hchartable)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"