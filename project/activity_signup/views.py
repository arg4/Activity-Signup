# Imports
from flask import render_template, Blueprint, request, redirect, url_for, flash
from project import db

from project.models import Employee
from .forms import AddEmployeeForm

# Config
activity_blueprint = Blueprint('activity_signup', __name__, template_folder='templates')

# Routes
@activity_blueprint.route('/', methods=['GET', 'POST'])
def add_employee():
    form = AddEmployeeForm(request.form)
    if request.method == 'POST':
         if form.validate_on_submit():
            new_employee = Employee(form.first_name.data,
                                    form.last_name.data,
                                    form.email_address.data,
                                    form.activity.data,
                                    form.comments.data)
            db.session.add(new_employee)
            db.session.commit()
            flash('New Employee, {} {}, added!'.format(new_employee.first_name, new_employee.last_name), 'success')
            return redirect(url_for('activity_signup.list'))
         else:
             flash_errors(form)
             flash('ERROR! Employee was not added.', 'error')

    # If Method == GET
    return render_template('add_employee.html', form=form)


@activity_blueprint.route('/list')
def list():
    all_employees = Employee.query.all()
    return  render_template('employee.html', employees=all_employees)
