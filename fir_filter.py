from scipy.io import wavfile
import numpy as np

#Input file has to be wav S/R: 11025Hz Mono 32-bit float
samplerate, data = wavfile.read('input.wav')
output = []
buffer = [0.00]*27
#Coefficients for Lowpass FIR filter with a hamming window, Fs = 11025, Fc = 3kHz
coeffs = [-0.00045581941038631439,0.0024627943741524234,-0.00016390987220157261,-0.0061204138832738611,0.0031028980901724804,0.013427277520441797,-0.012400155886939277,-0.023362277517784979,0.034358502598093706,0.03360407700678994,-0.085714933209765462,-0.041310928398418836,0.31072804593505071,0.54368968530813855,0.31072804593505071,-0.041310928398418836,-0.085714933209765462,0.03360407700678994,0.034358502598093706,-0.023362277517784979,-0.012400155886939277,0.013427277520441797,0.0031028980901724804,-0.0061204138832738611,-0.00016390987220157261,0.0024627943741524234,-0.00045581941038631439]
coeffs_linearphase = coeffs[0:14]

for sample in data:
    buffer.pop(0)
    buffer.append(sample)
    out_sample = 0

    for i in range(len(coeffs_linearphase)):
        coef = coeffs_linearphase[i]
        if i == 13 :
            out_sample += coef*buffer[13]
        else:
            out_sample += (buffer[i]+buffer[26-i])*coef

    output.append(np.float32(out_sample))

wavfile.write("output.wav",11025,np.array(output))
