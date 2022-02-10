// area_triangulo.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "conio.h"
#include "Triangulo.h"

using namespace std;

void main()
{
	float b,h,area;
	Triangulo tria;
	cout<<"Ingrese la base: ";cin>>b;
	cout<<"Ingrese la altura: ";cin>>h;
	area=tria.calculararea(b,h);
	cout<<"El area del triangulo es: "<<area<<endl;
	getch();
}