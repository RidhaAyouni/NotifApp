# from bs4 import BeautifulSoup
# import requests
# import sqlite3

# def fetch_content(url):
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         return str(soup)
#     except Exception as e:
#         print(f"Error fetching content from {url}: {e}")
#         return None
# def check_for_updates():
#     conn = sqlite3.connect('urls_database.db')
#     c = conn.cursor()

#     updated_urls = []

#     for row in c.execute('SELECT name, url, content FROM urls'):
#         name, url, current_content = row
#         new_content = fetch_content(url)
#         if new_content and current_content != new_content:
#             c.execute('UPDATE urls SET content = ? WHERE url = ?', (new_content, url))
#             updated_urls.append(name)
    
#     conn.commit()
#     conn.close()
    
#     return updated_urls
from bs4 import BeautifulSoup
import requests
import sqlite3

def fetch_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return str(soup)
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return None

def check_for_updates():
    conn = sqlite3.connect('urls_database.db')
    c = conn.cursor()

    updates_info = []

    for row in c.execute('SELECT name, url, content FROM urls'):
        name, url, current_content = row
        new_content = fetch_content(url)
        if new_content and current_content != new_content:
            # Update the database with new content
            c.execute('UPDATE urls SET content = ? WHERE url = ?', (new_content, url))
            # Append detailed information for the update notification
            updates_info.append({'name': name, 'url': url})
    
    conn.commit()
    conn.close()
    
    return updates_info
