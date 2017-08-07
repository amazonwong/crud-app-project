import csv


def enlarge(i):
    return i * 100

def run():
    products = []

    csv_file_path = "data/products.csv"
    headers = ["id", "name", "aisle", "department", "price"]
    user_input_headers = [header for header in headers if header != "id"]

    def get_product_id(product):
        return int(product["id"])

    def auto_incremented_id():
        product_ids = map(get_product_id, products)
        return max(product_ids) + 1

    #
    # READ PRODUCTS FROM FILE
    #

    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ordered_dict in reader:
            products.append(dict(ordered_dict))

    #
    # USER INPUT FUNCTIONS
    #

    def list_product():
        print("THERE ARE " + str(len(products)) + " PRODUCTS:")
        for product in products:
            print(" + ", product)
        return (products)

    def show_product():
        product_id = input("OK. Please specify the product's identifier: ")
        product = [p for p in products if p["id"] == product_id][0]
        if product_id:
            print("SHOWING A PRODUCT HERE!" + "\n", product)
        else:
            print("COULDN'T FIND A PRODUCT WITH THIS IDENTIFIER", product)

    def create_product():
        print("OK. Please specify the product's information...")
        product = {"id": auto_incremented_id() }
        for header in user_input_headers:
            product[header] = input("The '{0}' is: ".format(header))
        print("CREATING A NEW PRODUCT HERE!" + "\n", product)
        products.append(product)

    def update_product():
        product_id = input("OK. Please specify the product's identifier: ")
        product = [p for p in products if p["id"] == product_id][0]
        if product:
            print("OK. Please specify the product's information...")
            for header in user_input_headers:
                product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
            print("UPDATING A PRODUCT HERE!", product)
        else:
            print("COULDN'T FIND A PRODUCT WITH THIS IDENTIFIER", product_id)

    def destroy_product():
        product_id = input("OK. Please specify the product's identifier: ")
        product = [p for p in products if p["id"] == product_id][0]
        if product:
            print("DESTROYING A PRODUCT HERE!", product)
            del products[products.index(product)]
        else:
            print("COULDN'T FIND A PRODUCT WITH THIS IDENTIFIER", product_id)

    #
    # INTRO
    #

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

    if chosen_operation == "List": list_product()
    elif chosen_operation == "Show": show_product()
    elif chosen_operation == "Create": create_product()
    elif chosen_operation == "Update": update_product()
    elif chosen_operation == "Destroy": destroy_product()
    else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

    #
    # WRITE PRODUCTS TO FILE
    #

    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()

        for product in products:
            writer.writerow(product)

if __name__ == "__main__": # "if this script is run from the command-line"
    run()
