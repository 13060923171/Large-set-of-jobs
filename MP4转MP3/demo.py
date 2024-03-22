import os
from moviepy.editor import AudioFileClip

source_dir = './音乐'
output_dir = './ConvertedSoundFiles'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

def convert_to_mp3(file_path, output_path):
    audio = AudioFileClip(file_path)
    audio.write_audiofile(output_path)
    print(f"Converted {file_path} to {output_path}")

for filename in os.listdir(source_dir):
    if filename.endswith('.mp4'):
        file_path = os.path.join(source_dir, filename)
        output_filename = os.path.splitext(filename)[0] + '.mp3'
        output_path = os.path.join(output_dir, output_filename)
        try:
            convert_to_mp3(file_path, output_path)
        except Exception as e:
            print(f"Can't convert file {filename} due to {str(e)}")

print("All mp4 files converted to mp3 successfully!")