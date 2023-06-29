# pdfgetx3_gui
A gui for running PDFgetX3. I think it's a little easier to use than the interactive mode in PDFgetX3. Requires PDFgetX3 https://www.diffpy.org/products/pdfgetx.html, Scipy and PyQt(5) (pip or conda). Other common or standard packages required: numpy, matplotlib, os, time. The pdfgetx3_gui.py and pdffunctions.py scripts in the repository are required to run it.

To run do "python pdfgetx3_gui.py" in the terminal. Plots update on changing parameter values. Log files are made to store the current configuration so the settings are the same on rerunning the script.

Selected measurement files and background files are put into lists so they can be easily accessed again later. Press 'Plot' to run the calculation and display the selected plots (can choose any from I(Q), S(Q), F(Q), and G(r)). Pressing 'Save' will save text files containing the data of the selected plots. If the input format is '2theta', 'Save' will also return the background subtracted data as a function of 2theta with the name of \<base file name\>_bkgsub.xy. The 'Qmax together?' button moves Qmax and QmaxInst together which you may often want to do (QmaxInst is where the polynomial correction is calculated out to, and Qmax is where the Fourrier transform is integrated to).

The initial F(Q), S(Q) and G(r) plots (from when 'Plot' is last pressed) will appear in a faint grey colour.

Rebinning options were added 28/6/2023. I haven't tested it a huge amount.

![image](https://github.com/msujas/pdfgetx3_gui/assets/79653376/fc83070f-fa28-4b62-b7c0-ac6c5273f769)

![image](https://github.com/msujas/pdfgetx3_gui/assets/79653376/e573365f-f47b-46eb-9e6f-6fc639ccaf21)
