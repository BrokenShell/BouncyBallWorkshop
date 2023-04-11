import os

from PIL import Image
from moviepy.editor import ImageSequenceClip

from app.bounce import bouncy


def make_frames(foreground: str, background: str, output_path: str):
    ball = Image.open(foreground)
    scene = Image.open(background)
    positions = bouncy(height=200, cor=0.75, total_frames=60)
    for i, (x, y) in enumerate(positions):
        bg = scene.copy()
        pos = (150 + round(x), 512 - round(y) - 130)
        bg.paste(ball, pos, ball)
        bg.save(os.path.join(output_path, f"{i:0>2}.png"))


def make_movie(input_path: str, output_path: str):
    frames = sorted(
        os.path.join(input_path, img)
        for img in os.listdir(input_path)
        if img.endswith(".png")
    )
    sequence = ImageSequenceClip(frames, fps=24)
    sequence.write_videofile(
        output_path,
        fps=24,
        remove_temp=True,
        codec="mpeg4",
    )


if __name__ == '__main__':
    make_frames(
        os.path.join("app", "images", "ball.png"),
        os.path.join("app", "images", "bg.png"),
        os.path.join("app", "frames")
    )
    make_movie(
        input_path=os.path.join("app", "frames"),
        output_path=os.path.join("app", "video", "bounce-ball.mp4")
    )
