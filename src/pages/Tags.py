from gi.repository import Gtk

from .QuickCreateTag import QuickCreateTag
from .DeleteTag import DeleteTag
from .TagCard import TagCard
from pybookmarks import Tag

class TagPageBottomBar(Gtk.ButtonBox):

    def __init__(self, page, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.createImage = Gtk.Image.new_from_icon_name("list-add", 0)
        self.createButton = Gtk.Button()
        self.createButton.add(self.createImage)
        self.createButton.connect("clicked", self.onCreateClicked)
        self.deleteButton = Gtk.Button()
        self.deleteButton.connect("clicked", self.onDeleteClicked)
        self.deleteImage = Gtk.Image.new_from_icon_name("user-trash", 0)
        self.deleteButton.add(self.deleteImage)
        self.add(self.createButton)
        self.add(self.deleteButton)

    def onCreateClicked(self, widget):
        self.createPopover = QuickCreateTag(self.createButton, self.removeCreatePopover)

    def removeCreatePopover(self, widget, reload=False):
        self.createPopover.hide()
        self.createPopover = None
        if reload:
            self.page.empty()
            self.page.load()

    def onDeleteClicked(self, widget):
        tag = self.page.list.get_selected_row().tag
        self.deletePopover = DeleteTag(self.deleteButton, self.removeDeletePopover, tag)

    def removeDeletePopover(self, widget, reload=True):
        self.deletePopover.hide()
        self.deletePopover = None
        if reload:
            self.page.empty()
            self.page.load()


class Tags(Gtk.Box):

    def __init__(self, **kwargs):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, **kwargs)
        self.scrollWindow = Gtk.ScrolledWindow(vexpand=True)
        self.viewport = Gtk.Viewport()
        self.list = Gtk.ListBox()
        self.viewport.add(self.list)
        self.scrollWindow.add(self.viewport)
        self.buttons = TagPageBottomBar(self)
        self.add(self.scrollWindow)
        self.add(self.buttons)
        self.load()

    def empty(self):
        for child in self.list.get_children():
            self.list.remove(child)

    def load(self):
        for tag in Tag.all():
            self.list.add(TagCard(tag))
        self.list.show_all()
