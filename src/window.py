# window.py
#
# Copyright 2020 Bytebuddha
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

from .BookMarks import BookMarks
from .Tags import Tags
from .Folders import Folders

@Gtk.Template(resource_path='/org/byteheathen/BookMarks/ui/window.ui')
class BookmarksWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'BookmarksWindow'

    StackSwitcher = Gtk.Template.Child()
    Stack = Gtk.Template.Child()
    BookMarksPage = BookMarks()
    TagsPage = Tags()
    FoldersPage = Folders()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_default_size(350, 400)
        self.Stack.add_titled(self.BookMarksPage, "bookmarks", "BookMarks")
        self.Stack.add_titled(self.TagsPage, "tags", "Tags")
        self.Stack.add_titled(self.FoldersPage, "folders", "Folders")

        self.StackSwitcher.set_stack(self.Stack)
        self.show_all()

