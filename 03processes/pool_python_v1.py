import multiprocessing

def calcular(dado):
    return dado ** 2


def main():
    tamanho_pool = multiprocessing.cpu_count() * 2
    print(f'Tamanho do pool: {tamanho_pool}')
    
    pool = multiprocessing.Pool(processes=tamanho_pool)
    
    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)
    
    print(f'Saídas : {saidas}')
    
    pool.close()  # pode mandar ver na execução que eu não vou enviar nenhuma função
    pool.join()  # cada processo que foi criado, execute até o fim

if __name__ == '__main__':
    main()