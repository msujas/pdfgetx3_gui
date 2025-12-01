# pdfgetx3_gui
A gui for running PDFgetX3. I think it's a little easier to use than the interactive mode in PDFgetX3. Requires PDFgetX3 https://www.diffpy.org/products/pdfgetx.html, Scipy and PyQt(5) (pip or conda). Other common or standard packages required: numpy, matplotlib.

To install, either clone this repository and run ```pip install -e .``` (-e optional to make it editable), or from PyPi with ```pip install pdfgetx3gui```. This creates a python package with an exe file called pdfgetx3gui in the python 'Scripts' folder, then it can be run with ```pdfgetx3gui``` in the terminal (if Scripts is in your PATH). 

Plots update on changing parameter values. Log files are made to store the current configuration so the settings are the same on rerunning the script.

Selected measurement files and background files are put into lists so they can be easily accessed again later. Press 'Plot' to run the calculation and display the selected plots (can choose any from I(Q), S(Q), F(Q), and G(r)). Pressing 'Save' will save text files containing the data of the selected plots. If the input format is '2theta', 'Save' will also return the background subtracted data as a function of 2theta with the name of \<base file name\>_bkgsub.xy.

There's a rebinning option to reduce high Q noise. It's not so efficient, so could probably be faster.


<img width="695" height="579" alt="image" src="https://github.com/user-attachments/assets/b9d37adb-e36a-48c2-a1e0-2008cccae4a1" />

![image](https://github.com/user-attachments/assets/4a24f026-434b-45b5-a108-6493cbdf323c)

