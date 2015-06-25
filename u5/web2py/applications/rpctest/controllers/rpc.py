# -*- coding: utf-8 -*-
# Leif Oppermann, 30.05.2012, 13.06.2013, 07.06.2014, 11.06.2015
# hbrs-web uebung 5 (XML-RPC calls w. App Engine)

# Update 2015: neue App-Engine Version 1.9.22 und web2py 2.11.2
# Windows 7 App-Engine nicht nach Programme, sondern z.B. nach c:\dev\appengine installieren



'''
benötigte Software:
a) Python 2.7 (keine 3er Version!), http://www.python.org/
 - zusätzlich empfohlen bei Interesse an Python, aber für die Übung nicht benötigt: wxPython mit wxPython Demo (insb. wegen Pycrust), http://www.wxpython.org/
c) App Engine SDK, https://developers.google.com/appengine/downloads
b) web2py SOURCE CODE (in der grünen Box, nicht den Binary Installer), http://www.web2py.com/examples/default/download

Arbeitsschritte:
1) Software installieren
 - Python installieren (unter Windows nach c:\python27)
 - App Engine SDK für Python installieren
 - web2py_src.zip entpacken

2) lokalen web2py Server starten
 - die Datei web2py.py im Ordner web2py ausführen
 -- entweder einfach das Icon anklicken
 -- oder aus der Shell starten (im web2py Ordner: "web2py.py" ausführen)
 -- ggf. (unter Windows) eine "python.bat" irgendwo im Pfad erzeugen (inhalt: "c:\python27\python.exe %1 %2 %3 %4 %5 %6 %7 %8 %9")
 --- dann kann man im web2py Ordner auch "python web2py.py" ausführen, falls alles andere nicht hilft
 - geben sie ein einfaches Passwort ein, es wird nur lokal benötigt um das Admin Interface freizuschalten
 - starten Sie den Server. Es sollte sich kurz darauf automatisch ein Browser-Fenster öffnen.
 -- falls nicht einfach auf http://127.0.0.1:8000 gehen
 - Wenn Sie die Welcome App sehen, ist alles gut.

3) rpctest Anwendung erstellen und zum Laufen kriegen
 - öffnen Sie das Administrative Interface (Button auf der rechten Seite der Welcome App)
 - links sehen Sie eine Übersicht aller in dieser web2py Instanz installierten Anwendungen
 - eine "Neue einfache Anwendung" anlegen (Name der Applikation: rpctest) und zur Admin-Seite zurück kehren
 - Die Anwendung "rpctest" sollte links in der Liste auftauchen (ggf. Seite neu laden)
 - überprüfen Sie durch einen Klick auf rpctest, dass die Anwendung läuft (die Seite sieht aus wie die Welcome Anwendung)
 - kehren Sie dann zurück und klicken auf "Verwalten" (in manchen web2py Versionen auch "Bearbeiten")

 - die Datei rpc.py in das controllers Verzeichnis von rpctest kopieren

 - unter "Controller" sollte im Web UI rpc.py aufgeführt sein und call, hello und userid zur Verfügung stellen
 -- sonst ggf. neu lade
 - klicken Sie auf "hello", daraufhin sollte "webservice" im Browser ausgegeben werden

4) rpctest Anwendung anpassen Teil 1 - Funktion ohne Parameter
 - klicken Sie auf "userid", daraufhin ersteint noch mein Kürzel
 - ersetzen Sie dies durch Ihr Kürzel, indem sie in rpc.py die Funktion userid() anpassen
 -- falls Sie einen externen Editor verwenden, beachten Sie dabei, dass Sie die richtige Datei editieren (also web2py/applications/rpctest/controllers/rpc.py)
 -- ansonsten können Sie mit dem web2py Admin Interface den Controller Code auch komfortabel direkt im Browser bearbeiten!
 - testen sie die geänderte Funktion durch ausführen, entweder anklicken, oder per URL http://127.0.0.1:8000/rpctest/rpc/userid

/* Exkurs URLs in web2py:
 Einfache Funktionen _OHNE_ Parameter werden in web2py im Format /APPLICATION/CONTROLLER/FUNCTION auf die URL gemappt.

 Beispiel1:	die Funktion "userid()" in der Datei "rpc.py" in der Application "rpctest" wird auf einer lokalen Maschine
			als http://127.0.0.1:8000/rpctest/rpc/userid bereitgestellt
			dasselbe gilt analog für die Funktion hello() und alle anderen Funktionen ohne Parameter
			(Detaillierte Informationen zum Dispatching finden Sie in den Vorlesungs-Folien und auf http://web2py.com/books/default/chapter/29/04#Dispatching)

 Komplexere Funktionen _MIT_ Parametern sowie Webservices unterliegen in web2py einer anderen, etwas längeren Syntax. Das Format für das URL Mapping lautet dabei /APPLICATION/CONTROLLER/call/run/FUNCTION/PARAMETER1/PARAMETER2/etc...
 Hierzu muss FUNCTION für den "run" Service dekoriert sein (@service.run in der Zeile über der Funktionsdeklaration) und wird dann über die Funktion "call" aufgerufen. Neben "run" werden noch weitere Services, wie z.B. "xmlrpc" unterstützt.

 Beispiel2:	Da diese Syntax auch auf einfache Funktionen angewendet werden kann, zunächst nochmal das Beispiel für die userid() Funktion,
			die in der langen Syntax als http://127.0.0.1:8000/rpctest/rpc/call/run/userid adressiert werden kann

 Beispiel3:	Die Echo Funktion benötigt einen Parameter, den Sie ausgeben soll. Sie kann über http://127.0.0.1:8000/rpctest/rpc/call/run/echo/hallo 			 aufgerufen werden und sollte dann "--- hallo ---" ausgeben. (Dies tut sie aber noch nicht, deshalb Schritt 5.)

 (Detailierte Informationen zur Service Syntax und den RPC Funktionen von web2py unter http://www.web2py.com/book/default/chapter/10#Remote-procedure-calls)
 */

5) rpctest Anwendung anpassen Teil 2 - Funktion mit Parameter
  Die Funktionen echo(), add() und json() beinhalten noch minimale Fehler, die Sie fixen müssen. Die erwarteten Rückgabe-Werte für jeweils ein Beispiel sind in den sogenannten Python doctests, d.h. den Kommentaren mit >>> gleich nach der Funktionsdeklaration aufgeführt. web2py unterstützt das Testen mit doctests. Klicken Sie dazu im Admin-Interface links neben der zu testenden Code-Datei "rpc.py" auf das Dokumenten-Symbol mit dem gelb-schwarzen Kreis. Daraufhin sollten die Funktionen add(), echo() und json() mit einem roten Kreis markiert fehlschlagen.

  - machen Sie, dass die Tests grün werden!
  -- testen Sie immer wieder mit dem beschriebenen Mechanismus in web2py
  - testen Sie dann mit dem beigefügten "test-rpc.py" Skript aus einer Shell auf der lokalen Maschine (Sie werden das Skript später noch brauchen)
  -- es ercheint vermutlich die Fehlermeldung "[..]method "json" is not supported"
  (wenn Sie das Skript ausgeführt haben, bevor die Tests grün waren, sollten Sie einen Fehler "[..]unsupported operand type(s) for -: 'str' and 'str'" gemeldet bekommen, weil die add-Funktion noch nicht wie erwartet funktioniert und man Strings nicht so leicht subtrahieren kann.)
  -- d.h. die Funktion json funktioniert zwar in den internen doctests, wird jedoch nicht per xmlrpc als webservice bereitgestellt.
  (Im Broser würde der Aufruf von http://127.0.0.1:8000/rpctest/rpc/call/run/json/1/2 einen "Object does not exist" Fehler melden.)
  - beheben Sie diesen Fehler, indem sie die Funktion entsprechend für die Services run und xmlrpc dekorieren
  - testen Sie abschließend noch einmal mit "test-rpc.py" und im Browser

6) web2py App in der Google App Engine installieren (deployen)
 - erstellen Sie einen Account in der App Engine (http://appspot.com)
 -- sie können ihren Benutzernamen dort frei wählen
 -- aber der Application Name soll bitte ihr Hochschul-Kürzel beinhalten (z.b. lopper2g oder hbrs-lopper2g)

 - teilen Sie web2py den App Engine "Application Name" mit, damit das Deployment funktionieren kann
 -- kopieren Sie web2py/examples/app.example.yaml nach web2py/app.yaml und passen die Datei entsprechend an
 -- der Application Name muss in /web2py/app.yaml vermerkt sein! (heisst dort application und besitzt den Default-Wert "web2py")
 -- das Hochschul-Kürzel aus der userid() funktion muss zum Application Name und zu ihrer Hochschul Email Adresse passen

 - kopieren sie die Datei web2py/handlers/gaehandler.py nach web2py/gaehandler.py

 - starten Sie den Google App Engine Launcher (Windows)
 - Konfigurieren Sie den Launcher, damit er auf Ihre web2py Installation zeigt
 -- File->Add Existing Application->Application Path (muss auf den web2py Ordner zeigen, z.B. C:\dev\web2py)
 (Falls die app.yaml fehlt, wird der Launcher dies bemängeln. In diesem Fall das Projekt mit File->Remove Project entfernen, Fehler beheben und erneut versuchen.)
 - starten sie die Anwendung im Launcher mit Klick auf den "Run" Button
 - mit Klick auf "Browse" öffnet sich ein Browser und zeigt die lokal laufende Web-App an
 - testen Sie http://localhost:8080/rpctest/rpc/call/run/json/1/2 (evtl. Portnummer anpassen)
 - testen Sie mit "test-rpc.py"
 -- beachten Sie die beiden im Kommentar am Anfang vermerkten todos und stellen Sie den zu testenden Server auf localappengine um ("server = localappengine")
 -- starten Sie das modifizierte Skript und sehen Sie, wie Ihre Funktionen über xmlrpc aufgerufen werden.

 - wenn alles läuft deployen Sie nun zur Google App Engine
 -- im App Engine Launcher auf "Deploy" drücken
 -- mit Google Email und Passwort anmelden
 -- es öffnet sich ein Konsolen-Fenster in dem Sie den Deployment-Fortschritt sehen können (dauert einige Sekunden)

 - Ihre App in der App Engine erreichen Sie nun wie folgt
 - a) im Launcher auf "Dashboard" klicken. Ein Browser öffnet sich. In der Titelzeile rechts oben auf "<< My Applications" klicken (führt zu b)
 - b) im Applications Overview in https://appengine.google.com/ rechts in der Spalte Status auf Running klicken
 - c) oder einfach direkt die URL als http://APPLICATIONNAME.appspot.com/rpctest im Browser eingeben (APPLICATIONNAME z.B. lopper2g)

7) Abgabe
 - passen Sie "test-rpc.py" an die App Engine an
 -- Zeile "appengine = .." mit Ihrem Application Name / Kürzel versehen (falls nicht schon geschehen)
 -- Zeile "server = appengine"
 - Test von der Kommandozeile durchlaufen lassen
 (Jetzt ist das Skript zum Testen besonders praktisch, weil auf der App Engine kein web2py Admin Interface zur Verfügung steht!)

 - wenn alles in der App Engine läuft, bitte den automatischen test auf http://loppermann.appspot.com/rpcvalidator/ ausführen
 -- anmelden mit ihrer Hochschul Email adresse
 -- URL zu ihrem webservice eingeben (startet mit http:// und endet auf /call/xmlrpc, steht in der appengine-Zeile in test-rpc.py)
 -- die Funktionen werden daraufhin getestet
 - bei Erfolg erhalten Sie eine Email vom System und die Aufgabe ist abgeschlossen. Herzlichen Glückwunsch!

 - Abgabe bis 12.06.2014 (die automatische Email gilt als Abgabe)
  (Sie können mit dieser Installation problemlos weitere Apps in web2py hinzufügen und auf die App Engine deployen.)
'''

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@service.xmlrpc
@service.run
def hello():
    return "webservice"

@service.xmlrpc
@service.run
def userid():
    return "jwiens2s"

@service.xmlrpc
@service.run
def echo(something):
    '''
    >>> echo("appengine webapp mit web2py")
    '--- appengine webapp mit web2py ---'
    '''
    return "--- %s ---" % something

@service.xmlrpc
@service.run
def add(a,b):
    '''
    >>> add(1,2)
    3
    '''
    return a+b

@service.xmlrpc
@service.run
def json(a,b):
    '''
    >>> json(1,2)
    {'a': 1, 'b': 2}
    '''
    json = dict()
    json["a"]=a
    json["b"]=b
    return json
