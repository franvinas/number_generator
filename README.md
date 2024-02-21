# number_generator

El programa toma como input una imágen de fondo y una serie de dígitos y el símbolo "#" para hacer un 'collage' pegando los números en series de 1 a n y generando n imágenes distintas, que se guardan en el directorio 'generated'.

Toma la imágen background.png y los dígitos "white n.png" y el símbolo # 'white #.png" del directorio 'static'.

## Parámetros
Range define desde qué valor a qué valor se producen las imágenes.
```
[--range RANGE RANGE]  # RANGE type = int
```
Position define el porcentaje (valor de 0 a 1) de altura de la foto de background en el que deben ubicase los dígitos, tomando el punto más alto de los dígitos.
```
[--position POSITION]   # POSITION type = float
```

Correr el programa con
```
python main.py --range RANGE RANGE --position POSITION
```
