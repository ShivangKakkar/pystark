ChangeLog
=========

Latest Version - |code_version|

------------------

.. confval:: v0.3.0

- Additions
    - Use inline mode and callback buttons more easily.
    - Handle inline queries using ``Stark.inline()``.
    - Handle callback queries using ``Stark.callback()``.
    - Load plugins from multiple directories. Instead of passing a 'str' to 'activate()' function, pass a list.
    - Allow passing other keyword arguments while creating bot client.
    - Override the in-built/default plugins automatically as they are loaded later now.
- PyStark CLI
    - Added optional argument ['-v', '--version'] to see currently installed version.
    - Removed optional argument ['-h', '--help'] as passing no argument does the same thing.
    - Made unnecessary arguments private.
- Improvements
    - Improved PyPI Home page and Project Readme.
    - Improved Boilerplate.
    - Upgraded TelegramDB.
    - Separated constants.
    - Renamed default plugins file to remove confusion.
- BugFixes
    - Fixed ``ModuleNotFoundError`` for psycopg2 (missing requirement).
- Documentation
    - Added documentation for :doc:`all decorators </decorators/index>`. :meth:`Stark.callback <pystark.decorators.callback.Callback.callback>` and :meth:`Stark.inline <pystark.decorators.inline.Inline.inline>`
    - Added a temporary logo. Thanks to `Designatory <https://t.me/designatory>`_.
    - Removed dark mode.
    - Separated older releases. :doc:`Can be found here </meta/older-releases>`.
    - Enable Single Version option.
    - Changed the color for annoying visited links.
    - Changed templates for footer and header.
    - Add homepage to toctree.
    - Custom 404 page. Thanks to `Designatory <https://t.me/designatory>`_.
    - Other Improvements.


.. toctree::
    :hidden:

    older-releases
