#ifndef _SOLUCIONASIGNACION_H_
#define _SOLUCIONASIGNACION_H_

#include<iostream>
#include<list>
#include<set>
#include"agente.h"

using namespace std;

class SolucionAsignacion
{
	private:
		list <Agente> agentes;
		set <int> agentes_usados;
		set <int> tareas_asignadas;
		int costeTotal;
		
	public:
		//Constructor
		SolucionAsignacion()
		{
			setCosteTotal(0);
		}
		
		SolucionAsignacion(SolucionAsignacion const & s)
		{
			*this = s;
		}
		
		//Destructor
		~SolucionAsignacion()
		{
			agentes.clear();
			agentes_usados.clear();
			tareas_asignadas.clear();
			setCosteTotal(0);
		}
		
		//Observadores
		list <Agente> getAgentes() const {return agentes;}
		set <int> getAgentesUsados() const {return agentes_usados;}
		set <int> getTareasAsignadas() const {return tareas_asignadas;}
		int getCosteTotal() const {return costeTotal;}
		
		//Modificadores
		void setAgentes(list <Agente> const & l){agentes=l;}
		void setAgentesUsados(set <int> const & s){agentes_usados=s;}
		void setTareasAsignadas(set <int> const & s){tareas_asignadas=s;}
		void setCosteTotal(int c){costeTotal=c;}
		
		//Sobrecarga
		SolucionAsignacion & operator = (SolucionAsignacion const & s);
		bool operator > (SolucionAsignacion const & s) const;
		
		//Funcion de salida
		void mostrar() const;
		
		//Funciones para insertar y eliminar
		void addAgente(Agente const & a);
		void deleteAgente(Agente const & a);
		
};

#endif
