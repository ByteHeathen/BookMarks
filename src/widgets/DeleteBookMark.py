from gi.repository import Gtk

from pybookmarks import BookMark

@Gtk.Template(resource_path='/org/byteheathen/BookMarks/ui/delete-bookmark.ui')
class DeleteBookMark(Gtk.Popover):
    __gtype_name__ = 'DeleteBookMark'
    cancelButton = Gtk.Template.Child()
    createButton = Gtk.Template.Child()

    def __init__(self, widget, cancelCallback, bookmark, **kwargs):
        super().__init__(**kwargs)
        self.bookmark = bookmark
        self.set_relative_to(widget)
        self.cancelCallback = cancelCallback
        self.cancelButton.connect("clicked", self.cancelCallback)
        self.createButton.connect("clicked", self.create)
        self.show_all()
        self.popup()

    def create(self, widget):
        self.bookmark.delete()
        self.cancelCallback(self, reload=True)
