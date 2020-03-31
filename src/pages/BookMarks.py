from gi.repository import Gtk

from pybookmarks import BookMark
from .BookMarkCard import BookMarkCard
from .QuickCreateBookMark import QuickCreateBookMark
from .DeleteBookMark import DeleteBookMark
from .FlatButton import FlatButton

class BottomBar(Gtk.ButtonBox):

    def __init__(self, page, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.createPopover = None
        self.deletePopover = None
        self.createButton = FlatButton(icon='list-add')
        self.createButton.connect("clicked", self.onCreateClicked)
        self.deleteButton = FlatButton(icon='user-trash')
        self.add(self.createButton)
        self.add(self.deleteButton)

    def onCreateClicked(self, widget):
        self.createPopover = QuickCreateBookMark(self.createButton, self.removeCreatePopover)

    def onDeleteClicked(self, widget):
        bk = self.page.list.get_selected_row().bookmark
        self.deletePopover = DeleteBookMark(self.deleteButton, self.removeDeletePopover, bk)

    def removeCreatePopover(self, widget, reload=False):
        self.createPopover.hide()
        self.createPopover = None
        if reload:
            self.page.empty()
            self.page.load()

    def removeDeletePopover(self, widget, reload=True):
        self.deletePopover.hide()
        self.deletePopover = None
        if reload:
            self.page.empty()
            self.page.load()

class BookMarks(Gtk.Box):

    def __init__(self, hexpand=True, **kwargs):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, **kwargs)
        self.scrollWindow = Gtk.ScrolledWindow(vexpand=True)
        self.viewport = Gtk.Viewport()
        self.list = Gtk.ListBox()
        self.viewport.add(self.list)
        self.scrollWindow.add(self.viewport)
        self.buttons = BottomBar(self)
        self.add(self.scrollWindow)
        self.add(self.buttons)
        self.load()

    def empty(self):
        for child in self.list.get_children():
            self.list.remove(child)

    def load(self):
        for bookmark in BookMark.all():
            self.list.add(BookMarkCard(bookmark))
        self.list.show_all()
        
