### Task
---
Example:
To create an Employee Object Class for our Database via Django REST Framework. The Objective of this task is to expose Employee data for the client.
### Context
---
Example:
An Employee class table is required for the integrity of the database. It provides a primary key that links to two different tables(Employee_In_Training_Program, Employee_Gets_Computer) and a foreign key(Department_Id property) that links to one table(Department). Please refer to the ERD table:[ERD](https://www.draw.io/?state=%7B%22ids%22:%5B%220B-4vZ-mgQ31vc2cxUVVOamFFU2c%22%5D,%22action%22:%22open%22,%22userId%22:%22100761558679069137145%22%7D#G0B-4vZ-mgQ31vc2cxUVVOamFFU2c)
- For more resources on this prodects click [Here]()

### The process 
---
Example: (Checkbox content will change depending on ticket requirements)
- [ ] Pull Down Bangazon Project onto your local computer and create a new git branch

-  [ ] Go to the Bangazon directory 

- [ ] Go to the API app

- [ ] Create the Employee Class in the models.py file with the properties required: Employee_ID(PK), DepartmentID(FK). First_Name, Last_Name, Is_Supervisor (True=1, False=0)

- [ ] Create a viewset Class for the Employee Table in the views.py file.

-  [ ] Create a class that displays the specific attributes of the Employee class in the serializers.py file 

- [ ] add the employee class url extension "/employee" in the urls.py file

### Outcome/expected behavior
---
Example:
In all, 4 files will be changed. After these changes, the Class created will be ready to migrate using the Django REST framework. The outcome of the migrated files will expose the Employee Class that can also be linked to the other data tables in the database. 
