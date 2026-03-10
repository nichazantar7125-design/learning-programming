Algoritmo geometric_areas
	// Declare variables or constants
	constante_PI<-3.1416
	
	// Declare variables
	Definir lado, baseRec, alturaRec, baseTri, alturaTri, radio Como Real
	Definir areaCuadrado, areaRectangulo, areaTriangulo, areaCirculo, totalAreas Como Real
	
	// Inputs
	Escribir "Ingrese el lado del cuadrado:"
	Leer lado
	
	Escribir "Ingrese la base del rect�ngulo:"
	Leer baseRec
	Escribir "Ingrese la altura del rect�ngulo:"
	Leer alturaRec
	
	Escribir "Ingrese la base del tri�ngulo:"
	Leer baseTri
	Escribir "Ingrese la altura del tri�ngulo:"
	Leer alturaTri
	
	Escribir "Ingrese el radio del c�rculo:"
	Leer radio
	
	// Processes
	areaCuadrado <- lado * lado
	areaRectangulo <- baseRec * alturaRec
	areaTriangulo <- (baseTri * alturaTri) / 2
	areaCirculo <- PI * (radio * radio)
	totalAreas <- areaCuadrado + areaRectangulo + areaTriangulo + areaCirculo
	
	// Outputs
	Escribir "El �rea del cuadrado es: ", areaCuadrado
	Escribir "El �rea del rect�ngulo es: ", areaRectangulo
	Escribir "El �rea del tri�ngulo es: ", areaTriangulo
	Escribir "El �rea del c�rculo es: ", areaCirculo
	Escribir "La Suma total de todas las �reas es: ", totalAreas
FinAlgoritmo
