from gi.repository import Gtk

class FlatButton(Gtk.Button):

    def __init__(self, label=None, icon=None, **kwargs):
        super().__init__(**kwargs)
        if label is None and icon is not None:
            icon = Gtk.Image.new_from_icon_name(icon, 0)
            self.add(icon)
        else:
            self.add(Gtk.Label(label))
        Gtk.StyleContext.add_class(self.get_style_context(), "borderless")
