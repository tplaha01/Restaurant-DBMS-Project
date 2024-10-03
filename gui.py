import tkinter as tk
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
        result_text.insert(tk.END, "Query executed successfully.\n\n")
    except Exception as e:
        db.rollback()
        result_text.insert(tk.END, f"Error: {str(e)}\n\n")


def execute_select_query(sql):
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                result_text.insert(tk.END, f"{row}\n")
        else:
            result_text.insert(tk.END, "No records found.\n")
        result_text.insert(tk.END, "\n")
    except Exception as e:
        result_text.insert(tk.END, f"Error: {str(e)}\n\n")


def execute_insert_query(table, values):
    sql = f"INSERT INTO {table} VALUES {values}"
    execute_query(sql)


def execute_update_query(table, attributes, values, condition):
    set_values = ", ".join([f"{attr} = {val}" for attr, val in zip(attributes, values)])
    sql = f"UPDATE {table} SET {set_values} WHERE {condition}"
    execute_query(sql)


def execute_delete_query(table, condition):
    sql = f"DELETE FROM {table} WHERE {condition}"
    execute_query(sql)


def assign_random_waiter(customer_id):
    query = "SELECT waiter_id FROM waiter"
    cursor.execute(query)
    waiters = cursor.fetchall()
    if waiters:
        waiter_id = choice(waiters)[0]
        attends_values = f"('{waiter_id}', '{customer_id}')"
        execute_insert_query("attends", attends_values)


def show_customers():
    # Execute SELECT query for customers table
    query = "SELECT * FROM customer"
    execute_select_query(query)


def show_waiters():
    # Execute SELECT query for waiters table
    query = "SELECT * FROM waiter"
    execute_select_query(query)


def show_dishes():
    # Execute SELECT query for dishes table
    query = "SELECT * FROM dish"
    execute_select_query(query)


def show_chefs():
    # Execute SELECT query for chefs table
    query = "SELECT * FROM chef"
    execute_select_query(query)


def insert_customer():
    # Execute INSERT query for customers table
    customer_id = customer_id_entry.get()
    customer_name = customer_name_entry.get()
    customer_contact = customer_contact_entry.get()
    values = f"('{customer_id}', '{customer_name}', '{customer_contact}')"
    execute_insert_query("customer", values)
    assign_random_waiter(customer_id)


def insert_waiter():
    # Execute INSERT query for waiters table
    waiter_id = waiter_id_entry.get()
    waiter_name = waiter_name_entry.get()
    waiter_salary = waiter_salary_entry.get()
    values = f"('{waiter_id}', '{waiter_name}', {waiter_salary})"
    execute_insert_query("waiter", values)


def insert_dish():
    # Execute INSERT query for dishes table
    dish_id = dish_id_entry.get()
    dish_name = dish_name_entry.get()
    price = price_entry.get()
    values = f"('{dish_id}', '{dish_name}', {price})"
    execute_insert_query("dish", values)


def insert_chef():
    # Execute INSERT query for chefs table
    chef_id = chef_id_entry.get()
    chef_name = chef_name_entry.get()
    chef_salary = chef_salary_entry.get()
    values = f"('{chef_id}', '{chef_name}', {chef_salary})"
    execute_insert_query("chef", values)


def update_customer():
    # Execute UPDATE query for customers table
    customer_id = customer_id_entry.get()
    customer_name = customer_name_entry.get()
    customer_contact = customer_contact_entry.get()
    attributes = ["customer_name", "customer_contact"]
    values = [f"'{customer_name}'", f"'{customer_contact}'"]
    condition = f"customer_id = '{customer_id}'"
    execute_update_query("customer", attributes, values, condition)


def update_waiter():
    # Execute UPDATE query for waiters table
    waiter_id = waiter_id_entry.get()
    waiter_name = waiter_name_entry.get()
    waiter_salary = waiter_salary_entry.get()
    attributes = ["waiter_name", "waiter_salary"]
    values = [f"'{waiter_name}'", waiter_salary]
    condition = f"waiter_id = '{waiter_id}'"
    execute_update_query("waiter", attributes, values, condition)


def update_dish():
    # Execute UPDATE query for dishes table
    dish_id = dish_id_entry.get()
    dish_name = dish_name_entry.get()
    price = price_entry.get()
    attributes = ["dish_name", "price"]
    values = [f"'{dish_name}'", price]
    condition = f"dish_id = '{dish_id}'"
    execute_update_query("dish", attributes, values, condition)


