# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'UTDallas HPC Cluster Users Guide'
copyright = '2019, Noah Castetter'
author = 'Noah Castetter'

# The full version, including alpha/beta/rc tags
release = '1.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'guzzle_sphinx_theme'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# def setup(app):
#     app.add_stylesheet('pygments.css')
#     app.add_stylesheet('nature.css')
#     app.add_stylesheet('utd.css')



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'utd.css'

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['./themes/.']

extensions.append("sphinx_rtd_theme")

html_theme_options = {
    
        'navigation_depth': "3",
		
		'collapse_navigation': False,
		
		'includehidden': True,        

}

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']


#html_css_files = [
#		'_static/alabaster.css',
	#	'_static/basic.css',
	#	'_static/custom.css',
	#	'_static/nature.css',
	#	'_static/pygments.css',
	#	'_static/utd.css',
	#	'_static/utd2.css',
#]

#html_style = 'utd.css'

#html_theme_options = {
    
  #      'navigation_depth': 4,
  #      'collapse_navigation': False
#
#}
