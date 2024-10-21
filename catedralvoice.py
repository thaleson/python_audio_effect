import numpy as np
import scipy.signal
import soundfile as sf

# Carregar o arquivo de áudio
audio, samplerate = sf.read("voices/voz_original.wav")

# Simular um impulso de reverberação (isso simula o ambiente da catedral)
# para um resultado mais realista.
impulse_response = np.zeros(10000)  # Vetor de zeros
impulse_response[::500] = 1  # Padrão de impulso para eco

# Aplicar a convolução para adicionar o efeito de reverberação
reverb_audio = scipy.signal.convolve(audio, impulse_response, mode='full')

# Normalizar o áudio para evitar distorção
reverb_audio = reverb_audio / np.max(np.abs(reverb_audio))

# Salvar o resultado com efeito de catedral
sf.write('catedral.wav', reverb_audio, samplerate)
