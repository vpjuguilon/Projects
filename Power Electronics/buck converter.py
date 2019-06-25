from numpy.fft import rfft, irfft
from matplotlib.pyplot import plot, show
from numpy import linspace, array

time = linspace(0,1000,10000)


def squarewave(vs, vg, duty, frequency, timeArray):
    period = 1000/frequency          # period in ms
    on = duty*period
    vout = []
    for t in timeArray:
        if (t % period) < on:
            vout.append(vs)
        else:
            vout.append(vg)
    return array(vout)


waveform1 = squarewave(10, 0, 0.4, 5, time)     # Create square wave (switching)
plot(time, waveform1)
transform = rfft(waveform1)

n = len(waveform1)//2 + 1
for i in range(5, n):              # Lowpass filter
    transform[i] = 0
waveform2 = irfft(transform)
plot(time, waveform2)
show()

