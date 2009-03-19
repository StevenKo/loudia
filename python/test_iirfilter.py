#!/usr/bin/env python

import ricaudio
import scipy
import scipy.signal
from common import *

plot = False

atol = 1e-4

freq = 0.2
freqStop = 0.4
fs = 8000
rp = 0.05
rs = 40

def test_filter( order, freq, freqStop, btype, ftype, rp, rs, title = ''):
    rc = ricaudio.IIRFilter( order, freq, freqStop, btype[0], ftype[0], rp, rs )
    sc_b, sc_a = scipy.signal.iirfilter(order, [freq, freqStop], btype=btype[1], analog=0, output='ba', ftype=ftype[1], rp=rp, rs=rs)
    
    rc_b = rc.b().T
    rc_a = rc.a().T
    
    print scipy.allclose(sc_b, rc_b, atol = atol) and scipy.allclose(sc_a, rc_a, atol = atol)
    
    if plot:
        plot_freqz(rc_b, rc_a, title = title)
    

ftypes = [ ( ricaudio.IIRFilter.CHEBYSHEVI, 'cheby1' ),
           ( ricaudio.IIRFilter.CHEBYSHEVII, 'cheby2' ),
           ( ricaudio.IIRFilter.BESSEL, 'bessel' ),
           ( ricaudio.IIRFilter.BUTTERWORTH, 'butter' )]

btypes = [ ( ricaudio.IIRFilter.LOWPASS, 'lowpass' ),
           ( ricaudio.IIRFilter.HIGHPASS, 'highpass' ),
           ( ricaudio.IIRFilter.BANDPASS, 'bandpass' ),
           ( ricaudio.IIRFilter.BANDSTOP, 'bandstop' ) ]

orders = [4, 5]

# All tests
for order in orders:
    for ftype in ftypes:
        for btype in btypes:
            test_filter( order, freq, freqStop, btype, ftype, rp, rs,
                         title = '%s %s filter of order %d' % (btype[1],
                                                               ftype[1],
                                                               order) )

if plot:
    import pylab
    pylab.show()
