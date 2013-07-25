import urllib.request
import json
import sublime, sublime_plugin
import subprocess

class HtmlToJadeFromFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        source = self.view.file_name()
        if source.endswith(".html"):
            target = source + '.jade'
        if target:
            with open(source, 'r') as f:
                html = f.read()
            jade = HTHTools.convertHTML2Jade(html)
            if jade != None:
                with open(target, 'w') as f:
                    f.write(jade)
                self.view.window().open_file(target)

    def is_enabled(self):
        return True #return (self.view.file_name().endswith(".html") or self.view.file_name().endswith(".erb"))

class HtmlToJadeFromSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                html = self.view.substr(region)
                jade = HTHTools.convertHTML2Jade(html)
                if jade != None:
                    self.view.replace(edit, region, jade)

    def is_enabled(self):
        return True #return self.view.file_name().endswith(".jade")

class HtmlToJadeFromClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        html = sublime.get_clipboard()
        jade = HTHTools.convertHTML2Jade(html)
        if jade != None:
            for region in self.view.sel():
                self.view.replace(edit, region, jade)

    def is_enabled(self):
        return True #return self.view.file_name().endswith(".jade")

class HTHTools:
    @classmethod
    def convertHTML2Jade(self, contents):
        html2jade = subprocess.Popen(
            'html2jade',
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        output, error = html2jade.communicate(contents.encode())

        if error:
            self.write_to_console(error)
            self.window.run_command("show_panel", {"panel": "output.exec"})
            return None
        return output.decode()

    def write_to_console(self, str):
        self.output_view = self.window.get_output_panel("exec")
        selection_was_at_end = (
            len(self.output_view.sel()) == 1 and
            self.output_view.sel()[0] == sublime.Region(self.output_view.size())
        )
        self.output_view.set_read_only(False)
        edit = self.output_view.begin_edit()
        self.output_view.insert(edit, self.output_view.size(), str)
        if selection_was_at_end:
            self.output_view.show(self.output_view.size())
        self.output_view.end_edit(edit)
        self.output_view.set_read_only(True)