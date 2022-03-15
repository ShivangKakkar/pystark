import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

from pystark import __version__

project = 'PyStark'
copyright = '2021-2022, StarkProgrammer'
author = 'StarkProgrammer'
release = '2021-2022'
extensions = [
    "sphinx_copybutton",
    "sphinx_rtd_theme",
    "sphinx_toolbox.confval",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "notfound.extension",
    # 'sphinx_search.extension',
    # "sphinx_rtd_dark_mode",
    # "sphinx_toolbox.github",
    # "sphinx_toolbox.sidebar_links",
    # "myst_parser"
]

rst_epilog = f"""
.. |version| replace:: {__version__}
.. |code_version| replace:: ``{__version__}``
"""
html_title = 'PyStark Documentation'
html_favicon = 'images/favicon.ico'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {"logo_only": True}
html_logo = "images/pystark.png"
html_static_path = ['_static']
html_css_files = ['custom.css']
templates_path = ['templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

copybutton_prompt_text = "$ "
autodoc_inherit_docstrings = False
add_module_names = False
autodoc_class_signature = "separated"

# latex_engine = "xelatex"
# default_dark_mode = False
# github_username = 'StarkBotsIndustries'
# github_repository = 'pystark'

# napoleon_google_docstring = True
# napoleon_numpy_docstring = True
# napoleon_include_private_with_doc = False
# napoleon_include_special_with_doc = False
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = True
# napoleon_use_rtype = True

# sidebar, github
