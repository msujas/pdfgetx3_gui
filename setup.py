"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="pdfgetx3gui",  # Required

    version="1.0",  # Required

    description="a GUI for running PDFgetX3",  # Optional
    scripts=['pdfgetx3_gui.py'],
    package_dir={ 'pdfgetx3gui':'.','pdfgetx3gui.icon':'icon','pdfgetx3gui.exampleFiles':'exampleFiles'},
    entry_points = {'console_scripts': ['pdfgetx3gui = pdfgetx3gui.pdfgetx3_gui:main',]},
    package_data={'icon':['icon/icon.png',],'exampleFiles':['exampleFiles/*',]},
    include_package_data=True,
    #url="https://github.com/pypa/sampleproject",  # Optional
    author="Kenneth P. Marshall",  # Optional
    # This should be a valid email address corresponding to the author listed
    # above.
    author_email="kenneth.marshall@esrf.fr",  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    py_modules= ['pdffunctions','pdfgetx3_gui'],
    packages=   ['pdfgetx3gui.icon','pdfgetx3gui.exampleFiles','pdfgetx3gui'],  # Required
    install_requires = ['PyQt5','numpy','scipy','matplotlib'],
    python_requires=">=3.7, <3.10", #I believe these are the requirements for diffpy.pdfgetx
)
