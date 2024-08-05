from bottle import route, run, template, static_file
import sqlite3
db = sqlite3.connect("pizza.db")
cursor = db.cursor()


@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route("/")
def index():
    #Get all menu items
    cursor.execute("SELECT name, basePrice FROM Menu")
    menuItems = cursor.fetchall()
    #split records into groups of 3
    groups = [menuItems[i:min(i+3, len(menuItems))] for i in range(0, len(menuItems), 3)]
    return template("index", menu=groups)


run(host="localhost", port=8080, debug=True, reloader=True)

db.commit()
db.close()