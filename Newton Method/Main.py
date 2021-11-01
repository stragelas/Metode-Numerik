import numpy as np 

def turunan(fx,x):
    q = fx.deriv()
    return q

def newton(fx,x0):
    x1 = x0
    temp = 0
    while True:
        temp = x1
        turunan_fx = turunan(fx,temp)
        fx_sekarang = fx(temp)
        # rumus newton
        x1 = np.subtract(temp, np.divide(fx_sekarang, turunan_fx))
        if abs(x1 - temp) <= 0.00001:
            break
    return x1

def grafik(fx,x0):
    import matplotlib.pyplot as plt #jangan dihapus
    # Gunakan nilai x dari rentang (akar-10) sampai dengan (akar+10)
    batas_bawah = newton(fx,x0)-10
    batas_atas = newton(fx,x0)+10
    x = np.arange(batas_bawah, batas_atas)
    plt.plot(x, fx(x), 'blue')
    dot = newton(fx,x0)
    plt.plot(dot, 'ro')
    plt.show()
