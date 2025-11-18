#include<iostream>
#include"estadoasignacion.h"

using namespace std;

//Funciones de estado
void EstadoAsignacion::avanza(Agente const & a)
{
	sol.addAgente(a);
	setNValidos(getNValidos()+a.getCantidad());
	setNVisitados(getNVisitados()+1);
	
}

void EstadoAsignacion::retrocede(Agente const & a)
{
	sol.deleteAgente(a);
	setNValidos(getNValidos()-a.getCantidad());
	setNVisitados(getNVisitados()-1);
}

list <Agente> EstadoAsignacion::getAlternativas(Agente const & a)
{
	list<Agente> l;
	l.push_back(a);
	if(getSolucion().getAgentesUsados().count(a.getCodAgente())==0 && getSolucion().getTareasAsignadas().count(a.getTarea().getCodTarea())==0){
		Agente ag(a);
		ag.setCantidad(1);
		l.push_back(ag);
	}
	return l;
}

Agente EstadoAsignacion::getMejorAlternativa(Agente const & a)
{
	if(getSolucion().getAgentesUsados().count(a.getCodAgente())==0 && getSolucion().getTareasAsignadas().count(a.getTarea().getCodTarea())==0){
		Agente ag(a);
		ag.setCantidad(1);
		return ag;
	}
	return a;
}

bool EstadoAsignacion::esFinal()
{
	return getNVisitados()==(getNTotal()*getNTotal()) || getNValidos()==getNTotal();	
	
}
