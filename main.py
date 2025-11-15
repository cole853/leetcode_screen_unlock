import sys
import gi
import os

gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.1')
from gi.repository import GLib, Gtk, WebKit2

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.cole.leetcodeunlock")
        GLib.set_application_name('LeetCode PC Unlock')

    def do_activate(self):
        window = Gtk.Window(application=self, title="Hello World")
        window.set_default_size(1200, 800)

        webview = WebKit2.WebView()
        webview.connect("load-changed", self.on_load_changed)
        webview.connect("load-failed", self.on_load_failed)

        cookie_manager = webview.get_website_data_manager().get_cookie_manager()
        cookie_manager.set_persistent_storage(
            os.path.expanduser("~/.leetcode-cookies.txt"),
            WebKit2.CookiePersistentStorage.TEXT
        )

        webview.load_uri("https://www.leetcode.com/problemset/")

        window.add(webview)
        window.present()
        window.show_all()
    
    def on_load_changed(self, webview, load_event):
        print(f"Load event: {load_event}")
        if load_event == WebKit2.LoadEvent.FINISHED:
            print("Page finished loading!")
        
    def on_load_failed(self, webview, load_event, failing_uri, error):
        print(f"Load failed: {error}")
        return False


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)