def preprod():
    import cv2

    def enhance_contrast(input_image_path, output_image_path):
        image = cv2.imread(input_image_path)
        enhanced_image = cv2.convertScaleAbs(image, alpha=3, beta=50)

        cv2.imwrite(output_image_path, enhanced_image)

    input_image_path = 'data/input_image.jpg'
    output_image_path = 'data/enhanced_image.jpg'
    enhance_contrast(input_image_path, output_image_path)
