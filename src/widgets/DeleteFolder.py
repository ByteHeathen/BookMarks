from gi.repository import Gtk

from pybookmarks import BookMark

@Gtk.Template(resource_path='/org/byteheathen/BookMarks/ui/delete-folder.ui')
class DeleteFolder(Gtk.Popover):
    __gtype_name__ = 'DeleteFolder'
    cancelButton = Gtk.Template.Child()
    createButton = Gtk.Template.Child()

    def __init__(self, widget, cancelCallback, **kwargs):
        super().__init__(**kwargs)
        self.set_relative_to(widget)
        self.cancelCallback = cancelCallback
        self.cancelButton.connect("clicked", self.cancelCallback)
        self.createButton.connect("clicked", self.create)
        self.show_all()
        self.popup()

    def create(self, widget):
        self.cancelCallback(self, reload=True)
