# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else.
# See astropy.sphinx.conf for which values are set there.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))
# IMPORTANT: the above commented section was generated by sphinx-quickstart, but
# is *NOT* appropriate for astropy or Astropy affiliated packages. It is left
# commented out with this explanation to make it clear why this should not be
# done. If the sys.path entry above is added, when the astropy.sphinx.conf
# import occurs, it will import the *source* version of astropy instead of the
# version installed (if invoked as "make html" or directly with sphinx), or the
# version in the build directory (if "python setup.py build_docs" is used).
# Thus, any C-extensions that are needed to build the documentation will *not*
# be accessible, and the documentation will not build correctly.

import datetime
import os
import sys

try:
    import astropy_helpers
except ImportError:
    # Building from inside the docs/ directory?
    if os.path.basename(os.getcwd()) == 'docs':
        a_h_path = os.path.abspath(os.path.join('..', 'astropy_helpers'))
        if os.path.isdir(a_h_path):
            sys.path.insert(1, a_h_path)

# Load all of the global Astropy configuration
from astropy_helpers.sphinx.conf import *

# Get configuration information from setup.cfg
try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser
conf = ConfigParser()
conf.read([os.path.join(os.path.dirname(__file__), '..', 'setup.cfg')])
setup_cfg = dict(conf.items('metadata'))

plot_html_show_source_link = False

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.1'

# We currently want to link to the latest development version of the astropy docs,
# so we override the `intersphinx_mapping` entry pointing to the stable docs version
# that is listed in `astropy/sphinx/conf.py`.
intersphinx_mapping['astropy'] = ('http://docs.astropy.org/en/latest/', None)
intersphinx_mapping['regions'] = ('http://astropy-regions.readthedocs.io/en/latest/', None)
intersphinx_mapping['reproject'] = ('http://reproject.readthedocs.io/en/latest/', None)
intersphinx_mapping['gadf'] = ('http://gamma-astro-data-formats.readthedocs.io/en/latest/', None)

# Extend intersphinx_mapping with packages we use in gammapy
intersphinx_mapping['uncertainties'] = ('http://pythonhosted.org/uncertainties/', None)
intersphinx_mapping['pandas'] = ('http://pandas.pydata.org/pandas-docs/stable/', None)
intersphinx_mapping['skimage'] = ('http://scikit-image.org/docs/stable/', None)
intersphinx_mapping['sklearn'] = ('http://scikit-learn.org/stable/', None)
intersphinx_mapping['photutils'] = ('http://photutils.readthedocs.io/en/latest/', None)
intersphinx_mapping['aplpy'] = ('http://aplpy.readthedocs.io/en/latest/', None)
intersphinx_mapping['naima'] = ('http://naima.readthedocs.io/en/latest/', None)
intersphinx_mapping['reproject'] = ('http://reproject.readthedocs.io/en/latest/', None)


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns.append('_templates')
exclude_patterns.append('_static')
exclude_patterns.append('**.ipynb_checkpoints')


#
# -- nbsphinx settings
extensions.extend([
    'nbsphinx',
    'sphinx_click.ext',
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinx.ext.mathjax',
])
nbsphinx_execute = setup_cfg['execute_notebooks']

# --

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog += """
"""

# -- Project information ------------------------------------------------------

# This does not *have* to match the package name, but typically does
project = setup_cfg['package_name']
author = setup_cfg['author']
copyright = '{0}, {1}'.format(
    datetime.datetime.now().year, setup_cfg['author'])

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

__import__(setup_cfg['package_name'])
package = sys.modules[setup_cfg['package_name']]

# The short X.Y version.
version = package.__version__.split('-', 1)[0]
# The full version, including alpha/beta/rc tags.
release = package.__version__

# -- Options for HTML output ---------------------------------------------------

# A NOTE ON HTML THEMES
# The global astropy configuration uses a custom theme, 'bootstrap-astropy',
# which is installed along with astropy. A different theme can be used or
# the options for this theme can be modified by overriding some of the
# variables set in the global configuration. The variables set in the
# global configuration are listed below, commented out.

html_theme_options = {
    'logotext1': 'gamma',  # white,  semi-bold
    'logotext2': 'py',  # orange, light
    'logotext3': ':docs'  # white,  light
}

# Add any paths that contain custom themes here, relative to this directory.
# To use a different custom theme, add the directory containing the theme.
# html_theme_path = []

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes. To override the custom theme, set this to the
# name of a builtin theme or the name of a custom theme in html_theme_path.
# html_theme = None

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = ''

# The Gammapy logo doesn't look good so small (would need to make it thicker)
# So let's use the Astropy icon for now, i.e. not set `html_favicon` here.
# https://github.com/gammapy/gammapy-website/tree/master/logos
# html_favicon = '_static/gammapy_logo.ico'

# TODO: set this image also in the title bar
# (html_logo is not the right option)

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = ''

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = '{0} v{1}'.format(project, release)

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'

# Static files to copy after template files
html_static_path = ['_static']

from gammapy.utils.docs import gammapy_sphinx_ext_activate
gammapy_sphinx_ext_activate()

# integration of notebooks from gamapy-extra repo
from gammapy.utils.docs import gammapy_sphinx_notebooks
gammapy_sphinx_notebooks(setup_cfg)

html_style = 'gammapy.css'

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [('index', project + '.tex', project + u' Documentation',
                    author, 'manual')]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', project.lower(), project + u' Documentation',
              [author], 1)]

# -- Options for the edit_on_github extension ----------------------------------------

if eval(setup_cfg.get('edit_on_github')):
    extensions += ['astropy.sphinx.ext.edit_on_github']

    versionmod = __import__(setup_cfg['package_name'] + '.version')
    edit_on_github_project = setup_cfg['github_project']
    if versionmod.version.release:
        edit_on_github_branch = "v" + versionmod.version.version
    else:
        edit_on_github_branch = "master"

    edit_on_github_source_root = ""
    edit_on_github_doc_root = "docs"


github_issues_url = 'https://github.com/gammapy/gammapy/issues/'

# -- Other options --

# http://sphinx-automodapi.readthedocs.io/en/latest/automodapi.html
# show inherited members for classes
automodsumm_inherited_members = True


# In `about.rst` and `references.rst` we are giving lists of citations
# (e.g. papers using Gammapy) that partly aren't referenced from anywhere
# in the Gammapy docs. This is normal, but Sphinx emits a warning.
# The following config option suppresses the warning.
# http://www.sphinx-doc.org/en/stable/rest.html#citations
# http://www.sphinx-doc.org/en/stable/config.html#confval-suppress_warnings
suppress_warnings = [
    'ref.citation'
]

# remove docs/notebooks folder
from gammapy.utils.docs import remove_notebooks
remove_notebooks()

# nitpicky = True
