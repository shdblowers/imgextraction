import sys
import argparse
import cv2 as cv


def extractImages(pathIn, pathOut, skipSecs):

    capture = cv.VideoCapture(pathIn)
    if not capture.isOpened():
        print('Unable to open video: ' + pathIn)
        exit(0)

    print('Video frame rate: ', capture.get(cv.CAP_PROP_FPS))
    print('Frames in video: ', capture.get(cv.CAP_PROP_FRAME_COUNT))
    print('Length of video (secs): ', (capture.get(
        cv.CAP_PROP_FRAME_COUNT) / capture.get(cv.CAP_PROP_FPS)))

    count = 0
    capture.set(cv.CAP_PROP_POS_MSEC, (skipSecs * 1000))
    while True:
        success, image = capture.read()

        if image is None:
            break

        sys.stdout.write(".")
        sys.stdout.flush()

        cv.imwrite(pathOut + "/frame%d.png" % count, image)
        count = count + 1

    print("\nDone!")


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    a.add_argument("--skipSecs", help="skip capture start in secs")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut, int(args.skipSecs))
