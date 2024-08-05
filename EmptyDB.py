import sqlite3
# Set up connection to database and open a cursor
db = sqlite3.connect("pizza.db")
cursor = db.cursor()
# Save changes to the database and close the cursor

tables = ["Menu", "Ingredient", "Item", "Adjustment", "Request", "Employee", "Customer",
          "Invoice", "DiningTable", "Booking", "MenuIngredient", "MenuItem", "ItemAdjustment"]
for table in tables:
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
    except:
        print(f"Unable to drop: {table}")

#! Menu Table
cursor.execute("""CREATE TABLE Menu (
    MenuID INTEGER Primary Key,
    Name VARCHAR NOT NULL,
    GlutenOption BOOLEAN,
    BasePrice FLOAT,
    Description VARCHAR)
""")

#! Ingredient Table
cursor.execute("""CREATE TABLE Ingredient (
    Name VARCHAR PRIMARY KEY,
    AddPrice FLOAT,
    Quantity INT NOT NULL,
    SupplierName VARCHAR,
    SupplierEmail VARCHAR)""")

#! Item Table
cursor.execute("""CREATE TABLE Item (
    ItemID INTEGER PRIMARY KEY,
    Gluten BOOLEAN,
    Size CHAR,
    Quantity SMALLINT,
    Completed BOOLEAN)""")

#! Adjustment Table
cursor.execute("""CREATE TABLE Adjustment (
    AdjustmentID INTEGER PRIMARY KEY,
    Added BOOLEAN NOT NULL,
    IngredientID INT NOT NULL REFERENCES Ingredient(IngredientID))""")

#! Request Table
cursor.execute("""CREATE TABLE Request (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INT REFERENCES Customer(CustomerID),
    TableID INT REFERENCES DiningTable(TableID),
    Delivery BOOLEAN,
    OrderTime DATETIME,
    Server INT REFERENCES Employee(EmployeeID))""")

#! Employee Table
cursor.execute("""CREATE TABLE Employee (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName VARCHAR NOT NULL,
    LastName VARCHAR NOT NULL,
    Position VARCHAR NOT NULL,
    HourlyRate FLOAT)""")

#! Customer Table
cursor.execute("""CREATE TABLE Customer (
    CustomerID INTEGER PRIMARY KEY,
    FirstName VARCHAR NOT NULL,
    LastName VARCHAR NOT NULL,
    Phone VARCHAR NOT NULL,
    Address VARCHAR NOT NULL)""")

#! Invoice Table
cursor.execute("""CREATE TABLE Invoice (
    InvoiceID INTEGER PRIMARY KEY,
    CustomerID INT REFERENCES Customer(CustomerID),
    Total FLOAT NOT NULL,
    InvoiceDate DATETIME)""")

#! DiningTable Table 
cursor.execute("""CREATE TABLE DiningTable (
    TableID INTEGER PRIMARY KEY,
    Number INT NOT NULL,
    Seating INT NOT NULL)""")

#! Booking Table
cursor.execute("""CREATE TABLE Booking (
    BookingID INTEGER PRIMARY KEY,
    CustomerID INT REFERENCES Customer(CustomerID),
    People INT,
    Date DATETIME,
    TableID REFERENCES DiningTable(TableID))""")

#! MenuIngredient Table
cursor.execute("""CREATE TABLE MenuIngredient (
    MenuID INT REFERENCES Menu(MenuID),
    IngredientID REFERENCES Ingredient(IngredientID),
    PRIMARY KEY (MenuID, IngredientID))""")

#! MenuItem
cursor.execute("""CREATE TABLE MenuItem (
    MenuID INT REFERENCES Menu(MenuID),
    ItemID INT REFERENCES Item(ItemID),
    PRIMARY KEY (MenuID, ItemID))""")

#! ItemAdjustment
cursor.execute("""CREATE TABLE ItemAdjustment (
    ItemID INT REFERENCES Item(ItemID),
    AdjustmentID INT REFERENCES Adjustment(AdjustmentID),
    PRIMARY KEY (ItemID, AdjustmentID))""")

db.commit()
db.close()