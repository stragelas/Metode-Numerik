import numpy as np
import newton 
fx = np.poly1d([1,0,0,0,0,0,0,-1000]) #persamaan fx = x**7 - 1000 seperti contoh di slide
turunan = uts.turunan(fx,5)
print(turunan) #seharusnya bernilai 109375
x0 = 3
akar = uts.newton(fx,x0)
print(akar) #seharusnya bernilai 2.682695824849294
uts.grafik(fx,5) #klik View Desktop untuk melihat grafik
