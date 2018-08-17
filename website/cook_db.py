import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError


def send_data(title, url, mommy, category):
    r.connect( "localhost", 28015).repl()

    #--- Send Data ---#
        #-NOTE: Each connection sets a default database to use during its lifetime 
        # (if you don’t specify one in connect, the default database is set to test). 
        # This way we can omit the db('test') command in our query. 
        #-NOTE: The insert command accepts a single document or an array of documents 
        # if you want to batch inserts. We use an array in this query instead of running 
        # three separate insert commands for each document.
    if mommy == 'yes':
        r.db("cookpad_scrape").table("mom").insert(
            {'Title': title,
                "Recipe": url,
                "Author": "Chef Mom",
                "Category": category},
            conflict="error"
            ).run()
        print('SENT to rethinkdb: ' + title)
        #read_data()
    if mommy == 'no':
        r.db("cookpad_scrape").table("not_mom").insert([
            {'Title': title,
                "Recipe": url,
                "Author": "Chef Unknown",
                "Category": category},
            conflict="error"
            ]).run()
        print('SENT to rethinkdb: ' + title)
        #read_data()

def read_data():
    r.connect( "localhost", 28015).repl()

    #--- Read Data ---#
        #-NOTE: Since the table might contain a large number of documents, the database returns a cursor 
        # object. As you iterate through the cursor, the server will send documents to the client in 
        # batches as they are requested. The cursor is an iterable Python object so you can go through 
        # all of the results with a simple for loop.
        #--- Terms ---#
        # r.row = currently visited document
        # "author" = value of the field "author" in the visited document
    # cursor = r.table("recipes").filter(r.row["author"] == "Mom").run()
    # for document in cursor:
    #     print(document)
    cursor = r.db("cookpad_scrape").table("mom").run()
    for document in cursor:
        print(document)
    cursor2 = r.db("cookpad_scrape").table("not_mom").run()
    for document in cursor2:
        print(document)

def update_docs():
    r.connect( "localhost", 28015).repl()

    r.table("recipes").update({"category":"food"}).run()

def delete_docs():
    r.connect( "localhost", 28015).repl()

    r.table("recipes").filter( r.row["author"].count() > 2 ).delete().run()
