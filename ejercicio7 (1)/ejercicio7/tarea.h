#ifndef _TAREA_H_
#define _TAREA_H_

#include<iostream>

using namespace std;

class Tarea
{
	private:
		int codTarea;
		int coste;
	public:
		//CONSTRUCTOR
		Tarea(int cod=-1, int c=-1)
		{
			setCodTarea(cod);
			setCoste(c);
		}
		
		Tarea(Tarea const & t)
		{
			*this = t;
		}
		
		//OBSERVADORES
		int getCodTarea() const {return codTarea;}
		int getCoste() const {return coste;}
		
		//MODIFICADORES
		void setCodTarea(int cod){codTarea=cod;}
		void setCoste(int c){coste=c;}
		
		//SOBRECARGA
		Tarea & operator = (Tarea const & t);
		bool operator < (Tarea const & t) const;
		
		//FUNCION DE SALIDA
		void mostrar() const;
		
};

#endif
