# pdfgetx3_gui
Update: Jan. 2026 - PDFgetX3 2.4.0 has been released, which is compatible with Python 3.11 - 3.13. The GUI works the same for the new version, but now you don't have to create a new environment for an older version of Python. The new version has some options which are not yet available in the GUI. Lorch function has been implemented, multiple backgrounds not yet.

A gui for running PDFgetX3. I think it's a little easier to use than the interactive mode in PDFgetX3. Requires PDFgetX3 https://www.diffpy.org/products/pdfgetx.html, other dependencies (SciPy, numpy, matplotlib, PyQt5) will be installed through the installation (if not already installed). Recommended Python 3.10 (or later if you're using PDFgetX3 2.4+), and pip as your package manager, as this is the most recent version supported by PDFgetX3.

To install, either clone this repository and run ```pip install -e .``` (-e optional to make it editable), or from PyPi with ```pip install pdfgetx3gui```. This creates a python package with an exe file called pdfgetx3gui in the python 'Scripts' folder, then it can be run with ```pdfgetx3gui``` in the terminal (if Scripts is in your PATH). 

Plots update on changing parameter values. Log files are made to store the current configuration so the settings are the same on rerunning the script.

Selected measurement files and background files are put into lists so they can be easily accessed again later. Press 'Plot' to run the calculation and display the selected plots (can choose any from I(Q), S(Q), F(Q), and G(r)). Pressing 'Save' will save text files containing the data of the selected plots. If the input format is '2theta', 'Save' will also return the background subtracted data as a function of 2theta with the name of \<base file name\>_bkgsub.xy.

There's a rebinning option to reduce high Q noise. It's not so efficient, so could probably be faster.


<img width="695" height="579" alt="image" src="https://github.com/user-attachments/assets/b9d37adb-e36a-48c2-a1e0-2008cccae4a1" />

![image](https://github.com/user-attachments/assets/4a24f026-434b-45b5-a108-6493cbdf323c)

## Troubleshooting:

If there's issues with package conflicts, or Qt bugs, probably easiest to try a new Python 3.10 environment (or 3.13 if using the new PDFgetX3). Recommend using pip as your package manager (not conda's built in one). In conda e.g.
```
conda create -n pgx python==3.10
```
Install pdfgetx3 - if you don't have: get license, download from Columbia Technology Ventures https://inventions.techventures.columbia.edu/licenses/pdfgetx3-n3-s3-free-academic--113
```
pip install <diffpy pdfgetx3 filename>.whl
```
clone this repository, navigate to it and install
```
cd <path>/pdfgetx3_gui/
pip install -e .
```
Or from PyPi
```
pip install pdfgetx3gui
```
This will install other dependencies as well.
