import multiprocessing

def calcular(dado):
    return dado ** 2

def imprimir_nome_processo():
    print(f'Iniciando o processo com nome: {multiprocessing.current_process().name}')

def main():
    tamanho_pool = multiprocessing.cpu_count() * 2
    print(f'Tamanho do pool: {tamanho_pool}')
    
    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=imprimir_nome_processo)  # o initializer , executa uma função antes de executar cada processo
    
    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)
    
    print(f'Saídas : {saidas}')
    
    pool.close()  # pode mandar ver na execução que eu não vou enviar nenhuma função
    pool.join()  # cada processo que foi criado, execute até o fim

if __name__ == '__main__':
    main()