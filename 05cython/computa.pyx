
import cython

from libc.math cimport sqrt

def computar(fim: cython.int, inicio : cython.int = 1):
    pos : cython.int = inicio
    fator : cython.int = 1000 * 1000

    with nogil:  # aqui ele só vai executar em liguagem C, removendo o GIL do python
        while pos < fim:
            pos += 1
            sqrt((pos - fator) * (pos - fator))