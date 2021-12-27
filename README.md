If you are like me and have developed poor posture habits over the years, you may be seeking ways to correct them. For that purpose, I have written a short CircuitPython script using the VS Code CircuitPython extension inspired by Adafruit Carter Nelson's slouch detector to help prevent others from developing similar injuries.

The Circuit Playground Express (CPX) is a micro-controller, with several embedded sensors including an integrated accelerometer which I used in this case to calculate the angle of inclination of the arm/wrist. The microcontroller is programmed to beep once the threshold has been triggered and will stop once the posture has been corrected.

The angle can be adjusted based on the user's application. The script is portable to any microcontroller supporting circuitpython (see list here ) and is simple enough to easily be converted to lower level languages.

I have left a link to the github repository in the comment section with detailed instructions on how to set it up along with the required hardware and equipment for anyone to use and repurpose.

I hope many of you find this useful and look forward to hearing about your experience with your own version.


![](images/Picture1.png)
![](images/Picture2.png)
![](images/Picture3.png)

# Hardware
Circuit Playground Express or (Circuit Playground BlueFruit)
Power Source (Repurposed phone or AAA Battery Holder JST-PH)
Armband
Micro USB cable + Micro USB  to Female Adapter
or USB C cable + USB C to Female Adapter
![](images/20211226_161809.jpg)



