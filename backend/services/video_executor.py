import subprocess
import os

FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def trim_video(input_path: str, duration: int):
    output_path = os.path.join(OUTPUT_DIR, "trimmed.mp4")

    command = [
        FFMPEG_PATH,
        "-i", input_path,
        "-t", str(duration),
        "-y",
        output_path
    ]

    subprocess.run(
        command,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return output_path
