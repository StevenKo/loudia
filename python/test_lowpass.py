#!/usr/bin/env python

import ricaudio
import scipy
import scipy.signal
from common import *

plot = False

atol = 1e-5

freq = 0.3
fs = 8000

# Test type I with even order
rp = 0.05
order = 4

rc = ricaudio.LowPass( order, freq, rp, ricaudio.CHEBYSHEVI )
sc_b, sc_a = scipy.signal.cheby1(order, rp, freq, btype='low', analog=0, output='ba')

rc_b = rc.b().T
rc_a = rc.a().T

print scipy.allclose(sc_b, rc_b, atol = atol) and scipy.allclose(sc_a, rc_a, atol = atol)

if plot:
    plotFreqz(rc_b, rc_a, title = 'LowPass 1 order %d' % order)

# Test with type I with odd order
order = 11

rc = ricaudio.LowPass( order, freq, rp, ricaudio.CHEBYSHEVI )
sc_b, sc_a = scipy.signal.cheby1( order, rp, freq, btype='low', analog=0, output='ba' )

rc_b = rc.b().T
rc_a = rc.a().T

print scipy.allclose(sc_b, rc_b, atol = atol) and scipy.allclose(sc_a, rc_a, atol = atol)

if plot:
    plotFreqz(rc_b, rc_a, title = 'LowPass 1 order %d' % order)


# Test type II with even order
rp = 40
order = 4

rc = ricaudio.LowPass( order, freq, rp, ricaudio.CHEBYSHEVII )
sc_b, sc_a = scipy.signal.cheby2(order, rp, freq, btype='low', analog=0, output='ba')

rc_b = rc.b().T
rc_a = rc.a().T

print scipy.allclose(sc_b, rc_b, atol = atol) and scipy.allclose(sc_a, rc_a, atol = atol)

if plot:
    plotFreqz(rc_b, rc_a, title = 'LowPass 2 order %d' % order)


# Test with type II with odd order
order = 11

rc = ricaudio.LowPass( order, freq, rp, ricaudio.CHEBYSHEVII )
sc_b, sc_a = scipy.signal.cheby2(order, rp, freq, btype='low', analog=0, output='ba')

rc_b = rc.b().T
rc_a = rc.a().T

print scipy.allclose(sc_b, rc_b, atol = atol) and scipy.allclose(sc_a, rc_a, atol = atol)

if plot:
    plotFreqz(rc_b, rc_a, title = 'LowPass 2 order %d' % order)

if plot:
    import pylab
    pylab.show()
