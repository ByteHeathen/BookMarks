from gi.repository import Gtk

from pybookmarks import Tag

@Gtk.Template(resource_path='/org/byteheathen/BookMarks/ui/delete-tag.ui')
class DeleteTag(Gtk.Popover):
    __gtype_name__ = 'DeleteTag'
    cancelButton = Gtk.Template.Child()
    createButton = Gtk.Template.Child()

    def __init__(self, widget, cancelCallback, tag, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.set_relative_to(widget)
        self.cancelCallback = cancelCallback
        self.cancelButton.connect("clicked", self.cancelCallback)
        self.createButton.connect("clicked", self.create)
        self.show_all()
        self.popup()

    def create(self, widget):
        self.tag.delete()
        self.cancelCallback(self, reload=True)
