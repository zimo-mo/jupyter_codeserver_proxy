"""
Return config on servers to start for codeserver

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil


def setup_codeserver():
    # Make sure codeserver is in $PATH
    def _codeserver_command(port):
        full_path = shutil.which('code-server')
        if not full_path:
            raise FileNotFoundError('Can not find code-server in $PATH')
        working_dir = os.getenv("CODE_WORKINGDIR", None)
        if working_dir is None:
            working_dir = os.getenv("JUPYTER_SERVER_ROOT", ".")
        extensions_dir = os.path.expanduser("~/.vscode/extensions")
        command = [
            full_path, "--bind-addr", f"0.0.0.0:{port}", "--auth", "none",
            "--disable-telemetry", "--show-versions"
        ]
        if os.path.exists(extensions_dir):
            command.append("--extensions-dir")
            command.append(extensions_dir)
        command.append(working_dir)
        return command

    return {
        'command': _codeserver_command,
        'timeout': 20,
        'absolute_url': False,
        'new_browser_tab': False,
        'launcher_entry': {
            'title':
            'VS Code IDE',
            'icon_path':
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons',
                         'vscode.svg')
        }
    }
