import wave

# 打开WAV文件
with wave.open('C:\\Users\\Administrator\\Music\\greeting.wav', 'rb') as wav_file:
    # 获取采样率
    sample_rate = wav_file.getframerate()
    print(f"采样率: {sample_rate} Hz")
