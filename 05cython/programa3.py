import computa
import datetime
import multiprocessing

from concurrent.futures.process import ProcessPoolExecutor

def main():
    qtd_cores : int = multiprocessing.cpu_count()
    print(f"Realizando o processamento matemático com {qtd_cores} core(s)")
    
    inicio = datetime.datetime.now()
    
    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores + 1):
            ini = 50_000_000 * (n - 1) / qtd_cores
            fim = 50_000_000 * n / qtd_cores
            print(f'Core {n} procesando de {ini} a {fim}')
            executor.submit(computa.computar, inicio=ini, fim=fim)
    
    tempo = datetime.datetime.now() - inicio
    
    print(f"Terminou em {tempo.total_seconds():.2f} segundos.")
    

if __name__ == '__main__':
    main()
    
"""
Terminou em 5.53 segundos.  # sem tipagem dos daods com cython ( com GIL )
Terminou em 0.09 segundos.  # com a tipagem em cython ( com GIL )
Terminou em 0.09 segundos.  # com a tipagem em cython ( sem GIL )
Terminou em 0.04 segundos.  # com a tipagem em cython usando multiprocessing ( sem GIL )
"""