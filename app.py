import sqlite3

conn = sqlite3.connect('urls_database.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE urls
             (name TEXT, url TEXT, content TEXT)''')

# Insert initial data from the Excel file
initial_data  = [
    ("ALUBAF INTERNATIONAL BANK-TUNIS", "http://www.alubaf.com.tn/?q=en/search/node/appel%20d%27offre"),
    ("ATB", "https://www.atb.tn/ar/offres-emploi"),
    ("BNA", "http://www.bna.tn/fr/appels-d-offres-resultats.832.html"),
    ("Attijari Bank", "https://www.attijariwafabank.com/sites/default/files/2023-07/22-00608-Communique%CC%81-Cessions%20d%27actifs%28A4%29-VF_0.pdf"),
    ("BT", "https://www.bt.com.tn/News/26054"),
    ("AMEN BANK", "https://www.stbfinance.com.tn/amen-bank-appel-candidature"),
    ("BIAT", "https://www.biat.com.tn/search/content?keys=appel+d%27offre"),
    ("STB", "https://www.stb.com.tn/en/actualites/avis-dappel-doffres-ref-ao-042023-acquisition-et-mise-en-uvre-dune-solution-de-gestion-du-port/"),
    ("UBCI", "https://www.stb.com.tn/en/actualites/avis-dappel-doffres-ref-ao-042023-acquisition-et-mise-en-uvre-dune-solution-de-gestion-du-port/"),
    ("UIB", "https://www.stbfinance.com.tn/uib-appel-candidature"),
    ("BH BANK", "https://www.bhbank.tn/publications"),
    ("CITIBANK", "https://www.citi.com/"),
    ("BTK", "https://www.btknet.com/site/fr/news_details.php?id_article=218&id_news=7"),
    ("TSB", "https://www.tsb.com.tn/fr/recherche?recherche=Appel+d%27offre"),
    ("QNB", "https://www.qnb.com.tn/fr/#"),
    ("BanqueZitouna", "https://www.banquezitouna.com/fr/actualites-et-evenements/appel-candidatures-administrateurs-independants"),
    ("BTL", "https://btl.tn/actualites/"),
    ("BTS", "https://www.bts.com.tn/?s=appel+d%27offre"),
    ("BANK ABC", "la connexion au site web est devenue privé"),
    ("BFMPE", "https://bfpme.com.tn/?page_id=6359"),
    ("ALBARAKA BANK", "https://albaraka.com.tn/fr/actualites?title=Appel+d%27offre&field_theme_target_id=All"),
    ("WIFAK BANK", "https://managers.tn/2022/07/07/wifak-bank-lance-un-appel-a-candidature-pour-un-administrateur-independant/"),
    ("North Africa International Bank", "http://www.naibbank.com/"),
    ("S E R E P T", "https://www.serept.com.tn/Fr/recherche_57_36?q=Appel+d%27offre"),
    ("Milleis Banque", "https://www.milleis.fr/actualites-de-notre-maison?page=1"),
    ("Amen bank", "https://www.stbfinance.com.tn/amen-bank-appel-candidature"),
    ("STB BANK", "https://www.stb.com.tn/en/actualites/avis-dappel-doffres-ref-ao-042023-acquisition-et-mise-en-uvre-dune-solution-de-gestion-du-port/"),
    ("BTK", "https://www.btknet.com/site/fr/news_details.php?id_article=218&id_news=7"),
    ("BIAT", "https://www.biat.com.tn/search/content?keys=appel+d%27offre"),
    ("banque de France", "https://achats-banquedefrance.safetender.com/#/home"),
    ("group bcp", "https://www.groupebcp.com/fr/appels-doffres")
]

c.executemany('INSERT INTO urls (name, url) VALUES (?, ?)', initial_data)
conn.commit()
conn.close()
