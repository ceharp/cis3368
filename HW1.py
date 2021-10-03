import mysql.connector
import datetime
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
from datetime import date

#Creating connection to mysql database
conn = create_connection("cis3368.cxqdgumdlo2t.us-east-2.rds.amazonaws.com", "ceharp", "B3ntley3", "cis3368")

#Main function
def menu():
    #creating the "UI" for the menu
    menu_options = ('MENU\n'
        'a - Add item\n'
        'd - Remove item\n'
        'u - Update item details\n'
        'r1 - Output all items in alphabetical order\n'
        'r2 - Output all items by sorted by quantity (ascending)\n'
        'q - Quit\n')

    #Begin line for user input
    print(menu_options)
    option = input('\nChoose an option\n')

    #Adding item option
    if option == 'a':
        print('Add item to cart\n')
        item_description = input('Enter the item description\n')
        item_quantity = int(input('Enter the item quantity\n'))
        #Uses the current date when the item was added
        date_added = datetime.date.today()
        query = "INSERT INTO shoppinglist (item_description, quantity, date_added) VALUES (%s, %s, %s)" % (item_description, item_quantity, date_added)
        execute_query(conn, query) 

    #Item removal option
    elif option == 'd':
        print('Remove item from cart\n')
        id_delete = input('Insert item ID\n')
        delete_statement = "DELETE FROM invoices WHERE id = %s" % (id_delete)
        execute_query(conn, delete_statement)

    elif option == 'u':
        print('Update item details\n')

    #Print items in alphabetical order
    elif option == 'r1':
        cursor.execute("Select * FROM shoppinglist")
        result = cursor.fetchall()
        for row in result:
            print(row)
    
    #Print items by quantity
    elif option == 'r2':
        cursor.execute("Select * FROM shoppinglist")
        result = cursor.fetchall()
        for row in result:
            print(row)
    #Exit script
    elif option == 'q':
        print("Until next time!")
        quit()
    #Response to incorrect input
    else:
        print('Invalid selection')

menu()
