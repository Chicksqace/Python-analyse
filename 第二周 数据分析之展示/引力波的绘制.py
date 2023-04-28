import wave
import numpy as np
import matplotlib.pyplot as plt

with wave.open("H1_Strain.wav", 'rb') as h_wave:
    rate_h = h_wave.getframerate()
    h_frames = h_wave.getnframes()
    h_strain = np.frombuffer(h_wave.readframes(h_frames), dtype=np.int16)

with wave.open("L1_Strain.wav", 'rb') as l_wave:
    rate_l = l_wave.getframerate()
    l_frames = l_wave.getnframes()
    l_strain = np.frombuffer(l_wave.readframes(l_frames), dtype=np.int16)

reftime, ref_H1 = np.genfromtxt('wf_template.txt').transpose()

htime_interval = 1/rate_h
ltime_interval = 1/rate_l
fig = plt.figure(figsize=(12, 6))

htime_len = len(h_strain)/rate_h
htime = np.arange(-htime_len/2, htime_len/2, htime_interval)
plth = fig.add_subplot(221)
plth.plot(htime, h_strain, 'y')
plth.set_xlabel('Time (seconds)')
plth.set_ylabel('H1 Strain')
plth.set_title('H1 Strain')

ltime_len = len(l_strain)/rate_l
ltime = np.arange(-ltime_len/2, ltime_len/2, ltime_interval)
pltl = fig.add_subplot(222)
pltl.plot(ltime, l_strain, 'g')
pltl.set_xlabel('Time (seconds)')
pltl.set_ylabel('L1 Strain')
pltl.set_title('L1 Strain')

pltref = fig.add_subplot(212)
pltref.plot(reftime, ref_H1)
pltref.set_xlabel('Time (seconds)')
pltref.set_ylabel('Template Strain')
pltref.set_title('Template')
fig.tight_layout()

plt.savefig("Gravitational_Waves_Original.png")
plt.show()
plt.close(fig)