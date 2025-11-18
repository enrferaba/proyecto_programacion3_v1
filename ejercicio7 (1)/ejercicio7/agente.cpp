#include<iostream>
#include"tarea.h"
#include"agente.h"

using namespace std;

//Sobrecarga
Agente & Agente::operator=(Agente const & a)
{
	setCodAgente(a.getCodAgente());
	setNombre(a.getNombre());
	setCantidad(a.getCantidad());
	setTarea(a.getTarea());
	return *this;
}
bool Agente::operator < (Agente const & a) const
{
	return getTarea() < a.getTarea();
}

//Funcion de salida
void Agente::mostrar() const
{
	cout << "Agente: " << getNombre() << "(cod: " << getCodAgente() << ") hace Tarea ";
	getTarea().mostrar();
}
