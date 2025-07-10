#!/usr/bin/env python3
import mysql.connector
import os
import csv
import uuid

host="localhost"
user="root"
passwd="  "
database="ALX_prodev"

def connect_db():
    mydb = mysql.connector.connect(
        host,
        user,
        passwd,
        database
    )
    connection = mydb.cursor()

@connect_db
def create_database(connection):
    connection.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")

@connect_db
def connect_to_prodev():
    connection.execute("USE ALX_prodev")

@connect_to_prodev
def create_table(connection):
    create_table = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) NOT NULL PRIMARY KEY,
        name VARCHAR(36), NOT NULL,
        email VARCHAR(36), NOT NULL,
        age DECIMAL, NOT NULL
        )"""
        
    mycursor.execute(create_table)

@connect_db
def insert_data(connection, data):
    insert_query = """
    INSERT INTO user_data (user_id, name, email, age) 
    VALUES (%s, %s, %s, %s)
    """
    
    # Open and read the CSV file
    with open(data, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            user_id = str(uuid.uuid4())
            
            record = (
                user_id,
                row['name'],
                row['email'],
                int(row['age']) # Ensure age is an integer
            )
            cursor.execute(insert_query, record)
            rows_imported += 1
    connection.commit()
