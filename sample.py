from tkinter import *
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql0114!",
    database="restaurant mangement"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()


def execute_query(sql):
    try:
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("Success", "Query executed successfully.")
    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", str(e))


def execute_select_query(sql):
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)  # Display the results in the console
        else:
            print("No records found.")
    except Exception as e:
        print("Error:", str(e))


def execute_insert_query(table, values):
    sql = "INSERT INTO {} VALUES {}".format(table, values)
    execute_query(sql)


def execute_update_query(table, column, value, condition):
    sql = "UPDATE {} SET {} = {} WHERE {}".format(table, column, value, condition)
    execute_query(sql)


def execute_delete_query(table, condition):
    sql = "DELETE FROM {} WHERE {}".format(table, condition)
    execute_query(sql)


# Create the GUI
root = Tk()
root.title("SQL Database GUI")

# Function to execute SELECT query
def execute_select():
    query = select_entry.get()
    execute_select_query(query)

# Function to execute INSERT query
def execute_insert():
    table = insert_table_entry.get()
    values = insert_values_entry.get()
    execute_insert_query(table, values)

# Function to execute UPDATE query
def execute_update():
    table = update_table_entry.get()
    column = update_column_entry.get()
    value = update_value_entry.get()
    condition = update_condition_entry.get()
    execute_update_query(table, column, value, condition)

# Function to execute DELETE query
def execute_delete():
    table = delete_table_entry.get()
    condition = delete_condition_entry.get()
    execute_delete_query(table, condition)


# Create the SELECT query frame
select_frame = LabelFrame(root, text="SELECT Query")
select_frame.pack(padx=10, pady=10)

select_entry = Entry(select_frame, width=50)
select_entry.grid(row=0, column=0, padx=10, pady=10)

select_button = Button(select_frame, text="Execute", command=execute_select)
select_button.grid(row=0, column=1, padx=10, pady=10)


# Create the INSERT query frame
insert_frame = LabelFrame(root, text="INSERT Query")
insert_frame.pack(padx=10, pady=10)

insert_table_label = Label(insert_frame, text="Table:")
insert_table_label.grid(row=0, column=0, padx=5, pady=5)
insert_table_entry = Entry(insert_frame, width=20)
insert_table_entry.grid(row=0, column=1, padx=5, pady=5)

insert_values_label = Label(insert_frame, text="Values:")
insert_values_label.grid(row=1, column=0, padx=5, pady=5)
insert_values_entry = Entry(insert_frame, width=50)
insert_values_entry.grid(row=1, column=1, padx=5, pady=5)

insert_button = Button(insert_frame, text="Execute", command=execute_insert)
insert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


# Create the UPDATE query frame
update_frame = LabelFrame(root, text="UPDATE Query")
update_frame.pack(padx=10, pady=10)

update_table_label = Label(update_frame, text="Table:")
update_table_label.grid(row=0, column=0, padx=5, pady=5)
update_table_entry = Entry(update_frame, width=20)
update_table_entry.grid(row=0, column=1, padx=5, pady=5)

update_column_label = Label(update_frame, text="Column:")
update_column_label.grid(row=1, column=0, padx=5, pady=5)
update_column_entry = Entry(update_frame, width=20)
update_column_entry.grid(row=1, column=1, padx=5, pady=5)

update_value_label = Label(update_frame, text="Value:")
update_value_label.grid(row=2, column=0, padx=5, pady=5)
update_value_entry = Entry(update_frame, width=20)
update_value_entry.grid(row=2, column=1, padx=5, pady=5)

update_condition_label = Label(update_frame, text="Condition:")
update_condition_label.grid(row=3, column=0, padx=5, pady=5)
update_condition_entry = Entry(update_frame, width=50)
update_condition_entry.grid(row=3, column=1, padx=5, pady=5)

update_button = Button(update_frame, text="Execute", command=execute_update)
update_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


# Create the DELETE query frame
delete_frame = LabelFrame(root, text="DELETE Query")
delete_frame.pack(padx=10, pady=10)

delete_table_label = Label(delete_frame, text="Table:")
delete_table_label.grid(row=0, column=0, padx=5, pady=5)
delete_table_entry = Entry(delete_frame, width=20)
delete_table_entry.grid(row=0, column=1, padx=5, pady=5)

delete_condition_label = Label(delete_frame, text="Condition:")
delete_condition_label.grid(row=1, column=0, padx=5, pady=5)
delete_condition_entry = Entry(delete_frame, width=50)
delete_condition_entry.grid(row=1, column=1, padx=5, pady=5)

delete_button = Button(delete_frame, text="Execute", command=execute_delete)
delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()

# Close the database connection
db.close()
