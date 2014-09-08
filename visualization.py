import numpy
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import sys
import math

def smooth(x,window_len=11,window='hanning'):
        if x.ndim != 1:
                raise ValueError, "smooth only accepts 1 dimension arrays."
        if x.size < window_len:
                raise ValueError, "Input vector needs to be bigger than window size."
        if window_len<3:
                return x
        if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
                raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"
        s=numpy.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]
        if window == 'flat': #moving average
                w=numpy.ones(window_len,'d')
        else:  
                w=eval('numpy.'+window+'(window_len)')
        y=numpy.convolve(w/w.sum(),s,mode='same')
        return y[window_len:-window_len+1]

in_x = []
in_y = []
in_z = []
l2_z = []
in_heading = []
for line in sys.stdin:
	[prefix, rssi, heading] = line.strip().split('\t')
	in_heading.append(float(heading))
	in_x.append( 0.9 * math.sin(float(heading) / 180 * 3.14) )
	in_y.append( 0.9 * math.cos(float(heading) / 180 * 3.14) )
	in_z.append( int(rssi) ); 
	
smoothed = smooth(numpy.array(in_z),window_len= 100)
np_heading = numpy.array(in_heading)
for i in range(len(heading)):
	curHeading 	= heading[i]
	curRssi 	= smoothed[i]
	
	
# 
# x,y=np.mgrid[-2:2:20j,-2:2:20j]  
# z=x*np.exp(-x**2-y**2)
# 
# print x
# print y
# print z
# 
ax=plt.subplot(111,projection='3d')
ax.plot(in_x, in_y, smoothed, color = 'r')
# ax.scatter(x, y, z, zdir='z', c= 'red', marker = "^")
# ax.bar(x, y, z, zdir='z', color='red', alpha=0.8)


# ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()