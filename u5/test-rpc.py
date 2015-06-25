# -*- coding: utf-8 -*-
# leif oppermann, 30.05.2012, 14.06.2013, 07.06.2014, 11.06.2015
# xmlrpc helfer

# todo:
# - in der Zeile "appengine = .." ihr Kürzel eintragen
# - in der Zeile "server = .." den gewünschten Server setzen

# wenn alles auf der app engine läuft, sieht die fertige URL ungefähr so aus:
# - http://lopper2g.appspot.com/rpctest/rpc/call/xmlrpc (auch hier wieder ihr kürzel anpassen!)

from xmlrpclib import ServerProxy

# rpctest war der vorgeschlagene name für die web2py application, ansonsten einfach aendern
# kann auch mit der appengine verwendet werden. dazu url anpassen (-> http:APPLICATIONAME.appspot.com/rpctest/rpc/call/xmlrpc).

# drei mögliche server konfigurieren
localweb2py = ServerProxy("http://127.0.0.1:8000/rpctest/rpc/call/xmlrpc")
localappengine = ServerProxy("http://127.0.0.1:9080/rpctest/rpc/call/xmlrpc")
appengine = ServerProxy("http://jwiens2s-987.appspot.com/rpctest/rpc/call/xmlrpc") # ihr kürzel in die url eintragen!

# server entweder localweb2py, localappengine oder appengine
server = appengine

s=server._ServerProxy__host+server._ServerProxy__handler
print "Verbinde mit %s" % s
print server.hello()

name = server.userid()
print "hallo %s" %name

print server.echo("teste add mit zahlen (19+23=)")
print server.add(19, 23)
print server.echo("teste add mit strings")
print server.add("add funktioniert auch ", "mit strings")
print server.echo("teste json packer")
print server.json(1,2)
