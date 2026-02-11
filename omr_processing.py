import cv2
import pytesseract

def process_omr(filepath):

    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    reg_no = ""
    for line in text.split("\n"):
        if "Register" in line:
            reg_no = line.split(":")[-1].strip()

    # Dummy K-level values (You can improve bubble detection)
    k_values = {
        "K1": 2,
        "K2": 3,
        "K3": 1,
        "K4": 4,
        "K5": 2
    }

    return {
        "Register Number": reg_no,
        "K1": k_values["K1"],
        "K2": k_values["K2"],
        "K3": k_values["K3"],
        "K4": k_values["K4"],
        "K5": k_values["K5"]
    }
