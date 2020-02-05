from gi.repository import Gtk

from pybookmarks import Tag

@Gtk.Template(resource_path='/org/byteheathen/BookMarks/ui/forms/quick-create-tag.ui')
class QuickCreateTag(Gtk.Popover):
    __gtype_name__ = 'QuickCreateTag'

    labelEntry = Gtk.Template.Child()
    colorEntry = Gtk.Template.Child()
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
        name = self.labelEntry.get_text()
        if name == "" or name == None:
            name = None
        color = self.colorEntry.get_color().to_string()
        if color == "" or color == None:
            color = None
        Tag.create(label=name, color=color)
        self.cancelCallback(self, reload=True)
