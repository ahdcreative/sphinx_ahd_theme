import os
import sys
import sphinx_ahd_theme

sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_ahd_theme',
    'myst_parser'
]
templates_path = ['_templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
master_doc = 'index'
project = 'Sphinx AHD Theme'
copyright = "2022 - AHDCreative Solutions"
author = "AHD"
# The short X.Y version.
version = sphinx_ahd_theme.__version__
# Full Version
release = sphinx_ahd_theme.__version__
language = "en"
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'requirements.txt']
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False
today_fmt = '%d-%m-%Y %H:%M'
# -- Options for HTML output -------------------------------------------
html_theme = 'sphinx_ahd_theme'
html_static_path = []
# -- Options for HTMLHelp output ---------------------------------------
htmlhelp_basename = 'sphinx_ahd_themedoc'
# -- Options for LaTeX output ------------------------------------------
latex_elements = {}
latex_documents = [
    (master_doc, 'sphinx_ahd_theme.tex',
     'Sphinx Wagtail theme documentation',
     'Martin Bless', 'manual'),
]
# -- Options for manual page output ------------------------------------
man_pages = [
    (master_doc, 'sphinx_ahd_theme',
     'Sphinx AHD theme documentation',
     [author], 1)
]
# -- Options for Texinfo output ----------------------------------------
texinfo_documents = [
    (master_doc, 'sphinx_ahd_theme',
     'Sphinx AHD theme documentation',
     author,
     'sphinx_ahd_theme',
     'One line description of project.',
     'Miscellaneous'),
]
github_doc_root = 'https://github.com/ahdcreative/sphinx_ahd_theme/tree/main/docs'


def setup(app):
    pass


# https://docs.readthedocs.io/en/stable/guides/manage-translations.html#create-translatable-files
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-gettext_uuid
gettext_uuid = True
gettext_compact = False
