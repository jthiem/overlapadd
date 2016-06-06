#
# Overlap-add FIR filter, (c) Joachim Thiemann 2016
#
import numpy as np

def olafilt(b, x):
    L_I = b.shape[0]
    # Find power of 2 larger that 2*L_I (from abarnert on Stackoverflow)
    L_F = 2<<(L_I-1).bit_length()  
    L_S = L_F - L_I + 1
    L_sig = x.shape[0]
    offsets = range(0, L_sig, L_S)
    FDir = np.fft.rfft(b, n=L_F)
    tempresult = [np.fft.irfft(np.fft.rfft(x[n:n+L_S], n=L_F)*FDir) for n in offsets]
    res = np.zeros(L_sig+L_F)
    for i, n in enumerate(offsets):
        res[n:n+L_F] += tempresult[i]
    return res[:L_sig]
