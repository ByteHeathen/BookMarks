from gi.repository import Gtk

from .FolderDisplay import FolderDisplay
from .TagBadge import TagBadge

from pybookmarks import Folder

class BookMarkCard(Gtk.ListBoxRow):

    def __init__(self, bookmark, **kwargs):
        super().__init__(**kwargs)
        self.bookmark = bookmark
        self.iconTheme = Gtk.IconTheme()
        self.tagList = Gtk.ListBox()
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.vbox)
        Gtk.StyleContext.add_class(self.get_style_context(), "bookmark-card")

        self.topBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.vbox.add(self.topBox)

        if self.bookmark.starred == False:
            self.starButton = Gtk.Button()
            self.starButton.add(Gtk.Image.new_from_icon_name("starred-symbolic", 0))
            self.topBox.add(self.starButton)
        else:
            icon = Gtk.Image.new_from_icon_name("starred-symbolic", 0)
            Gtk.StyleContext.add_class(icon.get_style_context(), "starred")
            self.starButton = Gtk.Button()
            Gtk.StyleContext.add_class(self.starButton.get_style_context(), "starred")
            self.starButton.add(Gtk.Image.new_from_icon_name("starred-symbolic", 0))
            self.topBox.add(self.starButton)
        self.starButton.connect("clicked", self.toggleStarred)

        if self.bookmark.folder is not None:
            self.topBox.pack_end(FolderDisplay(Folder.find(self.bookmark.folder)), False, False, 0)
        else:
            self.topBox.pack_end(FolderDisplay(None), False, False, 0)

        if self.bookmark.label != None:
            self.maybeLabel = Gtk.Label(label=self.bookmark.label)
            Gtk.StyleContext.add_class(self.maybeLabel.get_style_context(), "text-lead")
            self.topBox.add(self.maybeLabel)
            self.urlLabel = Gtk.Label(label=self.bookmark.url)
            self.urlLabel.set_xalign(0.20)
            Gtk.StyleContext.add_class(self.urlLabel.get_style_context(), "text-minor")
            self.vbox.add(self.urlLabel)
        else:
            self.urlLabel = Gtk.Label(label=self.bookmark.url)
            Gtk.StyleContext.add_class(self.urlLabel.get_style_context(), "text-lead")
            self.topBox.add(self.urlLabel)

        for tag in self.bookmark.tags():
            self.tagList.add(TagBadge(tag))
        self.vbox.add(self.tagList)

    def toggleStarred(self, widget):
        if self.bookmark.starred == False:
            Gtk.StyleContext.add_class(self.starButton.get_style_context(), "starred")
            self.bookmark.starred = True
            self.bookmark.save()
        else:
            Gtk.StyleContext.remove_class(self.starButton.get_style_context(), "starred")
            self.bookmark.starred = False
            self.bookmark.save()

