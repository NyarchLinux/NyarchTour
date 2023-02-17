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
import subprocess
@Gtk.Template(resource_path='/moe/nyarchlinux/tour/window.ui')
class NyarchtourWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'NyarchtourWindow'

    carousel = Gtk.Template.Child("carousel")
    previous = Gtk.Template.Child("previous")
    nextbutton = Gtk.Template.Child("next")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.commands = {}
        for page in PAGES:
            p = self.generate_page(page)
            self.carousel.append(p)
        self.carousel.connect("page-changed", self.page_changes)
        self.nextbutton.connect("clicked", self.next_page)
        self.previous.connect("clicked", self.previous_page)

    def page_changes(self, carousel, page):
        if page > 0:
            self.previous.set_opacity(1)
        else:
            self.previous.set_opacity(0)
        if page >= self.carousel.get_n_pages()-1:
            self.nextbutton.set_opacity(0)
        else:
           self.nextbutton.set_opacity(1)
    def next_page(self, button):
        self.carousel.get_position()
        if self.carousel.get_position() < self.carousel.get_n_pages()-1:
            self.carousel.scroll_to(self.carousel.get_nth_page(self.carousel.get_position()+1), True)

    def previous_page(self, button):
        self.carousel.get_position()
        if self.carousel.get_position() > 0:
            self.carousel.scroll_to(self.carousel.get_nth_page(self.carousel.get_position()-1), True)

    def generate_page(self, page):
        builder = Gtk.Builder.new_from_resource("/moe/nyarchlinux/tour/carousel_page.ui")
        p = builder.get_object("page")
        titlelabel = builder.get_object("title")
        bodylabel = builder.get_object("body")
        gtkimage = builder.get_object("image")
        buttonsBox = builder.get_object("buttonsBox")
        for button in page['buttons']:
        	Gtkbutton = Gtk.Button()
        	button_content = Adw.ButtonContent()
        	# Set properties
        	if button["style"] is not None:
        		Gtkbutton.set_css_classes([button["style"]])
        	if button["icon"] is not None:
        		button_content.set_icon_name(button["icon"])
        		button_content.set_use_underline(True)
        		button_content.set_label(button["label"])
        		Gtkbutton.set_child(button_content)
        	else:
        		Gtkbutton.set_label(button["label"])
        	self.commands[Gtkbutton] = button["command"]
        	Gtkbutton.connect("clicked", self.button_clicked)
        	buttonsBox.append(Gtkbutton)

        titlelabel.set_label(page["title"])
        bodylabel.set_label(page["body"])
        gtkimage.set_resource("/moe/nyarchlinux/tour/pictures/" + page["icon"] + ".png")
        #gtkimage.set_pixel_size(page["icon-size"])
        return p

    def button_clicked(self, button):
        	self.background_process(self.commands[button])

    def background_process(self, command):
    	subprocess.Popen(["flatpak-spawn",  "--host"] + command.split())
    
