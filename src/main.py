# main.py
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

import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, Gdk

from .window import BookmarksWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.byteheathen.BookMarks',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.styleProvider = Gtk.CssProvider()
        self.styleProvider.load_from_resource("/org/byteheathen/BookMarks/styles/bookmark.css")
        self.styleProvider.load_from_resource("/org/byteheathen/BookMarks/styles/tag.css")

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), self.styleProvider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = BookmarksWindow(application=self)
        win.present()


def main(version):
    app = Application()
    return app.run(sys.argv)
