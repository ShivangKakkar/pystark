ChangeLog
=========

Latest Version - ``v0.2.7``

------------------

.. confval:: v0.2.7

- Auto Update Bot Menu at runtime. :doc:`Read More </topics/bot_menu>`
- Added description argument in ``command`` decorator(for bot menu).
- ``Stark.data()`` now also returns a dictionary of command descriptions (key=command, value=description). See :meth:`pystark.client.Stark.data`
- ``Stark.activate`` now takes a optional argument ``set_menu`` to disable (or enable) auto-update of bot menu. :ref:`Read More <customize-bot-menu>`
- Added docs for Bot Menu. :doc:`Read Here </topics/bot_menu>`

------------------

.. confval:: v0.2.6

- Added two new static methods to ``Stark`` class - :meth:`pystark.client.Stark.list_args` and :meth:`pystark.client.Stark.data`
- Improved ``Stark.log()`` function. Now pass int values for levels. See :meth:`pystark.client.Stark.log`
- Added docs for class ``Stark`` - :doc:`Read Here </topics/stark>`


.. confval:: v0.2.5

- Added in-built functions to query postgres tables - :ref:`Read More <default-functions>`
- Added ChangeLog to docs (this webpage)
- Improve documentation using sphinx-toolbox


.. confval:: v0.2.4

- This Documentation was created
