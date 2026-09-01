Fruit Sweets 🍓

Am creat pt tema un magazin online de akai cu fructe sau diverse dulciuri, pornind de la laboartorul 4. Am o pagina principala cu imagini, descrieri si preturi pt produse, butoane de adaugare si stergere produse din cos, cosul de
cumparaturi, pagina de comandat cu formular si salvare de comenzi, pagina de confirmare a comenzii si pagina de contact.

##Continutul temei:

#app:
main_app.py — initializeaza instanta Flask si inregistreaza rutele
products.py — lista de produse 
shop.py —  rutele aplicatiei: pagina principala, cos, checkout, contact

#public : imaginile produselor, fisierele Bootstrap si CSS-ul
style.css — stilurile CSS 
images — imaginile produselor 
bootstrap — fisierele Bootstrap luate din labul 4

#submitted-orders: folderul in care se salveaza automat comenzile , fiecare ca fisier json

#templates:  template-urile HTML
_layout.html —   structura HTML de baza pe care o folosesc toate paginile
cart.html — pagina cu cosul
checkout.html — formularul pt comandare
contact.html — pagina de contact
index.html — pagina cu produsele
order_success.html — pagina de confirmare dupa plasarea comenzii

server.py — porneste serverul Flask pe portul 5000
Dockerfile — porneste serverul Flask in container Alpine, accesibil pe portul 5000 si e bazat pe cel din labul 4
requirements.txt — lista de dependente Python bazat pe cel din labul 4

Ca bonusuri, am personalizat siteul cu culori rozalii, am pagina de confirmare pt comenzi care are detalii pt comanda efectuata precum produsele, pretul fiecareia, pretul total, butoane pt adaugarea sau scaderea cantitatii unui produs, salvarea comenzilor in format json.
Pentru rulare, merge si cu python3 server.py si cu docker build -t iap1-tema ./  docker run -p 5000:5000 -it iap1-tema
