TOOLS = """
Available tools:

open_app(app_name)

open_folder(folder_name)

create_folder(folder_name)

google_search(query)

youtube_search(query)

screenshot()

time()

date()

remember(key,value)

recall(key)

exit()

If one tool is enough,
respond ONLY like this:

TOOL: open_app
ARG: chrome

If multiple tools are needed:

TOOL: open_app
ARG: chrome

TOOL: youtube_search
ARG: linux tutorials

If no tool is needed,
respond normally.
"""