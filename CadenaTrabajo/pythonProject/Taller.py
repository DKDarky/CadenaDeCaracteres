#1. Teniendo en cuenta las siguientes variables que describen su edad, nombre y comida favorita, genera
#una cadena para presentarse: ingresamos las variables dadas por el documento y utilizamos el print para que
#imprima los datos dados en la cadena
name = "Luis"
age = 27
favoriteFood = "Pasta con salsa boloñesa"
print(f"Hola!Mi nombre es {name}, tengo {age} años, y mi comida favorita es  {favoriteFood}")

#2. Crea un código que solicite al usuario su nombre completo. Luego deberá contar el número de letras
#e su nombre, ignorando los espacios. Finalmente, debe saludar al usuario e informarle la longitud de
#su nombre.
fullname = input('Ingresa su nombre completo:')
print(f'Hola,{fullname}! Tu nombre tiene {len(fullname.replace(" ", ""))}, excluyendo los espacios')

#3. El analista de datos de una prestigiosa empresa láctea de la ciudad de Popayán, calculó las cifras de
#ventas del último trimestre: el porcentaje de aumento de las ventas y crecimiento de ingresos. Genere
#una cadena que le permita mostrar los porcentajes.
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078

print(f'Las ventas de la empresa láctea aumentaron un {increaseSalesPercent:.2f}% y '
      f'los ingresos crecieron un {revenueGrowthPercent:.2f}%')

#4. Se proporciona un mensaje secreto codificado en una cadena, para decodificar el mensaje: "Omita
#los primeros tres caracteres y luego omita todos los demás caracteres".
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
result= secretMessage[3::2]
print(result)

#5. Se proporciona una frase y luego se debe mostrar el número de palabras en esa frase.
text = '''El nombre "Python" viene dado por la
afición de Van Rossum al grupo Monty Python.'''

print(f'Número de palabras en la frase: {len(text.split())}')


#6. Escriba un programa que tome una cadena como entrada y reemplace todas las apariciones de la letra
# "a" con la letra "e".
word = "Camila"
print(word.replace('a','e'))

#7. Dada la siguiente frase, escriba un programa que invierta el orden de las palabras en esa frase.
sentence = '''La historia del lenguaje de programación Python'''
print(' '.join(sentence.split()[::-1]))
