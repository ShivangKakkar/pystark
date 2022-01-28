Generating Boilerplate
========================

PyStark comes with a command line tool to make everything even more simpler. You can easily generate a boilerplate to get started.
You can also create a boilerplate with added Heroku support. Isn't that amazing?

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

--------

What is a boilerplate ?
-----------------------

Boilerplate Code or Boilerplate refers to sections of code that have to be included in many places with little or no alteration.

While using PyStark some code will be same for all bots. Our tool will help you to generate that much code, so you don't have to code and it makes it easier to use PyStark. When you will generate a boilerplate using pystark, a folder with some files will be created for you.

You can choose to generate a boilerplate with or without Heroku Support. For first-timers, I recommend try using without Heroku Support which can be run locally.

--------

Generating a boilerplate to run locally
---------------------------------------

For generating a boilerplate for local deployment, run this command:

.. code-block:: console

    $ pystark --boilerplate


A folder named ``boilerplate`` will be created for you in that folder.

--------

Generating a boilerplate with Heroku Support
--------------------------------------------

For added Heroku support, run this command:

.. code-block:: console

    $ pystark --boilerplate-heroku

A folder named ``boilerplate`` will be created for you in that folder.
