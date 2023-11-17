import os
from xml.dom import minidom

doc = minidom.Document()

sitemapindex = doc.createElement("sitemapindex")
sitemapindex.setAttribute("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
doc.appendChild(sitemapindex)


katalog_skryptu = os.path.dirname(os.path.abspath(__file__))
katalog_sitemap = os.path.join(katalog_skryptu, "active_sitemaps")
katalog_wyjsciowy = os.path.join(katalog_skryptu, "output")


if not os.path.exists(katalog_wyjsciowy):
    os.makedirs(katalog_wyjsciowy)

nazwa_pliku_indeksu = os.path.join(katalog_wyjsciowy, "global_search_index.xml")

for plik in os.listdir(katalog_sitemap):
    if plik.endswith(".xml"):
        sitemap_element = doc.createElement("sitemap")
        loc_element = doc.createElement("loc")
        loc_element.appendChild(
            doc.createTextNode(f"https://allegrolokalnie.pl/sitemap-d10ea409-8640-41bb-ab18-a6383cb8c229/globalSearchs/{plik}")
        )
        sitemap_element.appendChild(loc_element)
        sitemapindex.appendChild(sitemap_element)

with open(nazwa_pliku_indeksu, "w", encoding="utf-8") as plik:
    doc.writexml(plik, indent="\t", addindent="\t", newl="\n", encoding="utf-8")

print(f"Plik indeksu '{nazwa_pliku_indeksu}' został utworzony.")
