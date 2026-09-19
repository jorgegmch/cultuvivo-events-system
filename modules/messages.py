import modules.utils as u
def primer_menu():
    print("⭐ Bienvenido al Programa Eventos CultuVivo ⭐\n")
    print("Seleccione una opción! 📋")
    print("1. 🔑 Ingresar")
    print("2. 📝 Registrarse como asistente")
    print("0. 🚪 Salir. ")
    opcion=input(">>  ")
    return opcion


def menu_asistentes():
    u.clear_screen()

    print(">>>> 🎟️  Menú de Asistentes <<<<<")
    print("1. ✅  Ver eventos disponibles")
    print("2. ✍️  Inscribirse en un evento")
    print("3. 📄  Ver mis inscripciones")
    print("4. 🔄  Actualizar estado de inscripción")
    print("5. ❌  Cancelar inscripción")
    print("0. 🚪 Cerrar Sesion")
    opcion=input(">>  ")
    return opcion

def menu_artistas():
    u.clear_screen()
    print(">>>> 🎤 Menú de Artistas <<<<<")
    print("1. 📅 Ver agenda de presentaciones")
    print("2. 📋 Ver detalles de eventos asignados")
    print("0. 🚪 Cerrar Sesion")
    opcion=input(">>  ")
    return opcion

def menu_admin():
    print("★★★ 👑 Administrador ★★★\n")
    print("Seleccione una opción\n")
    print("1. ➕ Crear Evento")
    print("2. 🎭 Agregar artistas")
    print("3. 🔗 Asignar Artistas a Evento")
    print("4. 📊 Monitorear capacidad eventos")
    print("5. 📈 Reportes")
    print("0. 🚪 Cerrar Sesion")
    opcion= input(">>   ")
    return opcion

def menu_reportes():
    print("★★★ 📈 Reportes ★★★\n")
    print("Seleccione una opción\n")
    print("1. 🎭 Lista de artistas que han participado en eventos")
    print("2. 📅 Eventos proximos")
    print("3. 👥 Lista de asistentes registrados")#registrados en el programa en general
    print("4. 📉 Eventos con menos asistentes")
    print("0. 🚪 Salir. ")
    opcion= input(">>   ")
    return opcion