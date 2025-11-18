#include<iostream>
#include"solucionasignacion.h"

using namespace std;
		
//Sobrecarga
SolucionAsignacion & SolucionAsignacion::operator = (SolucionAsignacion const & s)
{
	setAgentes(s.getAgentes());
	setAgentesUsados(s.getAgentesUsados());
	setTareasAsignadas(s.getTareasAsignadas());
	setCosteTotal(s.getCosteTotal());
	return *this;
}

bool SolucionAsignacion::operator > (SolucionAsignacion const & s) const
{
	return getCosteTotal() < s.getCosteTotal();
}

//Funcion de salida
void SolucionAsignacion::mostrar() const
{
	cout << "Coste de la solucion: " << getCosteTotal() << endl;
	list <Agente>::const_iterator it = agentes.begin();
	while(it!=agentes.end())
	{
		it->mostrar();
		it++;
	}
}

//Funciones para insertar y eliminar
void SolucionAsignacion::addAgente(Agente const & a)
{
	if(a.getCantidad()){
		agentes.push_back(a);
		agentes_usados.insert(a.getCodAgente());
		tareas_asignadas.insert(a.getTarea().getCodTarea());
		setCosteTotal(getCosteTotal()+a.getTarea().getCoste());
	}
	
}

void SolucionAsignacion::deleteAgente(Agente const & a)
{
	if(a.getCantidad()){
		agentes.pop_back();
		agentes_usados.erase(a.getCodAgente());
		tareas_asignadas.erase(a.getTarea().getCodTarea());
		setCosteTotal(getCosteTotal()-a.getTarea().getCoste());	
	}
}
