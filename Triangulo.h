#pragma once
class Triangulo
{
	//atributos
private:
	float base;
	float altura;
	float area;
	//metodos - procedimientos - prototipos
public:
	Triangulo(void);
	~Triangulo(void);
	float calculararea(float b, float h);
};

