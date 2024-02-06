# pdfgetx3_gui
A gui for running PDFgetX3. I think it's a little easier to use than the interactive mode in PDFgetX3. Requires PDFgetX3 https://www.diffpy.org/products/pdfgetx.html, Scipy and PyQt(5) (pip or conda). Other common or standard packages required: numpy, matplotlib. The pdfgetx3_gui.py and pdffunctions.py scripts in the repository are required to run it.

On cloning or downloading the repository, try running 'pip install -e .' in the directory. This should make an executable in the python Scripts folder which can be run from the command line as 'pdfgetx3gui' from any directory. If this doesn't work do "python pdfgetx3_gui.py" in the terminal. Plots update on changing parameter values. Log files are made to store the current configuration so the settings are the same on rerunning the script.

Selected measurement files and background files are put into lists so they can be easily accessed again later. Press 'Plot' to run the calculation and display the selected plots (can choose any from I(Q), S(Q), F(Q), and G(r)). Pressing 'Save' will save text files containing the data of the selected plots. If the input format is '2theta', 'Save' will also return the background subtracted data as a function of 2theta with the name of \<base file name\>_bkgsub.xy.

There's a rebinning option to reduce high Q noise. It's not so efficient, so could probably be faster.


![image](https://github.com/msujas/pdfgetx3_gui/assets/79653376/8a05433b-7cd8-46ea-932f-9479fd88f5b6)

![image](https://github.com/msujas/pdfgetx3_gui/assets/79653376/e573365f-f47b-46eb-9e6f-6fc639ccaf21)
