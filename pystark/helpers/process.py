# PyStark - Python add-on extension to Pyrogram
# Copyright (C) 2021-2022 Stark Bots <https://github.com/StarkBotsIndustries>
#
# This file is part of PyStark.
#
# PyStark is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyStark is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyStark. If not, see <https://www.gnu.org/licenses/>.


import asyncio
import subprocess


def exec_sync(cmd: str, shell: bool = False) -> (str, str):
    """Execute a system command synchronously using Python and get the stdout and stderr as strings.

    Parameters:
        cmd: Command to execute.
        shell: Whether to run in shell mode.

    Returns:
        tuple of stdout and stderr as strings
    """
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=shell)
    stdout, stderr = proc.communicate()
    # None shouldn't be converted to "None" or b''
    if stdout:
        stdout = str(stdout.decode("utf-8"))
    else:
        stdout = ""
    if stderr:
        stderr = str(stderr.decode("utf-8"))
    else:
        stderr = ""
    return stdout, stderr


async def exec_async(cmd: str, shell: bool = False) -> (str, str):
    """Execute a system command asynchronously using Python and get the stdout and stderr as strings

    Parameters:
        cmd: Command to execute.
        shell: Whether to run in shell mode.

    Returns:
        tuple of stdout and stderr as strings
    """
    if shell:
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT, shell=True)
    else:
        proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT, shell=True)
    stdout, stderr = await proc.communicate()
    # None shouldn't be converted to "None" or b''
    if stdout:
        stdout = str(stdout.decode("utf-8"))
    else:
        stdout = ""
    if stderr:
        stderr = str(stderr.decode("utf-8"))
    else:
        stderr = ""
    return stdout, stderr
