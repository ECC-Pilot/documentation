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
# sys.path.insert(0, os.path.abspath("."))
import datetime

# -- Project information -----------------------------------------------------

project = "ECC-Pilot"
copyright = f"{datetime.date.today().year}, EUGLOH Working Package - Campus Life"
author = "EUGLOH Working Package - Campus Life"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.githubpages",
    #"sphinxcontrib.spelling",
    "sphinx_issues",
    # 
    "sphinx.ext.graphviz",
    "sphinxcontrib.mermaid",
    "sphinx.ext.todo",
    #"sphinxcontrib-needs",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_title = "European Campus Card Pilot Project"
html_logo = "_static/eugloh-logo.svg"
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for sphinxcontrib.spelling -------------------------------

spelling_lang = "en_US"

spelling_show_suggestions = True
spelling_warning = True

# -- Options for MyST -------------------------------------------------

myst_enable_extensions = [
    "deflist",
    "fieldlist",
    "colon_fence",
    # "linkify",
]

# -- Options for Sphinx.ext.todo --------------------------------------

todo_include_todos = True