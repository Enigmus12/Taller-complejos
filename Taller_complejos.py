import math


def suma (a,b):
    pr = a[0] + b[0]
    pi = a[1] +  b[1]

    print(pr,"+",pi,"i")
    return (pr,pi)

def multiplicacion (a,b):
    pr = (a[0] * b[0]) - (a[1] * b[1])
    pi = (a[0] *  b[1]) + (b[0] * a[1])

    print(pr,"+",pi,"i")
    return (pr,pi)

def resta (a,b):
    pr = a[0] - b[0]
    pi = a[1] -  b[1]

    print(pr,"+",pi,"i")
    return (pr,pi)

def division (a,b):
    pr = ((a[0] * b[0]) + (a[1] * b[1])) / ((b[0] ** 2) + (b[1] ** 2))
    pi = ((b[0] * a[1]) - (a[0] * b[1])) / ((b[0] ** 2) + (b[1] ** 2))

    print(pr,"+",pi,"i")
    return (pr,pi)

def modulo(a,b):
    p1 = ((a[0]**2) + (a[1]**2)) ** 0.5
    p2 = ((b[0]**2) + (b[1]**2)) ** 0.5

    print("El modulo de c1 es:",p1,"\nEl modulo de c2 es:",p2)
    return (p1,p2)

def cartesianas_polares(a,b):
    p1 = math.sqrt((a[0]**2) + (a[1]**2))
    Θ1 = math.atan(a[0] / a[1])
    Θ1_grados = math.degrees(Θ1)
    p2 = math.sqrt((b[0]**2) + (b[1]**2))
    Θ2 = math.atan(b[0] / b[1])
    Θ2_grados = math.degrees(Θ2)

    print(p1,"cos","(",Θ1_grados,")","+",p1,"sin","(",Θ1_grados,")","i")
    print(p2,"cos","(",Θ2_grados,")","+",p2,"sin","(",Θ2_grados,")","i")

    return (p1,Θ1_grados,Θ2_grados,p2)

def polares_cartesianas(a,b):
    r1 = a[0]*math.cos(a[1])
    i1 = a[0]*math.sin(a[1])
    r2 = b[0]*math.cos(b[1])
    i2 = b[0]*math.sin(b[1])

    print(r1,"+",i1,"i")
    print(r2,"+",i2,"i") 
    return (r1,i1,r2,i2)

def fase(a,b):
    f1 = math.atan(a[1]/a[0])
    f2 = math.atan(b[1]/b[0])

    print(f1)
    print(f2)
    return(f1,f2)



