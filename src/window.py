# window.py
#
# Copyright 2023 Francesco Caracciolo
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
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk
from .pages import PAGES
@Gtk.Template(resource_path='/moe/nyarchlinux/tour/window.ui')
class NyarchtourWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NyarchtourWindow'

    carousel = Gtk.Template.Child("carousel")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for page in PAGES:
            p = self.generate_page(page)
            self.carousel.append(p)

    def generate_page(self, page):
        builder = Gtk.Builder.new_from_resource("/moe/nyarchlinux/tour/carousel_page.ui")
        p = builder.get_object("page")
        titlelabel = builder.get_object("title")
        bodylabel = builder.get_object("body")
        gtkimage = builder.get_object("image")

        titlelabel.set_label(page["title"])
        bodylabel.set_label(page["body"])
        gtkimage.set_from_icon_name(page["icon"])
        return p
