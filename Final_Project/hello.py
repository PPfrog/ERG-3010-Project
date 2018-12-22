from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length
import pymysql
from des import des
from check import search
import datetime




# Search Form
class searchForm(FlaskForm):
    plane_id = StringField('Plane ID', validators=[DataRequired(), Length(min = 6, max = 6)])
    search = SubmitField('Search')

# Select Form
class selectForm(FlaskForm):
    start_date = DateField('Start Date', format='%Y-%m-%d')
    end_date = DateField('End Date', format='%Y-%m-%d')
    select = SubmitField('Select')


    


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsASecretKey'



@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# ============Dashboard page========

@app.route('/')
@app.route('/dashboard')
def dashboard():
    search_dash = search()
    flight_time = search_dash.dash_board_one()
    cycle_time = search_dash.dash_board_two()
    flight_time_rank, utilization_rate_rank, failure_rate_rank = search_dash.dash_board_three()
    warning_plane = search_dash.dash_board_four()
    return render_template('dashboard.html', title = 'Dashboard', welcome = True, flight_time = flight_time, cycle_time = cycle_time, flight_time_rank = flight_time_rank, utilization_rate_rank = utilization_rate_rank, failure_rate_rank = failure_rate_rank, warning_plane = warning_plane)

# ============About page========

@app.route('/about')
def about():
    return render_template('template.html', title = 'About')

# ============Fleet page========

@app.route('/fleet/<string:fleetname>')
def fleet_details(fleetname):
    search_fleet = search(fleetName = fleetname)
    plane_name_list = search_fleet.find_all_plane_new()
    fleet_data = search_fleet.find_fleet_data()
    return render_template('fleet_details.html', title = 'Fleet', fleetname = fleetname, des = des[fleetname], plane_name_list = plane_name_list, fleet_data = fleet_data)

# ============Plane page========

@app.route('/plane', methods=['GET', 'POST'])
def plane():
    form = searchForm()
    search_plane = search(id = form.plane_id.data)
    if search_plane.check_exist():
        return redirect(url_for('plane_details_main', planename = form.plane_id.data))
    elif form.plane_id.data: 
        return render_template('plane.html', title = 'Plane', form = form, error = True)
    return render_template('plane.html', title = 'Plane', form = form, error = False)

@app.route('/plane/<string:planename>')
@app.route('/plane/<string:planename>/main')
def plane_details_main(planename):
    search_plane = search(id = planename)
    basic_data = search_plane.find_basic_data()
    return render_template('plane_details_main.html', title = 'Plane', planename = planename, basic_data = basic_data, right_navi = True)

@app.route('/plane/<string:planename>/performance', defaults={'page':1},  methods=['GET', 'POST'])
@app.route('/plane/<string:planename>/performance/<int:page>', methods=['GET', 'POST'])
def plane_details_performance(planename, page):
    search_perform = search(id = planename)
    left_engine, right_engine = search_perform.engine_info()
    left_engine_level, right_engine_level, warning = search_perform.check_warning()
    return render_template('plane_details_performance.html', title = 'Plane', planename = planename,  right_navi = True, left_engine = left_engine, right_engine = right_engine, left_engine_level = left_engine_level, right_engine_level = right_engine_level, warning = warning)


@app.route('/plane/<string:planename>/maintenance', defaults={'page':1},  methods=['GET', 'POST'])
@app.route('/plane/<string:planename>/maintenance/<int:page>', methods=['GET', 'POST'])
def plane_details_maintenance(planename, page):
    form = selectForm()
    start_date = end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    if form.validate_on_submit():
        start_date = form.start_date.data
        end_date = form.end_date.data
    search_plane = search(id = planename)
    detail_data, num_of_pages, col_names = search_plane.find_maintenance_record(page)
    if num_of_pages:
        page = num_of_pages
    return render_template('plane_details_maintenance.html', title = 'Plane', planename = planename,  detail_data = detail_data, right_navi = True, form = form, start_date = start_date, end_date = end_date, page = page, col_names = col_names)



@app.route('/plane/<string:planename>/flight', defaults={'page':1},  methods=['GET', 'POST'])
@app.route('/plane/<string:planename>/flight/<int:page>', methods=['GET', 'POST'])
def plane_details_flight(planename, page):
    form = selectForm()
    start_date = end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    if form.validate_on_submit():
        start_date = form.start_date.data
        end_date = form.end_date.data
    search_plane = search(id = planename)
    detail_data, num_of_pages, col_names = search_plane.find_fly_record(page)
    if num_of_pages:
        page = num_of_pages
    return render_template('plane_details_flight.html', title = 'Plane', planename = planename,  detail_data = detail_data, right_navi = True, form = form, start_date = start_date, end_date = end_date, page = page, col_names = col_names)

@app.route('/plane/<string:planename>/fault', defaults={'page':1},  methods=['GET', 'POST'])
@app.route('/plane/<string:planename>/fault/<int:page>', methods=['GET', 'POST'])
def plane_details_fault(planename, page):
    form = selectForm()
    start_date = end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    if form.validate_on_submit():
        start_date = form.start_date.data
        end_date = form.end_date.data
    search_plane = search(id = planename)
    detail_data, num_of_pages, col_names = search_plane.find_error_record(page)
    if num_of_pages:
        page = num_of_pages
    return render_template('plane_details_fault.html', title = 'Plane', planename = planename,  detail_data = detail_data, right_navi = True, form = form, start_date = start_date, end_date = end_date, page = page, col_names = col_names)


# ============Diagram page========

@app.route('/diagram')
def diagram():
    return render_template('diagram.html', title = 'Diagram')