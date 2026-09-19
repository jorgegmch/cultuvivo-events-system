import modules.utils as u

#login
def login():
    usuario = input("   Login: ")
    if usuario == "0":
        return "salir"

    try:
        admins = u.leer_json("data/admins.json")
    except FileNotFoundError:
        admins = []
    if usuario in admins:
        return "admin"

    try:
        asistentes = u.leer_json("data/asistentes.json")
    except FileNotFoundError:
        asistentes = []
    if any(a["cedula"] == usuario for a in asistentes):
        return "asistente"

    try:
        artistas = u.leer_json("data/artistas.json")
    except FileNotFoundError:
        artistas = []
    if any(a["id_artista"] == usuario for a in artistas):
        return "artista"

    print("\nUsuario no existe!!❌   \n\nIntente nuevamente o presione '0' para salir.\n ")
    return None


# ADMINS CRUD
def registro_eventos():
    try:
        eventos = u.leer_json("data/eventos.json")
    except FileNotFoundError:
        eventos = []
    print(">>>>  ➕ Nuevo Evento <<<<<\n")

    id = input("ID Evento: ")
    while any(e["id"] == id for e in eventos):
        print("Ya existe un evento con ese ID.")
        id = input("ID Evento: ")

    nombre = input("Nombre: ")

    fecha = input("Fecha (AAAA-MM-DD): ")
    while not u.validador_fecha(fecha):
        print("Fecha inválida. Debe tener el formato AAAA-MM-DD.")
        fecha = input("Fecha (AAAA-MM-DD): ")

    hora = input("Hora (HH:MM): ")
    while not u.validador_hora(hora):
        print("Hora inválida. Debe tener el formato HH:MM.")
        hora = input("Hora (HH:MM): ")

    lugar = input("Lugar: ")

    capacidad = input("Aforo: ")
    while not u.validador_capacidadmaxima(capacidad):
        print("Aforo inválido. Debe ser un número entero mayor a 0.")
        capacidad = input("Aforo: ")

    estado = input("Estado del evento (activo/proximo): ").lower()
    while estado not in ["activo", "proximo"]:
        print("Estado inválido. Debe ser 'activo' o 'proximo'.")
        estado = input("Estado del evento (activo/proximo): ").lower()

    nuevo_evento = {
        "id": id,
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "lugar": lugar,
        "capacidad": capacidad,
        "estado": estado
    }
    eventos.append(nuevo_evento)
    u.escribir_json("data/eventos.json",eventos)

def registro_artistas():
    try:
        artistas = u.leer_json("data/artistas.json")
    except FileNotFoundError:
        artistas = []
    print(">>>>> 🎨 Nuevo Artista <<<<<\n")

    id_artista = input("> ID : ")
    while any(a["id_artista"] == id_artista for a in artistas):
        print("Ya existe un artista con ese ID.")
        id_artista = input("> ID : ")

    nombre=input("> Nombre: ")
    tipo_presentacion=input("> Tipo de presentación: ")
    tiempo_presentacion=input("> Tiempo de Presentación: ")

    nuevo_artista= {
        "id_artista" : id_artista,
        "nombre": nombre,
        "tipo_presentacion":tipo_presentacion,
        "tiempo": tiempo_presentacion
    }
    artistas.append(nuevo_artista)
    u.escribir_json("data/artistas.json",artistas)
    print(f"Artista {nombre} registrado correctamente!")


