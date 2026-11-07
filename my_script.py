import platform
import datetime

AUTOR = "David Gustavo Moreno Morán | Angélica María Martínez Carmona"

def main():
    print(f"Autor: {AUTOR}")
    print(f"Sistema Operativo: {platform.system()} {platform.release()}")
    print(f"Fecha y hora desde Python: {datetime.datetime.now()}")

if __name__ == "__main__":
    main()