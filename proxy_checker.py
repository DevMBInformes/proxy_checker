#!/bin/python

import requests
import threading
import queue
import re


# Crear una cola para almacenar las direcciones IP con puertos
q = queue.Queue()

# Realiza una solicitud HTTP para obtener el contenido de la página web que almacena datos de proxies gratuitos
result = requests.get("https://free-proxy-list.net/")


if result.status_code == 200:
    # Extraer las direcciones IP con puertos utilizando expresiones regulares
    ip_ports = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}\b", result.text)
    ip_ports = list(set(ip_ports))  # Eliminar duplicados si es necesario
    print(f'Cantidad de direcciones proxies encontradas: {len(ip_ports)}...')
    for p in ip_ports:
        q.put(p) #empujamos a la pila el valor

# Crear una lista para almacenar las direcciones IP con puertos válidas
list_proxys_ok = []

# Crear un objeto de bloqueo para asegurar el acceso seguro a list_proxys_ok desde múltiples hilos
lock = threading.Lock()

# Función para verificar las direcciones IP con puertos
def check_proxys():
    global q, list_proxys_ok
    while not q.empty():
        url_proob = "https://free-proxy-list.net"
        item = q.get()
        if item != '':
            try:
                result = requests.get(url_proob, timeout=20, proxies={'https': item, 'http': item})
            except:
                continue
            if result.status_code == 200:
                with lock:
                    list_proxys_ok.append(item)
                    print(f'[+] {item} Servicio correcto!')

threads = []
# Crear hilos para verificar las direcciones IP con puertos
for _ in range(q.qsize()):
    thread = threading.Thread(target=check_proxys)
    thread.start()
    threads.append(thread)

# Esperar a que todos los hilos terminen su ejecución
for thread in threads:
    thread.join()

final_list=""
for item in list_proxys_ok:
    final_list += item + "\n"

final_list = final_list[:-1]
file = open("archivo","w")
file.write(final_list)
file.close()

print(final_list)
