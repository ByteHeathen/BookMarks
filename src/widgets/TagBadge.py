from gi.repository import Gtk, Gdk

class TagBadge(Gtk.ListBoxRow):

    def __init__(self, tag, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.tagLabel = Gtk.Label(label=self.tag.label, margin=5)
        if self.tag.color != None:
            self.colorLabel = Gtk.Label(label="⬤", margin=5)
            color = Gdk.Color.parse(self.tag.color)
            self.colorLabel.modify_fg(Gtk.StateType.NORMAL, color[1])
            self.box.pack_start(self.colorLabel, False, False, 10)
        self.box.pack_start(self.tagLabel, False, False, 0)
        self.add(self.box)
