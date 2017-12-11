from project import db
from project.models import Employee

# create the database
db.create_all()

person1 = Employee('Nathan', 'Grimberg', 'nategrimberg@gmail.com', 'Basketball', '')
db.session.add(person1)

db.session.commit()
