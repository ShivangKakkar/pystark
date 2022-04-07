# ChangeLog

Latest Version: `v1.0.2`

---

<a name="v1.0.2"></a>
### v1.0.2 <small>- April 7, 2022</small>

- Specify minimum python version which is `3.9`, in docs and pypi.
- More user-friendly boilerplate.

---

<a name="v1.0.1"></a>
### v1.0.1 <small>- April 7, 2022</small>

- Fix broken CLI due to bad imports.
- Add `dev-requirement.txt` for docs and pypi

---

<a name="v1.0.0"></a>
### v1.0.0 <small>- April 6, 2022</small>

- Enhanced project settings, inspired from django.
- Added brand new addons for additional features in bots.
- Brand-new documentation using Mkdocs instead of Sphinx.
- Database migration methods for `pystark.database.sql.Database` class like `add_column`, `remove_column`, etc.
- Added other useful methods like 
- Improved boilerplate in favour of new features.
- Added documentation for [project settings](/start/settings) using `settings.py`
- Removed customization options from `Stark.activate()` as they can be configured using `settings.py` now.
- Removed `pystark.database.postgres` in favour of `pystark.database.sql`.
- Added sudo users support for bots which can be set using `SUDO_USERS` environment variable.
- Allow username as `OWNER_ID` instead of only `user_id`
- Pre-made models for `users` and `bans` table.
- And much, much more! 

---


<a name="v0.4.0"></a>
### v0.4.0 <small>- March 15, 2022</small>

- BugFixes and improvements in SQL helper functions.
- Make Database related dependencies optional and automated.
- Class Database instead of functions
- Rollback at exceptions
- Raw SQL for getting all rows as it usually depends on python class instead of data in table
- Raise TableNotFound if it doesn't exist instead of returning None
- Rename `pystark.databases.postgres` to `pystark.databased.sql` in favour of other sql databases.
- Allow other type of Database URls
- Add attributes like `session`, `base`, `engine` to Database.


<a name="v0.3.0"></a>
### v0.3.0 <small>- January 28, 2022</small>

- Additions
    - Use inline mode and callback buttons more easily.
    - Handle inline queries using `Stark.inline()`.
    - Handle callback queries using `Stark.callback()`.
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
    - Fixed `ModuleNotFoundError` for psycopg2 (missing requirement).
- Documentation
    - Added documentation for [all decorators](/decorators). [Stark.callback][pystark.decorators.callback.Callback.callback] and [Stark.inline][pystark.decorators.inline.Inline.inline]
    - Added a temporary logo. Thanks to [Designatory](https://t.me/designatory).
    - Removed dark mode.
    - Separated older releases. [Can be found here](/older-releases).
    - Enable Single Version option.
    - Changed the color for annoying visited links.
    - Changed templates for footer and header.
    - Add homepage to toctree.
    - Custom 404 page. Thanks to [Designatory](https://t.me/designatory).
    - Other Improvements.
