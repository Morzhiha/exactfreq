from scipy import fft, arange
import numpy as np
from scipy.io import wavfile
import os

here_path = os.path.dirname(os.path.realpath(__file__))
wav_file_name = 'mix_09s.wav'
wave_file_path = os.path.join(here_path, wav_file_name)
sr, signal = wavfile.read(wave_file_path)


y = signal[::1]  
t = np.arange(len(y)) / float(sr)

def frequency_spectrum(x, sf):
    """
    вычисляем частотный спектр сигнала из временной области
    параметр x: сигнал во временной области
    параметр sf: sampling frequency - частота дискретизации
    возврашает частоты и их распределение
    """
    x = x - np.average(x)  

    n = len(x)
    
    k = arange(n)
    tarr = n / float(sf)
    frqarr = k / float(tarr)  

    frqarr = frqarr[range(n // 2)] 

    x = fft(x) / n  
    x = x[range(n // 2)]

    return frqarr, abs(x)

def init():

    frq, X = frequency_spectrum(y, sr)

    print('Частотные пики ')
    for i in range(len(frq)):
        if X[i] > 20:
            print(frq[i])
            
    
init()
