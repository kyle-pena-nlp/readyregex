# Configuration file based on pytest's sphinx config file

# -- Project information -----------------------------------------------------

import shutil

project = 'readyregex'
copyright = '2022, Kyle Pena'
author = 'Kyle Pena'

from readyregex import __version__ as _version, \
    __author__ as _author, \
    __copyright__ as _copyright, \
    __name__ as _name

project = _name
author = _author
copyright = _copyright
release = ".".join(_version.split(".")[:2])

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "pallets_sphinx_themes",
    "pygments_pytest",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

if shutil.which("inkscape"):
    extensions.append("sphinxcontrib.inkscapeconverter")

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = ".rst"

master_doc = "contents"

pygments_style = "sphinx"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.eggs', '.github', '.pytest_cache', '.tox', '.vscode', 'build', 'readyregex.egg-info', 'tests']

_repo = "https://github.com/kyle-pena-nlp/readyregex"

ext_links = {}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "flask"

html_title = "readyregex documentation"

html_short_title = "readyregex-%s" % release

html_theme_path = ["_themes"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "img/logo.png"

html_theme_options = {
    "logo_only": True,
    "display_version": False
}

html_domain_indices = True

html_use_index = False

html_show_sourcelink = False