def tesseractFunction():
    import subprocess

    command = 'C:/Program Files/Tesseract-OCR/tesseract data/input_image.jpg text'

    try:
        subprocess.run(command, shell=False, check=True, text=True, capture_output=True)

    except subprocess.CalledProcessError as e:
        print("error:", e)
        print(e.stderr)