def update_chef():
    # Execute UPDATE query for chefs table
    chef_id = chef_id_entry.get()
    chef_name = chef_name_entry.get()
    chef_salary = chef_salary_entry.get()
    attributes = ["chef_name", "chef_salary"]
    values = [f"'{chef_name}'", chef_salary]
    condition = f"chef_id = '{chef_id}'"
    execute_update_query("chef", attributes, values, condition)


def delete_customer():
    # Execute DELETE query for customers table
    customer_id = customer_id_entry.get()
    condition = f"customer_id = '{customer_id}'"
    execute_delete_query("customer", condition)


def delete_waiter():
    # Execute DELETE query for waiters table
    waiter_id = waiter_id_entry.get()
    condition = f"waiter_id = '{waiter_id}'"
    execute_delete_query("waiter", condition)


def delete_dish():
    # Execute DELETE query for dishes table
    dish_id = dish_id_entry.get()
    condition = f"dish_id = '{dish_id}'"
    execute_delete_query("dish", condition)


def delete_chef():
    # Execute DELETE query for chefs table
    chef_id = chef_id_entry.get()
    condition = f"chef_id = '{chef_id}'"
    execute_delete_query("chef", condition)


def calculate_total_bill():
    # Execute SELECT query to calculate the total bill for a customer
    customer_id = customer_id_entry.get()
    query = f"SELECT SUM(d.price) " \
            f"FROM customer c " \
            f"JOIN orders o ON c.customer_id = o.customer_customer_id " \
            f"JOIN dish d ON o.dish_dish_id = d.dish_id " \
            f"WHERE c.customer_id = '{customer_id}' " \
            f"GROUP BY c.customer_id"
    execute_select_query(query)


def clear_output():
    result_text.delete('1.0', tk.END)


# Create the main application window
root = tk.Tk()
root.title("Restaurant Management System")

# Create buttons to show records for each table
show_customers_btn = tk.Button(root, text="Show Customers", command=show_customers)
show_customers_btn.grid(row=0, column=3, padx=5, pady=5)
show_waiters_btn = tk.Button(root, text="Show Waiters", command=show_waiters)
show_waiters_btn.grid(row=3, column=3, padx=5, pady=5)
show_dishes_btn = tk.Button(root, text="Show Dishes", command=show_dishes)
show_dishes_btn.grid(row=6, column=3, padx=5, pady=5)
show_chefs_btn = tk.Button(root, text="Show Chefs", command=show_chefs)
show_chefs_btn.grid(row=9, column=3, padx=5, pady=5)

# Create labels for input fields
customer_id_label = tk.Label(root, text="Customer ID:")
customer_id_label.grid(row=0, column=0, sticky=tk.W)
customer_name_label = tk.Label(root, text="Customer Name:")
customer_name_label.grid(row=1, column=0, sticky=tk.W)
customer_contact_label = tk.Label(root, text="Customer Contact:")
customer_contact_label.grid(row=2, column=0, sticky=tk.W)
waiter_id_label = tk.Label(root, text="Waiter ID:")
waiter_id_label.grid(row=3, column=0, sticky=tk.W)
waiter_name_label = tk.Label(root, text="Waiter Name:")
waiter_name_label.grid(row=4, column=0, sticky=tk.W)
waiter_salary_label = tk.Label(root, text="Waiter Salary:")
waiter_salary_label.grid(row=5, column=0, sticky=tk.W)
dish_id_label = tk.Label(root, text="Dish ID:")
dish_id_label.grid(row=6, column=0, sticky=tk.W)
dish_name_label = tk.Label(root, text="Dish Name:")
dish_name_label.grid(row=7, column=0, sticky=tk.W)
price_label = tk.Label(root, text="Price:")
price_label.grid(row=8, column=0, sticky=tk.W)
chef_id_label = tk.Label(root, text="Chef ID:")
chef_id_label.grid(row=9, column=0, sticky=tk.W)
chef_name_label = tk.Label(root, text="Chef Name:")
chef_name_label.grid(row=10, column=0, sticky=tk.W)
chef_salary_label = tk.Label(root, text="Chef Salary:")
chef_salary_label.grid(row=11, column=0, sticky=tk.W)

