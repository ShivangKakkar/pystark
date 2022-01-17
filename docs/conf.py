project = 'PyStark'
copyright = '2022, StarkProgrammer'
author = 'StarkProgrammer'
release = '2022'
extensions = [
    # "myst_parser",
    "sphinx_copybutton",
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
    "sphinx_toolbox.confval",
    "sphinx_toolbox.github",
    "sphinx_toolbox.sidebar_links"
]
# latex_engine = "xelatex"
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_rtd_theme'
# html_theme_options = {"logo_only": True}
# html_logo = "pystark.png"
html_favicon = 'favicon.ico'
# html_static_path = ['_static']
copybutton_prompt_text = "$ "
default_dark_mode = False
github_username = 'StarkBotsIndustries'
github_repository = 'pystark'

# .. confval:: text
