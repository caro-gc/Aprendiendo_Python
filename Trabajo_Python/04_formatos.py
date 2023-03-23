# Formatos de impresión
edad = 27
estatura = 1.57
print('La edad es:', edad)
print('La estatura es:', estatura)
# 1ra manera de uso de formato:
print('La edad es:', edad, 'y la estatura es:', estatura)
# 2da manera de uso de formato (la mas utilizada):
print(f'La edad es: {edad} y la estatura es: {estatura}')
# 3ra manera de uso de formato:
print('La edad es: {} y la estatura es: {}'.format(edad, estatura))
print('la edad mas la estatura es:', edad + estatura)
print(f'la edad mas la estatura es: {edad + estatura}')
print('la edad mas la estatura es: {}'.format(edad + estatura))
suma = edad + estatura
print(f'la edad mas la estatura es: {suma}')
