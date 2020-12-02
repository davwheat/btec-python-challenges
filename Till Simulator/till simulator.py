class Product:
    def __init__(self, name, price, skuCode):
        self.name = name
        self.price = price
        self.skuCode = skuCode


def GetProductIndex(sku):
    thisProduct = None

    index = 0
    for product in AllProducts:
        if product.skuCode == sku:
            thisProduct = product
            break
        index += 1

    if thisProduct == None:
        return -1
    else:
        return index


def SaveAllProducts():
    global AllProducts

    lines = []

    for product in AllProducts:
        lines.append("[PRODUCT]\n")
        lines.append(f"name={product.name}\n")
        lines.append(f"price={product.price}\n")
        lines.append(f"sku={product.skuCode}\n")

    with open("./products.dat", "w") as f:
        f.writelines(lines)


def GetAllProducts():
    global IS_DEBUG_ENABLED
    allProducts = []

    def AddProduct(name, price, skuCode):
        global IS_DEBUG_ENABLED
        allProducts.append(Product(name, price, skuCode))
        if IS_DEBUG_ENABLED:
            print(f"DEBUG: Added product '{name}' (SKU: {skuCode}) at £{price}")
        name = price = skuCode = ""

    with open("./products.dat", "r") as f:
        raw = f.read()
        lines = raw.splitlines(False)

        name = ""
        price = ""
        skuCode = ""

        lineNumber = 0
        for l in lines:
            lineNumber += 1

            if l.startswith("[PRODUCT]"):
                # new product!
                if name != "" and price != "" and skuCode != "":
                    # if we have valid entries for all fields...
                    AddProduct(name, price, skuCode)
                else:
                    # we have invalid fields -- ignore product and reset values
                    name = price = skuCode = ""

                    # Don't warn when we start the loop
                    if lineNumber != 1:
                        print(f"WARN: Invalid product detected at line {lineNumber}")
            elif l.startswith("name="):
                # product name
                name = l[5:]
            elif l.startswith("price="):
                # product price
                price = l[6:]
            elif l.startswith("sku="):
                # product sku
                skuCode = l[4:]

        # We need to add the last product to the list
        if name != "" and price != "" and skuCode != "":
            AddProduct(name, price, skuCode)

        return allProducts


def ModeSelect():
    global Mode
    global IS_DEBUG_ENABLED
    global shouldExit

    chosenMode = ShowMenu(
        "Choose the mode the till should operate in.",
        "Choose mode:",
        ["Trading mode", "Admin mode", "Exit"],
    )

    if chosenMode == 1:
        Mode = "Trading"
    elif chosenMode == 2:
        Mode = "Admin"
    else:
        shouldExit = True

    if IS_DEBUG_ENABLED:
        print(f"DEBUG: Chosen mode is {Mode}")


def ShowMenu(description, prompt, options):
    m = "-1"

    # if the chosen option isn't in the valid range of options
    while not m in [str(x) for x in range(1, len(options) + 1)]:
        print(description)
        print("")

        # print all options, starting with number 1
        stepNum = 1
        for opt in options:
            print(f"{stepNum}. {opt}")
            stepNum += 1

        print("")
        m = input(prompt + " ")

    # return selected option as int, indexed from 1 and NOT 0!
    return int(m)


def AdminMode():
    global AllProducts

    def ViewCatalogue():
        index = 1
        for product in AllProducts:
            print("==============")
            print(f"Product #{index}")
            print(f"Product name: {product.name}")
            print(f"       Price: £{product.price}")
            print(f"    SKU Code: {product.skuCode}")
            index += 1
        print("==============\n\n")

    def AddProduct():
        name = input("Enter product name: ")
        price = input("Enter product price: £")
        skuCode = input("Enter product SKU: ")

        AllProducts.append(Product(name, price, skuCode))
        SaveAllProducts()

        print("\nAdded new product and saved changes to products.dat!\n\n")

    def DeleteProduct():
        skuCode = input("Enter SKU to delete: ")

        index = 0
        for product in AllProducts:
            if product.skuCode == skuCode:
                AllProducts.pop(index)
                break
            index += 1

        SaveAllProducts()

    def EditProduct():
        skuCode = input("Enter SKU to edit: ")

        thisProduct = None

        index = 0
        for product in AllProducts:
            if product.skuCode == skuCode:
                thisProduct = product
                AllProducts.pop(index)
                break
            index += 1

        if thisProduct == None:
            print("Invalid SKU code!")
            return

        print(f"Current name: {thisProduct.name}")
        print(f"Current price: {thisProduct.price}")

        newName = input("Enter new name: ")
        newPrice = input("Enter new price: ")

        AllProducts.append(Product(newName, newPrice, product.skuCode))

        SaveAllProducts()

    while True:
        chosenOption = ShowMenu(
            "ADMIN MODE",
            "Task:",
            [
                "View product catalogue",
                "Add new product",
                "Edit existing product",
                "Delete product",
                "Change mode",
            ],
        )

        if chosenOption == 1:
            ViewCatalogue()
        elif chosenOption == 2:
            AddProduct()
        elif chosenOption == 3:
            EditProduct()
        elif chosenOption == 4:
            DeleteProduct()
        elif chosenOption == 5:
            # Change mode
            return


def TradingMode():
    global AllProducts

    currentPriceTotal = 0
    isCheckout = False

    while not isCheckout:
        print(f"Current total £{currentPriceTotal}\n")
        sku = input("Enter a SKU, or ENTER to complete transaction\n$ ")

        if sku == "":
            isCheckout = True
            break

        index = GetProductIndex(sku)

        print(f"Product: {AllProducts[index].name}")
        print(f"Price: {AllProducts[index].price}\n")

        currentPriceTotal += float(AllProducts[index].price)

    print("=============")
    print(f"Total: £{currentPriceTotal}")
    paid = float(input("Amount paid: £"))
    print(f"\nChange: £{paid - currentPriceTotal}\n\n")

    TradingMode()


IS_DEBUG_ENABLED = True
AllProducts = GetAllProducts()
# Mode that the till is currently in
# Either "Trading" or "Admin"
Mode = "None"


ModeSelect()

shouldExit = False
while not shouldExit:
    print("\n\n")
    if Mode == "Admin":
        AdminMode()
    elif Mode == "Trading":
        TradingMode()
    else:
        exit()

    ModeSelect()
