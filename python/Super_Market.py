while True:

    main_menu()

    try:
        option = int(input("Seleccione una opción: "))
    except ValueError:
        print("\nERROR: Debe ingresar un número.")
        input("Presione Enter para continuar...")
        continue

    if option == 1:
        register_client()

    elif option == 2:
        register_product()

    elif option == 3:
        list_clients()

    elif option == 4:
        list_products()

    elif option == 5:
        search_client()

    elif option == 6:
        search_product()

    elif option == 7:
        update_client()

    elif option == 8:
        update_product()

    elif option == 9:
        delete_client()

    elif option == 10:
        delete_product()

    elif option == 11:
        print("¡Hasta luego!")
        break

    else:
        print("\nERROR: La opción no existe en el menú.")
        input("Presione Enter para continuar...")
