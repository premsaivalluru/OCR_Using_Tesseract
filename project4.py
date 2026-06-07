import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Increase contrast
    gray = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)

    # Noise removal (better than blur)
    gray = cv2.medianBlur(gray, 3)

    # Otsu threshold (better for OCR than adaptive in many cases)
    _, thresh = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return image, thresh


def extract_text(processed_image):

    config = r'--oem 3 --psm 6'

    text = pytesseract.image_to_string(processed_image, config=config)

    return text


def detect_text_boxes(original_image):

    data = pytesseract.image_to_data(
        original_image,
        output_type=pytesseract.Output.DICT
    )

    n_boxes = len(data['text'])

    for i in range(n_boxes):

        try:
            confidence = float(data['conf'][i])
        except:
            confidence = 0

        if confidence > 50:

            x = data['left'][i]
            y = data['top'][i]
            w = data['width'][i]
            h = data['height'][i]

            cv2.rectangle(
                original_image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    return original_image


def save_text(text):

    with open("recognized_text.txt", "w", encoding="utf-8") as file:
        file.write(text)


def main():
    image_path = input("Enter image path: ")
    
    original, processed = preprocess_image(image_path)

    text = extract_text(processed)

    print("\n===== EXTRACTED TEXT =====\n")
    print(text)

    save_text(text)

    boxed_image = detect_text_boxes(original)

    cv2.imshow("Detected Text", boxed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()