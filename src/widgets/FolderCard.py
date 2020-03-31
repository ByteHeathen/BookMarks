from gi.repository import Gtk

from .FlatButton import FlatButton

class FolderCard(Gtk.ListBoxRow):

    def __init__(self, folder, callBack, **kwargs):
        super().__init__(**kwargs)
        self.callback = callBack
        self.folder = folder
        self.iconTheme = Gtk.IconTheme()
        self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(self.box)
        Gtk.StyleContext.add_class(self.get_style_context(), "folder-card")

        self.topBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.label = Gtk.Label(label=self.folder.label)
        self.chooseButton = FlatButton(label="⮞")
        self.chooseButton.connect("clicked", self.onSelectClicked)
        self.box.add(self.label)
        self.box.pack_end(self.chooseButton, False, False, 0)

    def onSelectClicked(self, widget):
        self.callback(self.folder)
