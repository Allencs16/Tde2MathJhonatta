import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def translation():
    objeto = np.array([[0, 1, 1, 0], [0, 0, 1, 1]])

    dx, dy = 2, 3
    translacao = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

    objeto_transladado = np.dot(translacao, np.vstack([objeto, np.ones_like(objeto[0, :])]))

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(objeto[0, :], objeto[1, :], 'b-', label='Objeto original')
    ax.plot(objeto_transladado[0, :], objeto_transladado[1, :], 'r-', label='Objeto transladado')
    ax.legend()
    plt.show()


def rotation():
    objeto = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]])

    ponto = np.array([1, 1, 1])

    angulo = np.pi / 4

    rotacao = np.array(
        [[np.cos(angulo), -np.sin(angulo), 0, ponto[0] * (1 - np.cos(angulo)) + ponto[1] * np.sin(angulo)],
         [np.sin(angulo), np.cos(angulo), 0, ponto[1] * (1 - np.cos(angulo)) - ponto[0] * np.sin(angulo)],
         [0, 0, 1, 0],
         [0, 0, 0, 1]])

    objeto_rotacionado = np.dot(rotacao, objeto)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(objeto[0, :], objeto[1, :], objeto[2, :], 'b-', label='Objeto original')
    ax.plot(objeto_rotacionado[0, :], objeto_rotacionado[1, :], objeto_rotacionado[2, :], 'r-',
            label='Objeto rotacionado')
    ax.scatter(ponto[0], ponto[1], ponto[2], s=100, c='g', label='Ponto de rotação')
    ax.legend()
    plt.show()


def scale():
    objeto = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]])

    ponto = np.array([1, 1, 0])

    T1 = np.array([[1, 0, 0, -ponto[0]], [0, 1, 0, -ponto[1]], [0, 0, 1, -ponto[2]], [0, 0, 0, 1]])

    sx, sy, sz = 2, 3, 1
    escala = np.array([[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]])

    T2 = np.array([[1, 0, 0, ponto[0]], [0, 1, 0, ponto[1]], [0, 0, 1, ponto[2]], [0, 0, 0, 1]])

    transformacao = np.dot(np.dot(T2, escala), T1)
    objeto_escalonado = np.dot(transformacao, objeto)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(objeto[0, :], objeto[1, :], objeto[2, :], 'b-', label='Objeto original')
    ax.plot(objeto_escalonado[0, :], objeto_escalonado[1, :], objeto_escalonado[2, :], 'r-', label='Objeto escalonado')
    ax.scatter(ponto[0], ponto[1], ponto[2], color='black', marker='o', s=100)
    ax.legend()
    plt.show()


def reflection():
    objeto = np.array([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]])

    reflexao = np.array([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    objeto_refletido = np.dot(reflexao, objeto)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot(objeto[0, :], objeto[1, :], objeto[2, :], 'b-', label='Objeto original')
    ax.plot(objeto_refletido[0, :], objeto_refletido[1, :], objeto_refletido[2, :], 'r-', label='Objeto refletido')
    ax.legend()
    plt.show()