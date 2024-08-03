#include <GLFW/glfw3.h>
#include <iostream>
#include <vector>
#include <cmath>
#include "Bola.h"

using namespace std;

// Função de callback para ajustar o viewport quando a janela for redimensionada
void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
    glViewport(0, 0, width, height);
}

void desenharQuadrado(double x, double y, double size) {
    double halfSize = size / 2.0f / 10;

    glBegin(GL_QUADS);
    glVertex2f(x - halfSize, y - halfSize); // Vértice inferior esquerdo
    glVertex2f(x + halfSize, y - halfSize); // Vértice inferior direito
    glVertex2f(x + halfSize, y + halfSize); // Vértice superior direito
    glVertex2f(x - halfSize, y + halfSize); // Vértice superior esquerdo
    glEnd();
}

void desenharJogador(double x, double y, double size) {
    for (int i = 0; i < 10; i++) {
        desenharQuadrado(x, y, size);
        y += size / 10;
    }
}

int main() {
    // Inicializar a GLFW
    if (!glfwInit()) {
        std::cerr << "Falha ao inicializar a GLFW" << std::endl;
        return -1;
    }

    // Configurar o OpenGL (versão 2.1 para compatibilidade)
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 2);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 1);

    // Criar a janela GLFW
    GLFWwindow* window = glfwCreateWindow(640, 480, "Desenhar um Pixel com GLFW", NULL, NULL);
    if (!window) {
        std::cerr << "Falha ao criar a janela GLFW" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);

    // Configurar a função de callback para redimensionamento da janela
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    // Configurar o viewport inicial
    int width, height;
    glfwGetFramebufferSize(window, &width, &height);
    framebuffer_size_callback(window, width, height);

    // Variáveis para definir o tamanho e a posição do quadrado
    double size = 0.3;
    double xplayer1 = -0.9f; // Coordenada x do canto superior direito
    double yplayer1 = -0.15f; // Coordenada y do canto superior direito
    double xplayer2 = 0.9f;
    double yplayer2 = -0.15f;

    Bola bola;

    // Loop principal
    while (!glfwWindowShouldClose(window)) {
        // Limpar o buffer de cor
        glClear(GL_COLOR_BUFFER_BIT);

        // Processar entrada do usuário para redimensionar e mover o quadrado
        if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS) {
            yplayer1 += 0.03f; // Mover para cima
        }
        if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS) {
            yplayer1 -= 0.03f; // Mover para baixo
        }

        if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS) {
            yplayer2 += 0.03f; // Mover para cima
        }
        if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS) {
            yplayer2 -= 0.03f; // Mover para cima
        }

        if (bola.xbola + bola.raio >= xplayer2 && bola.ybola + bola.raio >= yplayer2 && bola.ybola + bola.raio <= yplayer2 + size ||
            bola.xbola - bola.raio <= xplayer1 && bola.ybola + bola.raio >= yplayer1 && bola.ybola + bola.raio <= yplayer1 + size) {
            bola.vxbola = -bola.vxbola;
        }

        bola.moverBola();


        // Definir a cor do quadrado (verde)
        glColor3f(1.0f, 1.0f, 1.0f);

        // Desenhar o quadrado na posição desejada
        desenharJogador(xplayer1, yplayer1, size);
        desenharJogador(xplayer2, yplayer2, size);

        bola.desenharBola();

        // Desenhar o círculo no centro da tela

        // Trocar os buffers
        glfwSwapBuffers(window);

        // Processar eventos
        glfwPollEvents();
    }

    // Encerrar a GLFW
    glfwDestroyWindow(window);
    glfwTerminate();

    return 0;
}
