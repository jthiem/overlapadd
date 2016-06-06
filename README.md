# overlapadd
Overlap-Add filter in Python (using numpy)

This small function implements a (real-valued) FFT-based
overlap-add linear finite impulse response filter.  It should
behave similarly to scipy.signal.lfilter, but is generally
much faster.  See the Jupyter notebook for a timing test
on an ancient (Core2Duo) Mac Mini (using Anaconda Python 3.5).
It's also generally faster than scipy.signal.fftconvolve.

See https://en.wikipedia.org/wiki/Overlap%E2%80%93add_method
for a good explanation of Overlap-add compared to standard
convolution.

## TODO

- Add ability to set and save state (trivial)
- Allow for complex signals (also trivial, should be separate function)
