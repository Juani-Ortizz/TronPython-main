def square(x, y, size, color):#dibuja un cuadrado en turtle con los parametros xy donde empieza size lado del cuadrado 
    import turtle#color es el color del cuadrado
    turtle.up()
    turtle.goto(x, y)  #posicion del cuadrado
    turtle.down()
    turtle.color(color) #color del cuadradi
    turtle.begin_fill() #rellena el cuadrado del color determinado

    for count in range(4):
        turtle.forward(size)
        turtle.left(90)

    turtle.end_fill()
