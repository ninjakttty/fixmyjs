import sublime, sublime_plugin

class fixmyjsCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command('set_build_system', {
      'file': 'Packages/fixmyjs/fixmyjs.sublime-build'
    })
    self.window.run_command('build')
    self.window.run_command("hide_panel", {"panel": "output.exec"})
