# image search for catuserbot
import os
import shutil
import googleimagesdownload

@register(outgoing=True, pattern="^.img (.*)")
async def img_sampler(event):
    """ For .img command, search and return images matching the query. """
    await event.edit("Processing...")
    query = event.pattern_match.group(1)
    lim = findall(r"lim=\d+", query)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 5
    response = googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }
    # passing the arguments to the function
    try:
        paths = response.download(arguments)
    except Exception as e:
        return await cat.edit(f"Error: \n{e}")
    lst = paths[0][query]
    await event.client.send_file(event.chat_id, lst, reply_to=reply_to_id)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await cat.delete()
