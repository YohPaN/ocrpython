def tesseractFunction():
    import subprocess

    command = 'C:/Program Files/Tesseract-OCR/tesseract data/enhanced_image.jpg text'

    try:
        result = subprocess.run(command, shell=False, check=True, text=True, capture_output=True)

        stdout = result.stdout
        stderr = result.stderr

        return_code = result.returncode

    except subprocess.CalledProcessError as e:
        print("error:", e)
        print(e.stderr)