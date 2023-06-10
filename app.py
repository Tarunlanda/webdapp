from flask import Flask
import requests
import psycopg2

app = Flask(__name__)

def establish_connection():
    conn = psycopg2.connect("")#add your connection string here
    cur = conn.cursor()
    return (conn,cur)

def close_connection(conn,cur):
    cur.close()
    conn.close()

@app.route('/')
def index_page():
    return "You are in the main page"

@app.route('/add_item')
def add_item():
    (conn,cur)=establish_connection()
    new_item = requests.json['item_name']
    new_price = requests.json['item_price']
    cur.execute("INSERT INTO items_list (name,price) VALUES (%s,%s)",(new_item,new_price))
    close_connection(conn,cur)


if __name__ == "__main__":
    app.run(debug=True)
    
