import computa
import datetime


def main():
    inicio = datetime.datetime.now()
    
    computa.computar(fim=50_000_000)
    
    tempo = datetime.datetime.now() - inicio
    
    print(f"Terminou em {tempo.total_seconds():.2f} segundos.")
    



if __name__ == '__main__':
    main()
    
"""
Terminou em 5.53 segundos.  # sem tipagem dos daods com cython ( com GIL )
Terminou em 0.09 segundos.  # com a tipagem em cython ( com GIL )
Terminou em 0.09 segundos.  # com a tipagem em cython ( sem GIL )
"""