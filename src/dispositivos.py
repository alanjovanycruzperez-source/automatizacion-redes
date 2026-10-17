## P3:

def mostrar_dispositivo(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Modelo:", dispositivo["modelo"])
    print("Protocolo:", dispositivo["protocolo"])


dispositivos = [

    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "estado": "Activo",
        "fabricante": "Cisco",
        "modelo": "Catalyst 9300",
        "protocolo": "OSPF"
    },

    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "estado": "Activo",
        "fabricante": "Cisco",
        "modelo": "Catalyst 9300",
        "protocolo": "OSPF"
    },

    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Activo",
        "fabricante": "Cisco",
        "modelo": "Catalyst 9300",
        "protocolo": "OSPF"
    }

]

for dispositivo in dispositivos:
    mostrar_dispositivo(dispositivo)

    if dispositivo["estado"] == "Activo":
        print("El dispositivo está disponible.")
    else:
        print("El dispositivo requiere atención.")

    print()


def buscar_dispositivo(dispositivos):
    nombre_buscar = input("Ingrese el nombre del dispositivo: ").strip()

    for dispositivo in dispositivos:
        if dispositivo["nombre"].lower() == nombre_buscar.lower():
            print("\nDispositivo encontrado:")
            mostrar_dispositivo(dispositivo)
            return

    print("Dispositivo no encontrado.")


buscar_dispositivo(dispositivos)
