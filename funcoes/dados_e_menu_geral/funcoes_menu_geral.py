from time import sleep

def menu(msg):
    print()
    sleep(1)
    print("-" * 30)
    print(f"{msg:^30}")
    print("-" * 30)
    print("")


def mostrar_menu_geral():
    menu("REFORÇO ESCOLAR")

    print("""    1 - Alunos
    2 - Notas
    3 - Mensalidades
    0 - Sair""")