def asignar_artista_evento():
    # Mostrar eventos disponibles
    eventos = u.leer_json("data/eventos.json")
    if not eventos:
        print("No hay eventos disponibles.")
        return
    print(">>>> 📅 Eventos Disponibles <<<<<")
    for evento in eventos:
        print(f"ID: {evento['id']}, Nombre: {evento['nombre']}")
    evento_id = input("Ingrese el ID del evento: ")
    evento = next((e for e in eventos if e['id'] == evento_id), None)
    if evento is None:
        print("Evento no encontrado.")
        return

    # Mostrar artistas disponibles
    artistas = u.leer_json("data/artistas.json")
    if not artistas:
        print("No hay artistas disponibles.")
        return
    print(">>>> 🎨 Artistas Disponibles <<<<<")
    for artista in artistas:
        print(f"ID: {artista['id_artista']}, Nombre: {artista['nombre']}")
    artista_id = input("Ingrese el ID del artista: ")
    artista = next((a for a in artistas if a['id_artista'] == artista_id), None)
    if artista is None:
        print("Artista no encontrado.")
        return

    # Verificar si ya está asignado
    asignaciones = u.leer_json("data/asignaciones_artistas.json")
    if asignaciones is None:
        asignaciones = []
    if any(a['artista_id'] == artista_id and a['evento_id'] == evento_id for a in asignaciones):
        print("Este artista ya está asignado a este evento.")
        return

    # Asignar
    nueva_asignacion = {
        "artista_id": artista_id,
        "evento_id": evento_id
    }
    asignaciones.append(nueva_asignacion)
    u.escribir_json("data/asignaciones_artistas.json", asignaciones)
    print(f"Artista {artista['nombre']} asignado al evento {evento['nombre']} con éxito.")

