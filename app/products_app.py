# CRUD APP PROJECT

# READ PRODUCTS CSV
import operator
import csv

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

print("\n" + "-------------------------------")
print("PRODUCTS APPLICATION")
print("-------------------------------")
print("Welcome @amazonwong" + "\n")

menu = """There are {0} products in the database. Please select an operation:

    Operation  |  Description
    ---------  |  -----------------
    'List'     |  Display a list of product identifiers and name.
    'Show'     |  Show information about a product.
    'Create'   |  Add a new product.
    'Update'   |  Edit an existing product.
    'Destroy'  |  Delete an existing product.

""".format(len(products))

chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

def list_product():
    print("""THERE ARE " + str(len(products)) "PRODUCTS:""")
    for product in products:
        print(product)

def show_product():
        product_id = input("OK. Please specify the product's identifier: ")
        if product_id:
            print("SHOWING A PRODUCT HERE!")
        else:
            product_ids.append(int(product_id))


def create_product():
    print("OK. Please specify the product's information...")
    product_id = input("id:")
    product_name = input("name:")
    product_aisle = input("aisle:")
    product_department = input("department:")
    product_price = input("price:")
    new_product = {
        "id": product_id,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("CREATING A NEW PRODUCT HERE!", new_product)
    products.append(new_product)

def update_product():
    product_id = input("OK. Please specify the product's identifier: ")
    if product_id:
        print("SHOWING A PRODUCT HERE!")
    else:
        product_ids.append(int(product_id))

    print("OK. Please specify the product's information...")
    product_id = input("id:")
    product_name = input("name:")
    product_aisle = input("aisle:")
    product_department = input("department:")
    product_price = input("price:")
    new_product = {
        "id": product_id,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("CREATING A NEW PRODUCT HERE!", new_product)
    products.append(new_product)
def destroy_product():
    product_id = input("OK. Please specify the product's identifier: ")
    if product_id:
        print("DESTROYING A PRODUCT HERE!")
    else:
        product_ids.append(int(product_id))



if chosen_operation == "List": list_product()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product
elif chosen_operation == "Destroy": destroy_product
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")


#print("THERE ARE " + str(len(products)) + " PRODUCTS:")

#products = sorted(products, key=operator.itemgetter('name'))

#for product in products:
    #price_usd = ' (${0:.2f})'.format(product["price"])
    #print(" + " + product["name"] + price_usd)




# example of manipulating/changing the products list
#example_new_product = {"id": 100, "name": "New Item", "aisle": "snacks", "department": "snacks", "price":1.99}
#products.append(example_new_product)


#other_path = "data/other_products.csv"
#with open(other_path, "w") as csv_file:
    #writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    #writer.writeheader() # uses fieldnames set above
    #for product in products:
        #writer.writerow(product)









    #writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
    #writer.writeheader() # uses fieldnames set above
    #writer.writerow({"city": "New York", "name": "Yankees"})
    #writer.writerow({"city": "New York", "name": "Mets"})
    #writer.writerow({"city": "Boston", "name": "Red Sox"})
    #writer.writerow({"city": "New Haven", "name": "Ravens"})
