import multiprocessing

def ping(conn):
    conn.send('Douglas')
    

def pong(conn):
    msg = conn.recv()
    print(f'{msg} Amorim')

def main():
    conn1, conn2 = multiprocessing.Pipe(True)  # ambos vão tanto enviar quanto receber, o False um só envia e um só recebe
    
    p1 = multiprocessing.Process(target=ping, args=(conn1,))
    p2 = multiprocessing.Process(target=pong, args=(conn2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

if __name__ == '__main__':
    main()