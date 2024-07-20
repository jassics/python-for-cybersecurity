from py_avataaars import PyAvataaar
# you might need to install cairo library.
# For mac: type `brew install cairo`
avatar = PyAvataaar()
avatar.render_png_file('basic_avatar.png')
avatar.render_svg_file('basic_avatar.svg')

