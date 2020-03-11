# Hands Off Your Face!

<img src="https://user-images.githubusercontent.com/9033365/76415349-7797ff80-63b2-11ea-867f-30a59813eb6b.png" alt="Example" width="600">

## Coronavirus (aka. COVID)
In December 2019, the world witnessed an aweful outbreak of [coronavirus disease](https://www.who.int/emergencies/diseases/novel-coronavirus-2019) in China. Not a long time later, it has been spread in more than 100 countries. No vaccine is currently available!

One underrated way of minimizing spreading the virus and protecting ourselves from it is to **avoid touching our face**.
![image](https://user-images.githubusercontent.com/9033365/76415845-67345480-63b3-11ea-9327-45bad2d3f9ed.png)

Not touching your face is harder than it sounds. In 2015, a Sydney university observed medical students on video and recorded how many times they touched their faces. Each of the 26 future doctors under observation touched their faces an average 23 times per hour.

Touching your face is at times tied to stress. This explains the excess of face touching during work as shown in [this video](https://www.facebook.com/Obeida.ElJundi/posts/10157869576021698).

Therefore, this app is developed to monitor your hand movement using any webcam and alert you (with police siren voice) once your hand gets near your face.

## DEMO

Video can be found [here](https://drive.google.com/file/d/1fe3ThyY80DQxw-qGK-85epxwJBSPxpY5/view?usp=sharing).

Hand is not close to face:
![image](https://user-images.githubusercontent.com/9033365/76417471-5afdc680-63b6-11ea-9292-7f136a830b35.png)

Hand is close to face:
![image](https://user-images.githubusercontent.com/9033365/76417565-841e5700-63b6-11ea-9918-6546a7a9d24f.png)

Video can be found [here](https://drive.google.com/file/d/1fe3ThyY80DQxw-qGK-85epxwJBSPxpY5/view?usp=sharing).

## Installation

### A) Easy (for non-technical & Windows users):
1. Download the installer from [here](https://drive.google.com/file/d/1-yvGvAZPskiqx7KB3zWO95OTYgRgNmOh/view?usp=sharing)

2. Run the installer and install the app.

3. Go to the installed folder and run **corona.exe**

4. The app will open where the first frame will be fixed and waiting for you to draw a bounding box around your hand to be tracked. Draw a bounding box and click Enter. To stop the app, press Esc.

### B) Advanced (for developers/technical users):

1. Clone or download this repository.

2. Make sure python 3.x is installed on your PC. To check if and which version is installed, run the following command:
```
python -V
```
If this results an error, this means that python isn’t installed on your PC! please download and install it from [the original website](https://www.python.org/)

3. (optional) it is recommended that you create a python virtual environment and install the necessary libraries in it to prevent versions collisions:
```
python -m venv corona
```
where corona is the environment name. Once you’ve created a virtual environment, you may activate it. Here is how to activate the environment on Windows:
```
corona\Scripts\activate.bat
```

4. Install required libraries from the provided file (**requirements.txt**):
```
pip install -r requirements.txt
```
Make sure you provide the correct path of **requirements.txt**

5. To be able to play the alert sound (police siren), add VLC folder (that contains VLC DLLs) to Windows environment path. If your python is 64-bit, make sure to use VLC 64-bit. Same for 32-bits versions of both python and VLC.

![image](https://user-images.githubusercontent.com/9033365/76417146-c6936400-63b5-11ea-8c59-a84ae80df8f1.png)

6. Run the script:
```
python corona.py
```

7. The app will open where the first frame will be fixed and waiting for you to draw a bounding box around your hand to be tracked. Draw a bounding box and click Enter. To stop the app, press Esc.
