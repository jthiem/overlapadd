# overlapadd
Overlap-Add filter in Python (using numpy)

This small function implements a (real-valued) FFT-based
overlap-add linear finite impulse response filter.  It should
behave similarly to scipy.signal.lfilter, but is generally
much faster.  See the Jupyter notebook for a timing test
on an ancient (Core2Duo) Mac Mini (using Anaconda Python 3.5).

The reason this is much faster is that while both lfilter and
my olafilter are O(N) with respect to x (the signal being 
filterd), lfilter is (I think) O(N^2) w.r.t. the filter (b).
Overlap-add is O(N log N).

Finally it's also generally faster than scipy.signal.fftconvolve,
which os O(N log N) of _the maximum_ of the signal and the
filter since it converts both into frequency domain, with the
FFT size given by the larger of the two - this only works well
if both x and b are of similar size.
