#include<iostream>
#include"problemaasignacion.h"

using namespace std;


int main()
{
	int n=3;
	int ** m = new int *[n];
	for(int i=0; i<n; i++)
	{
		m[i]=new int[n];
	}
	
	string * nombres = new string[n];
	
	//Rellenamos un ejemplos
	m[0][0]=4;
	m[0][1]=9;
	m[0][2]=1;
	m[1][0]=7;
	m[1][1]=2;
	m[1][2]=3;
	m[2][0]=8;
	m[2][1]=3;
	m[2][2]=5;
	
	nombres[0]="Antonio";
	nombres[1]="Pedro";
	nombres[2]="Juan";
	
	ProblemaAsignacion p1(m,nombres,n);
	ProblemaAsignacion p2(m,nombres,n);
	
	cout << "Voraz: " << endl;
	SolucionAsignacion sV = p1.ejecutaVoraz();
	sV.mostrar();
	
	cout << "Backtracking: " << endl;
	SolucionAsignacion sBt = p2.ejecutaBacktracking();
	sBt.mostrar();
	
	for(int i=0; i<n; i++)
	{
		delete [] m[i];
	}
	
	delete [] m;

	return 0;
}
