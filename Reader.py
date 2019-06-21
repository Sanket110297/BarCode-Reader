from pyzbar import pyzbar
import argparse
import cv2

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True)

    args = vars(ap.parse_args())

    # load the input image
    image = cv2.imread(args["image"])
    
    print('Original Dimensions : ',image.shape)
 
    # scale_percent = 60 # percent of original size
    # width = int(image.shape[1] * scale_percent / 100)
    # height = int(image.shape[0] * scale_percent / 100)
    # dim = (width, height)
    # # resize image
    # resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    
    # print('Resized Dimensions : ',resized.shape)
    
    # cv2.imshow("Resized image", resized)
    # find the barcodes in the image and decode each of the barcodes
    barcodes = pyzbar.decode(image)

    print(barcodes)

    for barcode in barcodes:
            # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
    
        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 255), 2)
    
        # print the barcode type and data to the terminal
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

main()
