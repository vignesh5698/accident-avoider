# https://ourcodeworld.com/articles/read/841/#how-to-install-and-use-the-python-face-recognition-and-detection-library-in-ubuntu-16-04
#https://stackoverflow.com/questions/58354509/modulenotfounderror-no-module-named-python-jwt-raspberry-pi

Inspired by Soukupová and Čech’s 2016 paper - Real-Time Eye Blink Detection using Facial Landmarks.

## Salient Features:
1) Real time drowsiness detection is implemented on light weight
processing unit (raspberry pi).
2) The system is able to capture real time images using miniature
camera (say webcam, raspberry camera) installed at dashboard
of a car.
3) Fast and accurate face detection and eye detection algorithm is
performed on real time captured images.
4) Proposed algorithm is able to detect drowsiness in both
constrained and unconstrained background.
5) Scale invariant detection is possible.
6) The system can detect drowsiness in noisy environment.
7) Entire Computational time is very less.
8) Prior communication is established with family members via
email, SMS etc.

## Proposed Methodology:
### Step 1: Real time image capture
Real time images are captured using raspberry pi camera with size of
640x480x3px(RGB).
### Step 2: Eye detection from facial landmark indexes
The facial landmark detector produces 68 (x, y)-coordinates that map
to specific facial structures. These 68 point mappings were obtained
by training a shape predictor on the labelled iBUG 300-W dataset.

![Facial Landmarks](https://pyblog.xyz/wp-content/uploads/2018/03/facial_landmarks_68markup-300x242.jpg)

Therefore, to extract the eye regions from a set of facial
landmarks, we simply need to know the correct array slice
indexes. Using those indexes, we are able to extract the eye
regions via an array slice.

The download link for the facial landamark indexes is given here - 
https://drive.google.com/open?id=11AK6QzVa4Xu5JsfKgJ7lrQF7L3C3ug-9

### Step 3: Eye Blink detection Algorithm
![Drowsiness Detection](https://www.pyimagesearch.com/wp-content/uploads/2017/04/blink_detection_plot.jpg)

For every video frame, the eye landmarks are detected. The eye aspect ratio (EAR) between height
and width of the eye is computed.

![alt text](https://latex.codecogs.com/gif.latex?EAR%20%3D%20%5Cfrac%7B%7C%7Cp_2-p_6%7C%7C&plus;%7C%7Cp_3-p_5%7C%7C%7D%7B%7C%7Cp_1-p_4%7C%7C%7D)

Here we've the graph of EAR w.r.t time. As we can see, the Eye Aspect Ratio is constant (indicating the eye is open), then rapidly drops to zero, then increases again, indicating a blink has taken place.

In our drowsiness detector case, we’ll be monitoring the Eye Aspect Ratio to see if the value falls but does not increase again, thus implying that the person has closed his eyes.

