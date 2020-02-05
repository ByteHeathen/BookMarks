from gi.repository import Gtk, Pango

from .QuickCreateFolder import QuickCreateFolder
from .FolderCard import FolderCard
from .BookMarkCard import BookMarkCard
from .QuickCreateBookMark import QuickCreateBookMark

from pybookmarks import root_folders
from pybookmarks import BookMark
from pybookmarks import Folder

class BottomBar(Gtk.ButtonBox):

    def __init__(self, page, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.createImage = Gtk.Image.new_from_icon_name("list-add", 0)
        self.createButton = Gtk.Button()
        self.createButton.add(self.createImage)
        self.createButton.connect("clicked", self.onCreateClicked)
        self.deleteButton = Gtk.Button()
        self.deleteImage = Gtk.Image.new_from_icon_name("user-trash", 0)
        self.deleteButton.add(self.deleteImage)
        self.menuPopover = Gtk.Popover()
        self.menuPopover.set_relative_to(self.createButton)
        self.menuBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.createFolderButton = Gtk.Button(label="Folder")
        self.createFolderButton.connect("clicked", self.createCreatePopover)
        self.createBookMarkButton = Gtk.Button(label="BookMark")
        self.createBookMarkButton.connect("clicked", self.createBookMarkPopover)
        self.menuBox.pack_start(self.createFolderButton, False, True, 0)
        self.menuBox.pack_start(self.createBookMarkButton, False, True, 0)
        self.menuPopover.add(self.menuBox)
        self.add(self.createButton)
        self.add(self.deleteButton)

    def onCreateClicked(self, widget):
        self.menuPopover.show_all()
        self.menuPopover.popup()

    def createCreatePopover(self, widget):
        self.createPopover = QuickCreateFolder(self.createButton, self.removeCreatePopover)

    def createBookMarkPopover(self, widget):
        self.createBookMarkPopover = QuickCreateBookMark(self.createButton, self.removeCreateBookMarkPopover)

    def removeCreatePopover(self, widget, reload=False):
        self.createPopover.popdown()
        self.createPopover = None
        if reload:
            self.page.empty()
            self.page.load()

    def removeCreateBookMarkPopover(self, widget, reload=False):
        self.createBookMarkPopover.popdown()
        self.createPopover = None
        if reload:
            self.page.empty()
            self.page.load()

class Folders(Gtk.Box):

    def __init__(self, **kwargs):
        super().__init__(margin=5, orientation=Gtk.Orientation.VERTICAL, **kwargs)
        self.currentFolder = None
        self.scrollWindow = Gtk.ScrolledWindow(vexpand=True)
        self.viewport = Gtk.Viewport(margin=20)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.backButton = Gtk.Button(label="⮜")
        self.backButton.connect("clicked", self.onBackPressed)
#        self.box.pack_start(self.backButton, False, False, 0)
        self.folderList = Gtk.ListBox(hexpand=True,)
        self.bookmarkList = Gtk.ListBox()
        self.folderLabel = Gtk.Label(label="Folders", xalign=0.0, margin=8)
        self.folderLabel.modify_font(Pango.FontDescription('Serif 14'))
        self.bookmarkLabel = Gtk.Label(label="BookMarks", xalign=0.0, margin=8)
        self.bookmarkLabel.modify_font(Pango.FontDescription('Serif 14'))
        self.box.pack_start(self.folderLabel, True, True, 0)
        self.box.pack_start(self.folderList, True, True, 0)
        self.box.pack_start(self.bookmarkLabel, True, True, 0)
        self.box.pack_start(self.bookmarkList, True, True, 0)
        self.viewport.add(self.box)
        self.scrollWindow.add(self.viewport)
        self.buttons = BottomBar(self)
        self.add(self.scrollWindow)
        self.add(self.buttons)
        self.load()

    def empty(self):
        for child in self.folderList.get_children():
            self.folderList.remove(child)
        for child in self.bookmarkList.get_children():
            self.bookmarkList.remove(child)

    def load(self):
        if self.currentFolder is not None:
            self.box.pack_start(self.backButton, False, False, 0)
            self.box.reorder_child(self.backButton, 0)
            self.backButton.show()
            for folder in self.currentFolder.children():
                self.folderList.add(FolderCard(folder, self.changeFolderCallback))
            for bookmark in self.currentFolder.bookmarks():
                self.bookmarkList.add(BookMarkCard(bookmark))
        else:
            self.backButton.hide()
            for folder in root_folders():
                self.folderList.add(FolderCard(folder, self.changeFolderCallback))
            for bookmark in BookMark.find_unfoldered():
                self.bookmarkList.add(BookMarkCard(bookmark))
        self.show()
        self.folderList.show_all()
        self.bookmarkList.show_all()


    def onBackPressed(self, widget):
        if self.currentFolder is not None and self.currentFolder.parent is not None:
            folder = Folder.find(self.currentFolder.parent)
            self.changeFolderCallback(folder)
        else:
            self.currentFolder = None
            self.empty()
            self.load()

    def changeFolderCallback(self, folder):
        self.empty()
        self.currentFolder = folder
        self.load()

