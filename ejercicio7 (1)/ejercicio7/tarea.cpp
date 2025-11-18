#include<iostream>
#include"tarea.h"

using namespace std;		
		
//SOBRECARGA
Tarea & Tarea::operator = (Tarea const & t)
{
	setCodTarea(t.getCodTarea());
	setCoste(t.getCoste());
	return *this;
}

bool Tarea::operator < (Tarea const & t) const
{
	return getCoste() < t.getCoste();
}

//FUNCION DE SALIDA
void Tarea::mostrar() const
{
	cout << "(Tarea: " << getCodTarea() << ", Coste: " << getCoste() << ")" << endl;
}
