#ifndef _PROBLEMAASIGNACION_H_
#define _PROBLEMAASIGNACION_H_

#include<iostream>
#include"estadoasignacion.h"

using namespace std;

class ProblemaAsignacion
{
	private:
		list <Agente> agentes_disponibles;
		int n;
		SolucionAsignacion mejorSol;
		
	public:
		//Constructor
		ProblemaAsignacion(int ** c, string * nombre, int n)
		{
			for(int i=0; i<n; i++)
			{
				for(int j=0; j<n; j++)
				{
					agentes_disponibles.push_back(Agente(nombre[i],i,0,Tarea(j,c[i][j])));
				}
			}
			agentes_disponibles.sort();
			setN(n);
		}
		
		//Observadores
		list <Agente> getAgentesDisponibles() const {return agentes_disponibles;}
		int getN() const {return n;}
		SolucionAsignacion getMejorSolucion() const {return mejorSol;}
		
		//Modificadores
		void setAgentesDisponibles(list <Agente> const & l){agentes_disponibles=l;}
		void setN(int nn){n=nn;}
		void setMejorSolucion(SolucionAsignacion const & s){mejorSol=s;}
		
		//Funciones de los algoritmos
		SolucionAsignacion ejecutaBacktracking();
		void bt(EstadoAsignacion & e);
		SolucionAsignacion ejecutaVoraz();
		void vorazR(EstadoAsignacion & e);
		void actualizaMejorSolucion(EstadoAsignacion & e);
};

#endif
