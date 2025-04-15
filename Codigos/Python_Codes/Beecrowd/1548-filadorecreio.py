# -*- coding: utf-8 -*-

def troca(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def empurra(L, n):
    i = 0
    while i < n-1:
        if L[i] < L[i+1]:
            troca(L, i, i+1)
        i += 1

def bsort(L):
    copia = L[:]
    n = len(copia) # tamanho da parte não ordenada
    while n > 1:
        empurra(copia, n)
        n -= 1
    return copia

def nao_mudaram(a, b):
    qtd = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            qtd += 1
    return qtd

def converte(L, tipo):
    for i in range(len(L)):
        L[i] = tipo(L[i])

qtd_casos = int(input())

for i in range(qtd_casos):
    qtd_alunos = int(input())
    alunos = input().split()
    converte(alunos, int)
    ordenados = bsort(alunos)
    print(nao_mudaram(alunos, ordenados))