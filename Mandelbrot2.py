import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    In deze functie wordt de Mandelbrot formule uitgerekend.
    param: c (complex) het complexe getal waarvoor je de formule uitrekent.
    param: max_iter (integer) het maximale aantal dat je de formule mag uitrekenen
        om uit te proberen of de mandelbrot formule begrenst is voor dat complexe getal (= 80).
    :return: (integer) een getal tussen 0 en max_iter (= 80).
    """
    z = complex(0, 0)
    for n in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return n
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
    """
    In deze functie wordt de Mandelbrotset gemaakt.
    param: xmin (float) de laagste waarde van de x-as (= -2.0).
    param: xmax (float) de hoogste waarde van de x-as (= o.5).
    param: ymin (float) de laagste waarde van de y-as (= -1.25).
    param: ymax (float) de hoogste waarde van de y-as (= 1.25).
    param: width (integer) het aantal punten van de x-as (= 1000).
    param: height (integer) het aantal punten van de y-as (= 1000).
    param: maxiter (integer) het maximale aantal dat je de formule mag uitrekenen
        om uit te proberen of de mandelbrot formule begrenst is voor dat complexe getal (= 80).
    :return: (tuple) het x-as-object en het y-as-object gevolgd door een lijst met alle punten van het rooster.
    """
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    lijst = []
    for r in r1:
        for i in r2:
            lijst.append(mandelbrot(complex(r, i), maxiter))                     
    return (r1, r2, lijst)


def plot(m_set):
    """
    Deze functie zet de Mandelbrotset om in een grafische weergave.
    param: m_set (tuple) het x-as-object en het y-as-object gevolgd door een lijst met alle punten van het rooster.
    :return: None. Maar er verschijnt wel een venster met een plaatje.
    """
    r1,r2,lst = m_set
    print r1
    realAxisLen = len(r1)
    imaginaryAxisLen = len(r2)
    
    # een 2 Dimensionaal array dat een Mandelbrotset representeert.
    rooster = np.empty((realAxisLen, imaginaryAxisLen))

    for x in xrange(realAxisLen):
        for y in xrange(imaginaryAxisLen):
            rooster[x, y] = lst[x * realAxisLen + y]

    plt.imshow(rooster.T, interpolation="nearest")
    plt.show()

# Hier wordt de grafische weergave van de Mandelbrotset gemaakt. Dit is het startpunt van het programma.                            
plot(mandelbrot_set(-2.0, 0.5, -1.25, 1.25, 1000, 1000, 80))
