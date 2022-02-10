#include "StdAfx.h"
#include "Triangulo.h"


Triangulo::Triangulo(void)
{
}


Triangulo::~Triangulo(void)
{
}
float Triangulo::calculararea(float b, float h)
{
	area=(b*h)/2;
	return area;
}
