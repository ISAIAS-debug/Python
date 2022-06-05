from multiprocessing import Pool
import time

CONTADOR = 500000


def contando(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    p1 = pool.apply_async(contando, [CONTADOR//2])
    p2 = pool.apply_async(contando, [CONTADOR//2])
    pool.close()
    pool.join()
    fim = time.time()

   
    print(f'O tempo gasto para dois processos em Poll foi de aproxidamente  de: {fim - inicio}')
