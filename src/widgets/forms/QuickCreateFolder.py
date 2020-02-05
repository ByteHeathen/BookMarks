from gi.repository import Gtk

from pybookmarks import Folder

@Gtk.Template(resource_path='/org/byteheathen/BookMarks/ui/forms/quick-create-folder.ui')
class QuickCreateFolder(Gtk.Popover):
    __gtype_name__ = 'QuickCreateFolder'

    labelEntry = Gtk.Template.Child()
    parentSelect = Gtk.Template.Child()
    cancelButton = Gtk.Template.Child()
    createButton = Gtk.Template.Child()

    def __init__(self, widget, cancelCallback, **kwargs):
        super().__init__(**kwargs)
        self.set_relative_to(widget)
        self.list = Gtk.ListStore(int, str, int)
        self.parentSelect.set_model(self.list)
        renderer_text = Gtk.CellRendererText()
        self.parentSelect.pack_start(renderer_text, True)
        self.parentSelect.add_attribute(renderer_text, "text", 1)
        self.cancelCallback = cancelCallback
        self.cancelButton.connect("clicked", self.cancelCallback)
        self.createButton.connect("clicked", self.create)
        self.load()
        self.show_all()
        self.popup()

    def create(self, widget):
        name = self.labelEntry.get_text()
        if name == "" or name == None:
            name = None
        parent = self.parentSelect.get_active()
        print(parent)
        if parent == None:
            Folder.create(label=name)
        else:
            raw_parent = self.list.get_iter([parent, 0])
            Folder.create(label=name, parent=self.list[raw_parent][0])
        self.cancelCallback(self, reload=True)

    def load(self):
        for folder in Folder.all():
            self.list.append([folder.id, folder.label, folder.parent])
