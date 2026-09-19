import modules.utils as u
import modules.messages as m
import modules.CRUD as c
def main():
    u.clear_screen()
    bandera=True
    while bandera:
        opcion1=m.primer_menu()
        if opcion1 == "2":
            c.nuevo_asistente()
            u.pause()
        elif opcion1 == "1":        
            isActive= True
            while isActive:            
                rol = c.login()       
                if rol == "asistente":
                    running = True    
                    while running:
                        u.clear_screen
                        opcion = m.menu_asistentes()
                        if opcion == "1":
                            u.clear_screen()
                            c.ver_eventos_disponibles()
                            u.pause()
                        elif opcion == "2":
                            u.clear_screen()
                            c.inscripcion_evento()
                            u.pause()
                        elif opcion == "3":
                            u.clear_screen()
                            c.boletos_incripciones()
                            u.pause()
                        elif opcion == "4":
                            u.clear_screen()
                            c.actualizar_estado_inscripcion()
                            u.pause()
                        elif opcion == "5":
                            u.clear_screen()
                            c.cancelar_inscripcion()
                            u.pause()
                        elif opcion == "0":                            
                            print("Cerrando sesión.")
                            running = False
                        else:
                            print("Opción inválida. Intente de nuevo.")
                            u.pause()
                        
                elif rol == "admin":
                    running = True
                    while running:
                        u.clear_screen()
                        option = m.menu_admin()
                        if option == "1":
                            u.clear_screen()
                            c.registro_eventos()
                            u.pause()
                        elif option == "2":
                            u.clear_screen()
                            c.registro_artistas()
                            u.pause()
                        elif option == "3":
                            u.clear_screen()
                            c.asignar_artista_evento()
                            u.pause()
                        elif option == "4":
                            u.clear_screen()
                            c.monitorear_aforo()
                            u.pause()
                        elif option == "5":
                            u.clear_screen()
                            running_reportes = True
                            while running_reportes:
                                opcion_reportes = m.menu_reportes()
                                if opcion_reportes == "1":
                                    u.clear_screen()
                                    c.participacion_artistas()
                                    u.pause()
                                elif opcion_reportes == "2":
                                    u.clear_screen()
                                    c.ver_proximos_eventos()
                                    u.pause()
                                elif opcion_reportes == "3":
                                    u.clear_screen()
                                    c.listado_asistentes()
                                    u.pause()
                                elif opcion_reportes == "4":
                                    u.clear_screen()
                                    c.eventos_menos_asistentes()
                                    u.pause()
                                elif opcion_reportes == "0":
                                    running_reportes = False
                                    u.clear_screen()
                                else:
                                    print("Opción inválida. Intente de nuevo.")
                                    u.pause()
                        elif option == "0":
                            running= False
                            u.clear_screen()

                elif rol == "artista":
                    running = True    
                    while running:
                        u.clear_screen()
                        option = m.menu_artistas()
                        if option == "1":
                            u.clear_screen()
                            c.agenda_presentaciones()
                            u.pause()
                        elif option == "2":
                            u.clear_screen()
                            c.detalles_eventos()
                            u.pause()
                        elif option == "0":
                            running= False
                            u.clear_screen()


                elif rol == "salir":
                    u.clear_screen()
                    isActive=False


        elif opcion1 == "0":
            bandera=False
            print("¡Hasta luego!")




if __name__ == "__main__":
    main()