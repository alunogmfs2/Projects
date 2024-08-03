#pragma once
#include <GLFW/glfw3.h>
#include <iostream>

class Jogador
{
public:
	double xjogador;
	double yjogador;

	Jogador(double x) {
		xjogador = x;
		yjogador = -0.15f;
		size = 0.3;
	}

	void desenharJogador() {
		for (int i = 0; i < 10; i++) {
			desenharQuadrado(xjogador, yjogador, size);
			yjogador += size / 10;
		}
	}

private:
	double size;

	void desenharQuadrado(double x, double y, double size) {
		double halfSize = size / 2.0f / 10;

		glBegin(GL_QUADS);
		glVertex2f(x - halfSize, y - halfSize); // Vértice inferior esquerdo
		glVertex2f(x + halfSize, y - halfSize); // Vértice inferior direito
		glVertex2f(x + halfSize, y + halfSize); // Vértice superior direito
		glVertex2f(x - halfSize, y + halfSize); // Vértice superior esquerdo
		glEnd();
	}
};

