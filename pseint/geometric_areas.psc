Algoritmo geometric_areas
	// Declaración de constante
	Definir pi_valor Como Real
	pi_valor <- 3.1416
	

	// Declaración de variables
	Definir lado Como Real
	Definir baseRect, alturaRect Como Real
	Definir baseTri, alturaTri Como Real
	Definir radio Como Real
	
	Definir areaCuadrado, areaRectangulo, areaTriangulo, areaCirculo Como Real
	Definir totalAreas Como Real
	
	// Solicitar datos para el cuadrado
	Escribir "Ingrese el lado del cuadrado:"
	Leer lado
	areaCuadrado <- lado * lado
	
	// Solicitar datos para el rectángulo
	Escribir "Ingrese la base del rectángulo:"
	Leer baseRect
	Escribir "Ingrese la altura del rectángulo:"
	Leer alturaRect
	areaRectangulo <- baseRect * alturaRect
	
	// Solicitar datos para el triángulo
	Escribir "Ingrese la base del triángulo:"
	Leer baseTri
	Escribir "Ingrese la altura del triángulo:"
	Leer alturaTri
	areaTriangulo <- (baseTri * alturaTri) / 2
	
	// Solicitar datos para el círculo
	Escribir "Ingrese el radio del círculo:"
	Leer radio
	areaCirculo <- PI * (radio * radio)
	
	// Calcular total de áreas
	totalAreas <- areaCuadrado + areaRectangulo + areaTriangulo + areaCirculo
	
	// Mostrar resultados
	Escribir "Área del cuadrado: ", areaCuadrado
	Escribir "Área del rectángulo: ", areaRectangulo
	Escribir "Área del triángulo: ", areaTriangulo
	Escribir "Área del círculo: ", areaCirculo
	Escribir "Total de todas las áreas: ", totalAreas
	
FinAlgoritmo
