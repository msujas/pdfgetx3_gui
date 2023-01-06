# pdfgetx3_gui
A gui for running PDFgetX3. I think it's a little easier to use than the interactive mode in PDFgetX3, but lacks some features of XPDFsuite. Requires PDFgetX3 https://www.diffpy.org/products/pdfgetx.html, and PyQt(5) (pip or conda). The pdfgetx3_gui.py and pdffunctions.py scripts in the repository are required to run it.

To run do "python pdfgetx3_gui.py" in the terminal. Plots update on changing parameter values. Log files are made to store the current configuration so the settings are the same on rerunning the script.

Changing the values in the 'relative ' boxes change the step size of the spin boxes (these values aren't stored in the config). Press 'Plot' to run the calculation and display the selected plots (can choose any of I(Q), S(Q), F(Q), and G(r)). Pressing 'Save' will save text files containing the data of the selected plots. If the input format is '2theta', 'Save' will also return the background subtracted data as a function of 2theta with the name of <base file name>_bkgsub.xy.
