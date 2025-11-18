#include<iostream>
#include"problemaasignacion.h"

using namespace std;

//Funciones de los algoritmos
SolucionAsignacion ProblemaAsignacion::ejecutaBacktracking()
{
	EstadoAsignacion e(getN());
	bt(e);
	return getMejorSolucion();
}

void ProblemaAsignacion::bt(EstadoAsignacion & e)
{
	if(e.esFinal())
	{
		actualizaMejorSolucion(e);
	}
	else
	{
		list <Agente>::iterator it=agentes_disponibles.begin();
		advance(it,e.getNVisitados());
		list <Agente> alts = e.getAlternativas(*it);
		list <Agente>::iterator it2 = alts.begin();
		while(it2!=alts.end())
		{
			e.avanza(*it2);
			bt(e);
			e.retrocede(*it2);
			it2++;
		}
	}
}

SolucionAsignacion ProblemaAsignacion::ejecutaVoraz()
{
	EstadoAsignacion e(getN());
	vorazR(e);
	return getMejorSolucion();
}

void ProblemaAsignacion::vorazR(EstadoAsignacion & e)
{
	if(e.esFinal())
	{
		actualizaMejorSolucion(e);
	}
	else
	{
		list <Agente>::iterator it=agentes_disponibles.begin();
		advance(it,e.getNVisitados());
		Agente alt = e.getMejorAlternativa(*it);
		e.avanza(alt);
		vorazR(e);
	}
}

void ProblemaAsignacion::actualizaMejorSolucion(EstadoAsignacion & e)
{
	if(e.getNValidos() == getN()){
		if(getMejorSolucion().getCosteTotal()==0 || e.getSolucion() > getMejorSolucion())
		{
			setMejorSolucion(e.getSolucion());	
		}
	}
}
