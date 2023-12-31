# -*- coding: utf-8 -*-
try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database


from lib.utils.globalvars import *
from lib.proxy.kodi import kodi_proxy
from lib.proxy.python import proxy as pyproxy


profileDir = pyproxy.decode(translatePath(plugin_addon.getAddonInfo('profile')))

# create profile dirs
if not os.path.exists(profileDir):
    os.makedirs(profileDir)

db_file = os.path.join(profileDir, 'search.db')

# connect to db
init_connection = database.connect(db_file)
init_cursor = init_connection.cursor()

# create table
try:
    init_cursor.execute('CREATE TABLE IF NOT EXISTS search (search_term);')
except:
    pass

# close connection
init_connection.close()


def get_search_history():
    """
    Search for Search History inside db
    :return: list of used search terms
    """
    items = []
    db_connection = None
    try:
        db_connection = database.connect(db_file)
        db_cursor = db_connection.cursor()
        db_cursor.execute('SELECT search_term FROM search ORDER BY ROWID DESC')
        faves = db_cursor.fetchall()
        for a_row in faves:
            if len(a_row) > 0:
                items.append(a_row)
    except:
        pass
    finally:
        if db_connection is not None:
            db_connection.close()
    return items


def add_search_history(query):
    """
    Add 'keyword' to Search History
    :param query: term to add to db
    :return:
    """
    db_connection = database.connect(db_file)
    db_cursor = db_connection.cursor()
    db_cursor.execute('INSERT INTO search (search_term) VALUES (?)', (query,))
    db_connection.commit()
    db_connection.close()


def remove_search_history(query=None):
    """
    Remove single term from Search History
    :param query:
    :return:
    """
    db_connection = database.connect(db_file)
    db_cursor = db_connection.cursor()

    if query is not None:
        db_cursor.execute('DELETE FROM search WHERE search_term=?', (query,))
    else:
        db_cursor.execute('DELETE FROM search')

    db_connection.commit()
    db_connection.close()


def check_in_database(term):
    """
    Check if 'term' is inside database
    :param term: string that you check for
    :return: True if exist in database, False if not
    """
    db_connection = database.connect(db_file)
    db_cursor = db_connection.cursor()
    db_cursor.execute('SELECT Count(search_term) FROM search WHERE search_term=?', (term,))
    data = db_cursor.fetchone()
    if hasattr(data, '__getitem__'):
        return data[0]

    return data > 0


def clear_search_history():
    do_clean = kodi_proxy.Dialog.yes_no('Confirm Delete', 'Are you sure you want to delete ALL search terms?')
    if do_clean:
        remove_search_history()
        kodi_proxy.Dialog.refresh()
