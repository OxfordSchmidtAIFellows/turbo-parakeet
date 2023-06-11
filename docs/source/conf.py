# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'turbo-parakeet'
copyright = '2023, Elnaz Azizi, Richard Creswell, Holly Pacey, Rachel Parkinson'
author = 'Elnaz Azizi, Richard Creswell, Holly Pacey, Rachel Parkinson'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc','sphinx.ext.viewcode','sphinx.ext.napoleon','sphinx.ext.coverage']

templates_path = ['_templates']
exclude_patterns = []

# Configuration of sphinx.ext.coverage
coverage_show_missing_items = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

#sys.path.insert(0, os.path.dirname(os.getcwd()))
import sys,os
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(1, os.path.abspath('../../Data'))
sys.path.insert(2, os.path.abspath('../../pytimeops'))

#import pathlib
#import sys
#sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