def monitorear_aforo():
    eventos = u.leer_json("data/eventos.json")
    if not eventos:
        print("No hay eventos disponibles.")
        return

    # Filtrar solo eventos activos
    activos = [e for e in eventos if e.get("estado") == "activo"]
    if not activos:
        print("No hay eventos activos para monitorear.")
        return

    # Mostrar eventos activos con número de asistentes confirmados
    print(">>>> 📊 Monitoreo de Aforo <<<<<")
    for i, evento in enumerate(activos, 1):
        # Contar asistentes confirmados
        inscripciones = u.leer_json("data/inscripciones.json")
        if inscripciones is None:
            count = 0
        else:
            count = sum(1 for i in inscripciones if i['evento_id'] == evento['id'] and i['estado'] == 'confirmado')
        bloqueado = evento.get("bloqueado", False)
        status = "Bloqueado" if bloqueado else "Abierto"
        print(f"{i}. {evento['nombre']} - Asistentes Confirmados: {count}/{evento['capacidad']} - Estado: {status}")

    try:
        op_evento = int(input("Seleccione un evento (número): ")) - 1
        if op_evento < 0 or op_evento >= len(activos):
            print("Selección inválida.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    evento = activos[op_evento]
    print(f"\n>>>> 📋 Detalles del Evento: {evento['nombre']} <<<<<")
    print(f"ID: {evento['id']}")
    print(f"Fecha: {evento['fecha']}")
    print(f"Hora: {evento['hora']}")
    print(f"Lugar: {evento['lugar']}")
    print(f"Capacidad: {evento['capacidad']}")

    # Contar asistentes
    if inscripciones is None:
        count = 0
    else:
        count = sum(1 for i in inscripciones if i['evento_id'] == evento['id'] and i['estado'] == 'confirmado')
    print(f"Asistentes Confirmados: {count}")

    bloqueado = evento.get("bloqueado", False)
    if bloqueado:
        print("Estado: Bloqueado (inscripciones no permitidas)")
    else:
        print("Estado: Abierto")

    # Opción para bloquear/desbloquear
    if bloqueado:
        opcion = input("¿Desea desbloquear las inscripciones? (s/n): ").lower()
        if opcion == 's':
            evento["bloqueado"] = False
            u.escribir_json("data/eventos.json", eventos)
            print("Inscripciones desbloqueadas.")
        else:
            print("Sin cambios.")
    else:
        opcion = input("¿Desea bloquear las inscripciones? (s/n): ").lower()
        if opcion == 's':
            evento["bloqueado"] = True
            u.escribir_json("data/eventos.json", eventos)
            print("Inscripciones bloqueadas.")
        else:
            print("Sin cambios.")


# ADMINS REPORTES
def participacion_artistas():
    artistas = u.leer_json("data/artistas.json")
    asignaciones = u.leer_json("data/asignaciones_artistas.json")
    if artistas is None or asignaciones is None:
        print("No hay datos disponibles.")
        return
    participacion = {}
    for artista in artistas:
        id_artista = artista['id_artista']
        count = sum(1 for a in asignaciones if a['artista_id'] == id_artista)
        participacion[id_artista] = {'nombre': artista['nombre'], 'eventos': count}
    print(">>>> 🎤 Participación de Artistas <<<<<")
    for id_artista, data in participacion.items():
        print(f"ID: {id_artista}, Nombre: {data['nombre']}, Eventos: {data['eventos']}")
    print()

def ver_proximos_eventos():
    eventos = u.leer_json("data/eventos.json")
    if eventos is None:
        print("No hay eventos disponibles.")
        return
    proximos = [evento for evento in eventos if evento.get("estado") == "proximo"]
    if not proximos:
        print("No hay eventos próximos.")
        return
    print(">>>> 📅 Próximos Eventos <<<<<")
    for evento in proximos:
        print(f"ID: {evento['id']}, Nombre: {evento['nombre']}, Fecha: {evento['fecha']}, Hora: {evento['hora']}, Lugar: {evento['lugar']}")
    print()

def listado_asistentes():
    asistentes = u.leer_json("data/asistentes.json")
    if not asistentes:
        print("No hay asistentes registrados.")
        return
    print(">>>> 👥 Listado de Asistentes <<<<<")
    for asistente in asistentes:
        print(f"Nombre: {asistente['nombre']}, Cédula: {asistente['cedula']}, Correo: {asistente['correo']}, Estado: {asistente['estado']}, Tipo Boleta: {asistente['tipo_boleta']}")
    print()

def eventos_menos_asistentes():
    eventos = u.leer_json("data/eventos.json")
    inscripciones = u.leer_json("data/inscripciones.json")
    if eventos is None or inscripciones is None:
        print("No hay datos disponibles.")
        return
    conteo = {}
    for evento in eventos:
        id_evento = evento['id']
        count = sum(1 for i in inscripciones if i['evento_id'] == id_evento and i['estado'] == 'confirmado')
        conteo[id_evento] = {'nombre': evento['nombre'], 'asistentes': count}
    if not conteo:
        print("No hay eventos con asistentes confirmados.")
        return
    min_asistentes = min(conteo.values(), key=lambda x: x['asistentes'])['asistentes']
    eventos_menos = [data for data in conteo.values() if data['asistentes'] == min_asistentes]
    print(">>>> 📉 Eventos con Menos Asistentes Confirmados <<<<<")
    for evento in eventos_menos:
        print(f"Nombre: {evento['nombre']}, Asistentes Confirmados: {evento['asistentes']}")
    print()

# ARTISTAS CRUD
def agenda_presentaciones():
    artista_id = input("Ingrese su ID de artista: ")
    asignaciones = u.leer_json("data/asignaciones_artistas.json")
    if not asignaciones:
        print("No hay asignaciones de presentaciones.")
        return
    mis_asignaciones = [a for a in asignaciones if a['artista_id'] == artista_id]
    if len(mis_asignaciones) == 0:
        print("No tiene presentaciones asignadas.")
        return
    eventos = u.leer_json("data/eventos.json")
    if eventos is None:
        print("No hay eventos disponibles.")
        return
    print(">>>> 📅 Agenda de Presentaciones <<<<<\n")
    for asignacion in mis_asignaciones:
        evento = next((e for e in eventos if e['id'] == asignacion['evento_id']), None)
        if evento:
            print(f"Evento: {evento['nombre']} \nFecha: {evento['fecha']} \nHora: {evento['hora']} \nLugar: {evento['lugar']}\n")
    print()

def detalles_eventos():
    artista_id = input("Ingrese su ID de artista: ")
    asignaciones = u.leer_json("data/asignaciones_artistas.json")
    if not asignaciones:
        print("No hay asignaciones de presentaciones.")
        return
    mis_asignaciones = [a for a in asignaciones if a['artista_id'] == artista_id]
    if len(mis_asignaciones) == 0:
        print("No tiene presentaciones asignadas.")
        return
    eventos = u.leer_json("data/eventos.json")
    if eventos is None:
        print("No hay eventos disponibles.")
        return
    print(">>>> 📋 Detalles de Eventos Asignados <<<<<")
    for asignacion in mis_asignaciones:
        evento = next((e for e in eventos if e['id'] == asignacion['evento_id']), None)
        if evento:
            print(f"ID: {evento['id']}, Nombre: {evento['nombre']}, Fecha: {evento['fecha']}, Hora: {evento['hora']}, Lugar: {evento['lugar']}, Capacidad: {evento['capacidad']}")
    print()

# ASISTENTES CRUD
def nuevo_asistente():
    nombre = input("Nombre Completo: ")
    id = input("Cedula: ")
    correo = input("Correo: ")

    # Leer asistentes existentes o iniciar lista vacía
    try:
        total_asistentes = u.leer_json("data/asistentes.json")
    except FileNotFoundError:
        total_asistentes = []

    # Verificar si el asistente ya existe
    for asistente in total_asistentes:
        if asistente["cedula"] == id:
            print("Ese asistente ya existe")
            return

    # Agregar nuevo asistente
    total_asistentes.append({
        "nombre": nombre,
        "cedula": id,
        "correo": correo,
        "estado":"",
        "tipo_boleta": ""
    })

    u.escribir_json("data/asistentes.json", total_asistentes)
    print(f"{nombre} Registrado correctamete! ")

def ver_eventos_disponibles():
    eventos = u.leer_json("data/eventos.json")
    if not eventos:
        print("No hay eventos disponibles.")
        return
    # Filtrar eventos no bloqueados
    eventos_disponibles = [e for e in eventos if not e.get("bloqueado", False)]
    if len(eventos_disponibles) == 0:
        print("No hay eventos disponibles.")
        return
    print(">>>> 📅 Eventos Disponibles <<<<<")
    for evento in eventos_disponibles:
        print(f"N°:{evento['id']}\n Nombre: {evento['nombre']}\n Fecha: {evento['fecha']}\n Hora: {evento['hora']}\n Lugar: {evento['lugar']}\n")
    print()


def inscripcion_evento():
    ver_eventos_disponibles()
    evento_id = input("Ingrese el N° del evento al que desea inscribirse: ")
    asistente_id = input("Ingrese su ID de asistente: ")
    # Verificar si el evento existe
    eventos = u.leer_json("data/eventos.json")
    if eventos is None:
        print("No hay eventos disponibles.")
        return
    evento = next((e for e in eventos if e['id'] == evento_id), None)
    if evento is None:
        print("Evento no encontrado.")
        return
    # Verificar si el evento está bloqueado
    if evento.get("bloqueado", False):
        print("Las inscripciones para este evento están bloqueadas.")
        return
    # Verificar si ya está inscrito
    inscripciones = u.leer_json("data/inscripciones.json")
    if inscripciones is None:
        inscripciones = []
    if any(i['asistente_id'] == asistente_id and i['evento_id'] == evento_id for i in inscripciones):
        print("Ya está inscrito en este evento.")
        return
    # Registrar inscripción con estado "en espera"
    nueva_inscripcion = {
        "asistente_id": asistente_id,
        "evento_id": evento_id,
        "estado": "en espera"
    }
    inscripciones.append(nueva_inscripcion)
    u.escribir_json("data/inscripciones.json", inscripciones)
    print("Inscripción realizada con éxito. Estado: en espera.")

def cancelar_inscripcion():
    asistente_id = input("Ingrese su ID de asistente: ")
    evento_id = input("Ingrese el N° del evento a cancelar: ")
    inscripciones = u.leer_json("data/inscripciones.json")
    if inscripciones is None:
        print("No hay inscripciones.")
        return
    inscripcion = next((i for i in inscripciones if i['asistente_id'] == asistente_id and i['evento_id'] == evento_id), None)
    if inscripcion is None:
        print("Inscripción no encontrada.")
        return
    if inscripcion['estado'] == "cancelado":
        print("La inscripción ya está cancelada.")
        return
    inscripcion['estado'] = "cancelado"
    u.escribir_json("data/inscripciones.json", inscripciones)
    print("Inscripción cancelada con éxito.")

def boletos_incripciones():
    asistente_id = input("Ingrese su ID de asistente: ")
    inscripciones = u.leer_json("data/inscripciones.json")
    if inscripciones is None:
        print("No hay inscripciones.")
        return
    mis_inscripciones = [i for i in inscripciones if i['asistente_id'] == asistente_id]
    if len(mis_inscripciones) == 0:
        print("No tiene inscripciones.")
        return
    print("\n>>>> 🎫 Mis Inscripciones <<<<<\n")
    for i in mis_inscripciones:
        print(f"Evento N°: {i['evento_id']}, Estado: {i['estado']}")
    print()

def actualizar_estado_inscripcion():
    asistente_id = input("Ingrese su ID de asistente: ")
    evento_id = input("Ingrese el N° del evento: ")
    nuevo_estado = input("Ingrese el nuevo estado (confirmado/cancelado): ").lower()
    if nuevo_estado not in ["confirmado", "cancelado"]:
        print("Estado inválido. Debe ser 'confirmado' o 'cancelado'.")
        return
    inscripciones = u.leer_json("data/inscripciones.json")
    if inscripciones is None:
        print("No hay inscripciones.")
        return
    inscripcion = next((i for i in inscripciones if i['asistente_id'] == asistente_id and i['evento_id'] == evento_id), None)
    if inscripcion is None:
        print("Inscripción no encontrada.")
        return
    # Leer eventos para verificar capacidad y bloqueo (solo necesario si se confirma)
    eventos = u.leer_json("data/eventos.json")
    evento = None
    if eventos is not None:
        evento = next((e for e in eventos if e['id'] == evento_id), None)

    # Si el nuevo estado es 'confirmado' debemos verificar que la inscripción esté en 'en espera'
    if nuevo_estado == "confirmado":
        if inscripcion['estado'] != "en espera":
            print("Solo se puede confirmar la inscripción si está en 'en espera'.")
            return
        if evento is None:
            print("Evento no encontrado.")
            return
        if evento.get("bloqueado", False):
            print("Las inscripciones para este evento están bloqueadas.")
            return

        # Contar confirmados actuales
        count_confirmados = sum(1 for i in inscripciones if i['evento_id'] == evento_id and i['estado'] == 'confirmado')
        try:
            capacidad = int(evento['capacidad'])
        except Exception:
            print("Capacidad del evento inválida.")
            return
        if count_confirmados + 1 > capacidad:
            print("El evento ya está lleno y no hay más cupos disponibles.")
            # Bloquear el evento
            evento["bloqueado"] = True
            u.escribir_json("data/eventos.json", eventos)
            return

        # Confirmar la inscripción
        inscripcion['estado'] = nuevo_estado
        u.escribir_json("data/inscripciones.json", inscripciones)
        print(f"Estado actualizado a '{nuevo_estado}' con éxito.")
        # Verificar si ahora está lleno y bloquear
        count_confirmados += 1
        if count_confirmados == capacidad:
            evento["bloqueado"] = True
            u.escribir_json("data/eventos.json", eventos)
            print("El evento ha alcanzado su capacidad máxima y ha sido bloqueado automáticamente.")
    else:
        # Si es 'cancelado' permitimos cancelarlo desde cualquier estado (a menos que ya esté cancelado)
        if inscripcion['estado'] == "cancelado":
            print("La inscripción ya está cancelada.")
            return
        inscripcion['estado'] = nuevo_estado
        u.escribir_json("data/inscripciones.json", inscripciones)
        print(f"Estado actualizado a '{nuevo_estado}' con éxito.")