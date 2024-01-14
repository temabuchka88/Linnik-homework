import sqlalchemy

connection_string = "sqlite:///hw15.sqlite"
engine = sqlalchemy.create_engine(connection_string)
connection = engine.connect()

# connection.execute(sqlalchemy.text("INSERT INTO Departments VALUES(1,'managment');"))
# connection.execute(sqlalchemy.text("INSERT INTO Departments VALUES(2,'HRs');"))
# connection.execute(sqlalchemy.text("INSERT INTO Departments VALUES(3,'sales');"))
# connection.execute(
#     sqlalchemy.text("INSERT INTO Departments VALUES(4,'Software Development');")
# )
# connection.execute(sqlalchemy.text("INSERT INTO Departments VALUES(5,'support');"))
# connection.execute(sqlalchemy.text("INSERT INTO Departments VALUES(6,'RND');"))


# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee(id,name,department_id,role) VALUES(1,'James Smith',1,'CEO');"
#     )
# )
# connection.execute(
#     sqlalchemy.text("INSERT INTO employee VALUES(2,'Sara Goldman',1,'CFO',1);")
# )
# connection.execute(
#     sqlalchemy.text("INSERT INTO employee VALUES(3,'Wayne Albet',1,'CIO',1);")
# )
# connection.execute(
#     sqlalchemy.text("INSERT INTO employee VALUES(4,'Michelle Carey',2,'HR manager',1);")
# )
# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee VALUES(5,'Chris Matthews',3,'sales manager',2);"
#     )
# )
# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee VALUES(6,'Andrew Judy',4,'Development manager',3);"
#     )
# )
# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee VALUES(7,'Daniele McLeon',5,'support manager',3);"
#     )
# )
# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee VALUES(8,'Matthew Swan',2,'HR representative',4);"
#     )
# )
# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee VALUES(9,'Stephanie Richardson',2,'salesperson',5);"
#     )
# )
# connection.execute(
#     sqlalchemy.text("INSERT INTO employee VALUES(10,'Tony Stark',3,'salesperson',5);")
# )
# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee VALUES(11,'Jenna Lockett',4,'Front-end Developer',6);"
#     )
# )
# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee VALUES(12,'Michael Dunstall',4,'Back-end Developer',6);"
#     )
# )
# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee VALUES(13,'Jane Voss',4,'Back-End Developer',6);"
#     )
# )
# connection.execute(
#     sqlalchemy.text(
#         "INSERT INTO employee(id, name,role,manager_id) VALUES(14,'Anthony Hird','support',7);"
#     )
# )
# connection.execute(
#     sqlalchemy.text("INSERT INTO employee VALUES(15,'Natali Rocca',5,'support',7);")
# )

# connection.commit()


query_1 = sqlalchemy.text(
    "SELECT Employee.NAME, Employee.ROLE, Departments.NAME FROM Employee LEFT JOIN Departments ON Employee.DEPARTMENT_ID = Departments.ID;"
)
result_1 = connection.execute(query_1)
for row in result_1:
    print(row)

query_2 = sqlalchemy.text(
    "SELECT NAME FROM Employee WHERE ID = (SELECT MANAGER_ID FROM Employee WHERE NAME = 'Tony Stark');"
)
result_2 = connection.execute(query_2)
for row in result_2:
    print(row)

query_3 = sqlalchemy.text(
    "SELECT Departments.NAME, Employee.NAME FROM Departments OUTER LEFT JOIN Employee ON Departments.ID = Employee.DEPARTMENT_ID;"
)
result_3 = connection.execute(query_3)
for row in result_3:
    print(row)

connection.close()
