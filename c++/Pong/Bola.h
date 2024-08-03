#pragma once
#include <GLFW/glfw3.h>
#include <iostream>

class Bola
{
public:
	double xbola;
	double ybola;
	double vxbola;
    double vybola;
    double raio;

    Bola() {
        xbola = 0.0f;
        ybola = 0.0f;

        vxbola = 0.01f;
        vybola = 0.02f;

        raio = 0.02f;
    }

    void desenharBola() {
        glBegin(GL_TRIANGLE_FAN);
        glVertex2f(xbola, ybola);
        for (int i = 0; i <= 360; i++) {
            float angle = i * 3.1415 / 180.0f;
            glVertex2f(xbola + cos(angle) * raio, ybola + sin(angle) * raio * 1.5);
        }

        glEnd();
    }

    void moverBola() {
        prenderBola();

        xbola += vxbola;
        ybola += vybola;

        std::cout << xbola + raio << std::endl << std::endl;
    }
private:
    void prenderBola() {
        if (xbola + raio >= 1.0f || xbola - raio <= -1.0f) {
            vxbola = -vxbola;
        }

        if (ybola + raio >= 1.0f || ybola - raio <= -1.0f) {
            vybola = -vybola;
        }
    }
};