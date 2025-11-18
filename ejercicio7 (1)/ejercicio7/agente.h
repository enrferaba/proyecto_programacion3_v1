#ifndef _AGENTE_H_
#define _AGENTE_H_

#include<iostream>
#include"tarea.h"

using namespace std;

class Agente
{
	private:
		int codAgente;
		string nombre;
		int cantidad;
		Tarea tarea;
		
		
	public:
		//Constructor
		Agente(string n="", int c=-1, int ca=0, Tarea const & t=Tarea())
		{
			setCodAgente(c);
			setNombre(n);
			setCantidad(ca);
			setTarea(t);
		}

		Agente(Agente const & a)
		{
			*this = a;
		}
		
		//Observadores
		int getCodAgente() const {return codAgente;}
		string getNombre() const {return nombre;}
		int getCantidad() const {return cantidad;}
		Tarea getTarea() const {return tarea;}
		
		//Modificadores
		void setCodAgente(int c) {codAgente=c;}
		void setNombre(string n) {nombre=n;}
		void setCantidad(int c) {cantidad=c;}
		void setTarea(Tarea const & t) {tarea=t;}
		
		//Sobrecarga
		Agente & operator=(Agente const & a);
		bool operator < (Agente const & a) const;
		
		//Funcion de salida
		void mostrar() const;
};

#endif
