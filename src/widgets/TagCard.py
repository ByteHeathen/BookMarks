from gi.repository import Gtk, Gdk

from .FolderDisplay import FolderDisplay

class TagCard(Gtk.ListBoxRow):

    def __init__(self, tag, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.iconTheme = Gtk.IconTheme()
        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(self.box)
        Gtk.StyleContext.add_class(self.get_style_context(), "tag-card")

        self.topBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.label = Gtk.Label(label=self.tag.label)
        self.box.add(self.label)
        if self.tag.color != None:
            self.colorLabel = Gtk.Label()
            self.colorLabel.set_markup("⬤")
            color = Gdk.Color.parse(self.tag.color)
            self.colorLabel.modify_fg(Gtk.StateType.NORMAL, color[1])
        self.box.pack_end(self.colorLabel, False, False, 0)
        
