# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Import Sphinx theme
import sphinx_rtd_theme
#import sphinx_bootstrap_theme
#import sphinx_material
#import sphinx_pdj_theme


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Calculator Application'
copyright = '2024, Ashish Kumar (ashish.bmistry@gmail.com)'
author = 'Ashish Kumar (ashish.bmistry@gmail.com)'
version = '1.0'
release = '1.0.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# -- Extension configuration -------------------------------------------------
# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = [
    'sphinx.ext.autodoc',       # Additing extension for auto docoumentation.
    # Add more extensions as needed
    'sphinx.ext.napoleon',      # Enable Napoleon extension for Google-style docstrings
    'sphinx_rtd_theme',         # Use ReadTheDocs theme
    #'sphinx_bootstrap_theme',  # Use Bootstrap theme
    #'sphinx_material',         # Use Material theme
    #'sphinx_pdj_theme',        # Use PDJ theme
    'sphinx.ext.todo',
    'sphinx.ext.viewcode'
]

# Napoleon settings
napoleon_google_docstring = True  # Parse Google-style docstrings

# Customer sections style settings
napoleon_custom_sections = [('Classes', 'params_style'), ('Imports', 'params_style'), ('Author', 'params_style')]

# Add type hints to the documentation
autodoc_typehints = 'description'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory, add these directories to sys.path here.
# If the directory is relative to the documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('..\\..\\'))


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of builtin themes.

# Use Alabaster theme
#html_theme = 'alabaster'

# Use ReadTheDocs theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Use Bootstrap theme
#html_theme = 'bootstrap'

# Bootstrap theme options
#html_theme_options = {
#    'bootswatch_theme': "flatly",
#    'navbar_sidebarrel': False,
#    'bootstrap_version': "3",
#}

# Use Material theme
#html_theme = 'sphinx_material'

# Material theme options
#html_theme_options = {
#    'nav_title': 'Calculator Documentation',
#    'google_analytics_account': 'YOUR_GOOGLE_ANALYTICS_ACCOUNT_ID',            #use appropriate value.
#    'color_primary': 'blue',
#    'color_accent': 'light-blue',
#    'repo_url': 'https://github.com/yourusername/yourproject',                 #use appropriate value.
#    'repo_name': 'YourProject',                                                #use appropriate value.
#    'html_minify': True,
#    'css_minify': True,
#    'version_dropdown': False, 
#}

# Use PDJ theme
#html_theme = 'sphinx_pdj_theme'

# PDJ theme options
#html_theme_options = {
#    'style': 'green',
#    'collapse_navigation': False,
#    'sticky_navigation': True,
#    'navigation_depth': 3,
#}

# The name of an image file (relative to this directory) to place at the top of the sidebar.
html_logo = '_static/calc_fevicon.png'

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory.
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'Calculator Application'


# -- Options for LaTeX output ------------------------------------------------

#latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': r'''
    #    \usepackage{amsmath,amsfonts,amssymb,amsthm}
    #    \usepackage{graphicx}
    #''',

    # Latex figure (float) alignment
    #'figure_align': 'htbp',
#}

# List of LaTeX packages to include.
#latex_additional_files = ['_static/your_customizations.sty']

# The name of an image file (relative to this directory) to place at the top of the title page.
#latex_logo = '_static/calc_fevicon.png'


# These options are specifically for configuring the generation of manual pages (in the form of man pages) and Texinfo documents.
# -- Options for manual page output ------------------------------------------

#man_pages = [
#    ('index', 'yourprojectname', 'Your Project Name Documentation',
#     [author], 1)
#]

# -- Options for Texinfo output ----------------------------------------------

#texinfo_documents = [
#    ('index', 'YourProjectName', 'Your Project Name Documentation',
#     author, 'YourProjectName', 'One line description of project.',
#     'Miscellaneous'),
#]

# -- Define master document -------------------------------------------------

#master_doc = 'index'  # Define the master document as 'index'