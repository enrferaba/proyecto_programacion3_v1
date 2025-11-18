#ifndef _ESTADOASIGNACION_H_
#define _ESTADOASIGNACION_H_

#include<iostream>
#include"solucionasignacion.h"

using namespace std;

class EstadoAsignacion
{
	private:
		SolucionAsignacion sol;
		int nVisitados;
		int nValidos;
		int nTotal;
		
	public:
		//Constructor
		EstadoAsignacion(int n)
		{
			setNTotal(n);
			setNValidos(0);
			setNVisitados(0);
		}
		
		//Observadores
		SolucionAsignacion getSolucion() const {return sol;}
		int getNVisitados() const {return nVisitados;}
		int getNValidos() const {return nValidos;}
		int getNTotal() const {return nTotal;}
		
		//Modificadores
		void setSolucion(SolucionAsignacion const & s){sol=s;}
		void setNVisitados(int n){nVisitados=n;}
		void setNValidos(int n){nValidos=n;}
		void setNTotal(int n){nTotal=n;}
		
		//Funciones de estado
		void avanza(Agente const & a);
		void retrocede(Agente const & a);
		list <Agente> getAlternativas(Agente const & a);
		Agente getMejorAlternativa(Agente const & a);
		bool esFinal();
		


};

#endif
