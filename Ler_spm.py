def lerspm(filename):

    import numpy as np
    import matplotlib.pyplot as plt
    import pylab as plb
    import peakutils
    from peakutils.plot import plot as pplot
    from scipy import signal
    from scipy.optimize import curve_fit
    from scipy import asarray as ar,exp
    from scipy.integrate import quad

    from SPM import spectrum



    # def gaus(x,a,x0,sigma):
    #     return a*exp(-(x-x0)**2/(2*sigma**2))

    spectrum(filename)


    xa = np.linspace(1, 1024,1024)
    data = spectrum.data
    ya = (spectrum.data)
    #Findpeaks, define the width of the peak
    width=[20, 160]
    height=[50, 2000]
    peakind, properties = signal.find_peaks(data,height=height,width=width)
    finWidth=properties["widths"]
    # Peaks in data
    yy=[]
    for i in peakind:
        yy.append(ya[i])
    #qwprint (yy)

    #define the fit.
    a=0
    gaussx=[]
    gaussy=[]
    for i in peakind:
        xgauss=xa[int(i-finWidth[0]):int(i+finWidth[0])]
        ygauss=ya[int(i-finWidth[0]):int(i+finWidth[0])]
        gaussx.append(xgauss)
        gaussy.append(ygauss)


    # Make the fit
    x=gaussx[0]
    y=gaussy[0]

    if y ==[]:
        y=[1]
        x=[1]
    n = len(x)                      #the number of data
    mean = sum(x*y)/sum(y)  #note this correction
    sigma = np.sqrt(sum(y * (x - mean)**2) / sum(y))        #note this correction

    # Line fit


    b=ya[100];
    m=-1*(b/xa[ya.index(min(ya))])
    rect=[]
    ret=0

    for i in xa:
        ret=m*i+b
        rect.append(ret)
    #print (rect)
    def Gauss(x, a, x0, sigma, m, b):
        return a * np.exp(-(x - x0)**2 / (2 * sigma**2))+m*x+b

    popt,pcov = curve_fit(Gauss, x, y, p0=[max(y), mean, sigma, m, b])
    R=(((2.355*popt[2])/popt[1])*100)
    c=popt[1]
    FWHM=2.355*popt[2]
    peak_counts=int(popt[0])
    Gain=popt[1]

    def intpeak(x):
        return popt[0] * np.exp(-(x - popt[1])**2 / (2 * popt[2]**2))+popt[3]*x+popt[4]

    ans, err = quad(intpeak, 300, 420)

    #print (int(popt[0]))








    # for i in peakind:
    #     n = len(gaussx[a])
    #     print (n)                          #the number of data
    #     mean = sum(gaussx[a]*gaussy[a])/n
    #     print (mean)                   #note this correction
    #     sigma = sum(gaussy[a]*(gaussx[a]-mean)**2)/n
    #     print (sigma)
    #
    # popt,pcov = curve_fit(gaus,gaussx[a],gaussy[a],p0=[1,mean,sigma])
    # indexes = peakutils.indexes(y, thres=0.5, min_dist=30)
    # print (indexes)
    yLimit=peak_counts+200
    fig, ax = plt.subplots()
    ax.set_xlim(40,1024)
    ax.set_ylim(0,yLimit)
    #plt.plot(peakind, yy, "x")
    #plt.plot(gaussx[0], gaussy[0])
    #plt.plot(x,gaus(x,*popt),'ro:',label='fit')
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.plot(x, Gauss(x, *popt), 'r-', label='fit')
    ax.plot(xa,ya,'b+:',label='data')
    #plt.plot(xa,rect)
    ax.legend(('Fit', 'data'),
               shadow=True, loc=(0.01, 0.48), handlelength=1.5, fontsize=16)

    textstr = '\n'.join((
        r'$R=%.2f$' % (R, ),
        r'$centroid=%.2f$' % (c, ),
        r'$peak counts=%.2f$' % (peak_counts, ),
        #r'$Gain=%.2f$' % (Gain, ),
        r'$FWHM=%.2f$' % (FWHM, )))
    # the arrow
    Nome=str(filename)
    ax.text(0.95, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top',horizontalalignment='right', bbox=props)
    ax.set_title(Nome)
    plt.show()
