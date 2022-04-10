"""This module contains some sticker conversion tools for Telegram"""

from PIL import Image


async def to_webp(path: str) -> str:
    """Convert any image to webp for telegram static stickers. Resizes according to telegram sticker requirements automatically.

    !!! important

        Requires library `pillow` which is not bundled with pystark.

        Add `pillow` to your `requirements.txt` | `pip install pillow`

    Parameters:
        path: Path of image to convert to webp.

    Returns:
        str: path to the converted webp image.

    Examples:

        ```python
        # This is an example plugin that converts any sent image to sticker and replies it back.

        import os
        from pystark import Stark, filters
        from pystark.helpers.stickers import to_webp


        # filters.photo means that this function will be executed if any message has a photo.
        @Stark.cmd(extra_filters=filters.photo)
        async def reply_webp(_, msg):
            message = await msg.reply("Converting...")
            file = await msg.download()
            # main function
            sticker = await to_webp(file)
            await msg.reply_sticker(sticker)
            await message.delete()
            # remove your image and sticker later
            os.remove(sticker)
            os.remove(file)

        ```
    """
    name = path.rsplit(".", 1)[0]+".webp"
    im = Image.open(path).convert("RGB")
    width, height = im.size
    max_pixels = 512
    ratio = min(max_pixels/width, max_pixels/height)
    size = (int(ratio*width), int(ratio*height))
    im.resize(size)
    im.save(name, "webp")
    return name
