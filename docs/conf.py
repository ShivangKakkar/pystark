import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'PyStark'
copyright = '2021-2022, StarkProgrammer'
author = 'StarkProgrammer'
release = '2021-2022'
extensions = [
    "sphinx_copybutton",
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
    "sphinx_toolbox.confval",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    # "sphinx_toolbox.github",
    # "sphinx_toolbox.sidebar_links",
    # "myst_parser"
]
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

templates_path = ['templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_rtd_theme'
# html_theme = "pydata_sphinx_theme"
html_favicon = 'images/favicon.ico'
copybutton_prompt_text = "$ "
default_dark_mode = False

# autodoc_class_signature = "separated"
autodoc_inherit_docstrings = False
add_module_names = False

# latex_engine = "xelatex"
# html_theme_options = {"logo_only": True}
# html_logo = "pystark.png"
# html_static_path = ['_static']
# github_username = 'StarkBotsIndustries'
# github_repository = 'pystark'

# .. confval:: text,
# sidebar, github
