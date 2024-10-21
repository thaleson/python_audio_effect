import numpy as np
import soundfile as sf
import librosa

# Carregar o arquivo de áudio original
audio, samplerate = sf.read("voices/voz_original.wav")

# Ajustar o pitch para criar um efeito robótico (você pode modificar n_steps)
n_steps = 7  # Alterar o valor para ajustar a altura
robot_voice = librosa.effects.pitch_shift(audio, n_steps=n_steps, sr=samplerate)

# Adicionar distorção simples (opcional)
distortion_factor = 0.4  # O fator de distorção (ajuste conforme necessário)
robot_voice = np.sign(robot_voice) * np.power(np.abs(robot_voice), distortion_factor)

# Normalizar o áudio para evitar distorção
robot_voice = robot_voice / np.max(np.abs(robot_voice))

# Salvar o resultado com efeito robótico
sf.write('voz_robotica.wav', robot_voice, samplerate)
