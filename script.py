from faker import Faker
import random
from db import connection
from datetime import datetime


faker = Faker()



genres = ["Mystery","Horor","Adventure"]
adjectives = ["Dark","Forbiden","Eternal","Mysterious"]
nouns = ["Secrets","Kingdom","Love","Shadow"]

def generate_random_dob():
    return faker.date_between(start_date=datetime(1950, 1, 1), end_date=datetime(2000, 1, 1))

def generate_random_genre():
    return random.choice(genres)

def generate_random_name():
    return faker.name()

def generate_book_title (book_genre, book_name):

    return f"{random.choice(adjectives)} {random.choice(nouns)}: A {book_genre} book by {book_name} "

def insert_user(con,random_name,dob):
    cursor = con.cursor()
    users_query = "INSERT INTO users (name,dob) VALUES (%s, %s)"
    cursor.execute(users_query, (random_name,dob))
    con.commit()
    cursor.close()



def insert_book(con,book_name, book_genre,book_author):
    cursor = con.cursor()
    query = "INSERT INTO books (name,category,author) VALUES (%s, %s, %s)"
    cursor.execute(query, (book_name, book_genre,book_author))
    con.commit()
    cursor.close()


dob = generate_random_dob()
genre = generate_random_genre()
name = generate_random_name()
book_title = generate_book_title(genre,name)
insert_book(connection,book_title,genre,name)
insert_user(connection,name,dob)


print(dob,genre,name,book_title)


#generate author  vraca faker name funkcija
#generate book title uzima autora i vraca ime knjige
#generisi ime autora
#generisi ime knjige
#insertuj knjigu
#insertuj autora
#generate random dob
#generate random genre






