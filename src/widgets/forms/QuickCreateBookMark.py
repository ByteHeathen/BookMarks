from gi.repository import Gtk

from pybookmarks import BookMark
from pybookmarks import Folder
from pybookmarks import Tag

from .TagBadge import TagBadge

@Gtk.Template(resource_path='/org/byteheathen/BookMarks/ui/forms/quick-create-bookmark.ui')
class QuickCreateBookMark(Gtk.Popover):
    __gtype_name__ = 'QuickCreateBookMark'

    labelEntry = Gtk.Template.Child()
    urlEntry = Gtk.Template.Child()
    starredEntry = Gtk.Template.Child()
    cancelButton = Gtk.Template.Child()
    createButton = Gtk.Template.Child()
    folderStore = Gtk.Template.Child()
    folderSelect = Gtk.Template.Child()
    tagList = Gtk.Template.Child()
    tagStore = Gtk.Template.Child()

    def __init__(self, widget, cancelCallback, **kwargs):
        super().__init__(**kwargs)
        self.set_relative_to(widget)
        self.cancelCallback = cancelCallback
        self.cancelButton.connect("clicked", self.cancelCallback)
        self.createButton.connect("clicked", self.create)
        self.folderRenderer = Gtk.CellRendererText()
        self.folderSelect.pack_start(self.folderRenderer, True)
        self.folderSelect.add_attribute(self.folderRenderer, "text", 1)
        self.loadFolders()
        self.loadTags()
        self.show_all()
        self.popup()

    def create(self, widget):
        name = self.labelEntry.get_text()
        if name == "" or name == None:
            name = None
        url = self.urlEntry.get_text()
        if url == "" or url == None:
            url = None
        starred = self.starredEntry.get_active()
        if starred == "" or starred == None:
            starred = None

        folder_reqs = self.folderSelect.get_active_iter()
        if folder_reqs is None:
            folder = None
        else:
            folder = folder_reqs[0]

        bk = BookMark.create(label=name, url=url, starred=starred, folder=folder)
        print(bk.id)
        print(bk.label)
        for tag in self.tagList.get_selected_rows():
            print(tag.tag.id)
            bk.assign_tag(tag.tag.id)
        self.cancelCallback(self, reload=True)

    def loadFolders(self):
        for folder in Folder.all():
            self.folderStore.append([folder.id, folder.label, folder.parent])

    def loadTags(self):
        for tag in Tag.all():
            self.tagList.add(TagBadge(tag))
