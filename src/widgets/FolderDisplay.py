from gi.repository import Gtk

from pybookmarks import Folder

class FolderDisplay(Gtk.Box):

    def __init__(self, folder):
        super().__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self.folderIcon = Gtk.Image.new_from_icon_name("folder", 0)
        self.add(self.folderIcon)
        if folder is None:
            self.add(Gtk.Label(label="n/a"))
        else:
            self.add(Gtk.Label(label=folder.label))