# Create input fields for user input
customer_id_entry = tk.Entry(root)
customer_id_entry.grid(row=0, column=1)
customer_name_entry = tk.Entry(root)
customer_name_entry.grid(row=1, column=1)
customer_contact_entry = tk.Entry(root)
customer_contact_entry.grid(row=2, column=1)
waiter_id_entry = tk.Entry(root)
waiter_id_entry.grid(row=3, column=1)
waiter_name_entry = tk.Entry(root)
waiter_name_entry.grid(row=4, column=1)
waiter_salary_entry = tk.Entry(root)
waiter_salary_entry.grid(row=5, column=1)
dish_id_entry = tk.Entry(root)
dish_id_entry.grid(row=6, column=1)
dish_name_entry = tk.Entry(root)
dish_name_entry.grid(row=7, column=1)
price_entry = tk.Entry(root)
price_entry.grid(row=8, column=1)
chef_id_entry = tk.Entry(root)
chef_id_entry.grid(row=9, column=1)
chef_name_entry = tk.Entry(root)
chef_name_entry.grid(row=10, column=1)
chef_salary_entry = tk.Entry(root)
chef_salary_entry.grid(row=11, column=1)

# Create buttons to perform CRUD operations for each table
customer_btn_frame = tk.Frame(root)
customer_btn_frame.grid(row=0, column=2)
insert_customer_btn = tk.Button(customer_btn_frame, text="Insert", command=insert_customer)
insert_customer_btn.grid(row=0, column=0, padx=5, pady=5)
update_customer_btn = tk.Button(customer_btn_frame, text="Update", command=update_customer)
update_customer_btn.grid(row=0, column=1, padx=5, pady=5)
delete_customer_btn = tk.Button(customer_btn_frame, text="Delete", command=delete_customer)
delete_customer_btn.grid(row=0, column=2, padx=5, pady=5)

waiter_btn_frame = tk.Frame(root)
waiter_btn_frame.grid(row=3, column=2)
insert_waiter_btn = tk.Button(waiter_btn_frame, text="Insert", command=insert_waiter)
insert_waiter_btn.grid(row=0, column=0, padx=5, pady=5)
update_waiter_btn = tk.Button(waiter_btn_frame, text="Update", command=update_waiter)
update_waiter_btn.grid(row=0, column=1, padx=5, pady=5)
delete_waiter_btn = tk.Button(waiter_btn_frame, text="Delete", command=delete_waiter)
delete_waiter_btn.grid(row=0, column=2, padx=5, pady=5)

dish_btn_frame = tk.Frame(root)
dish_btn_frame.grid(row=6, column=2)
insert_dish_btn = tk.Button(dish_btn_frame, text="Insert", command=insert_dish)
insert_dish_btn.grid(row=0, column=0, padx=5, pady=5)
update_dish_btn = tk.Button(dish_btn_frame, text="Update", command=update_dish)
update_dish_btn.grid(row=0, column=1, padx=5, pady=5)
delete_dish_btn = tk.Button(dish_btn_frame, text="Delete", command=delete_dish)
delete_dish_btn.grid(row=0, column=2, padx=5, pady=5)

chef_btn_frame = tk.Frame(root)
chef_btn_frame.grid(row=9, column=2)
insert_chef_btn = tk.Button(chef_btn_frame, text="Insert", command=insert_chef)
insert_chef_btn.grid(row=0, column=0, padx=5, pady=5)
update_chef_btn = tk.Button(chef_btn_frame, text="Update", command=update_chef)
update_chef_btn.grid(row=0, column=1, padx=5, pady=5)
delete_chef_btn = tk.Button(chef_btn_frame, text="Delete", command=delete_chef)
delete_chef_btn.grid(row=0, column=2, padx=5, pady=5)

# Create a button to calculate the total bill for a customer
calculate_total_bill_btn = tk.Button(root, text="Calculate Total Bill", command=calculate_total_bill)
calculate_total_bill_btn.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

# Create a text widget to display the result
result_text = tk.Text(root, width=50, height=10)
result_text.grid(row=13, column=0, columnspan=4, padx=5, pady=5)

# Create a button to clear the output
clear_output_btn = tk.Button(root, text="Clear Output", command=clear_output)
clear_output_btn.grid(row=14, column=0, columnspan=4, padx=5, pady=5)

# Run the main event loop
root.mainloop()
