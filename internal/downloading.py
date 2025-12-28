import pathlib, requests, zipfile, shutil, tempfile, os
from PySide6.QtCore import QObject, Signal

import internal.config

def get_local_game():
    try:
        return [int(i) for i in (pathlib.Path(internal.config.working_path) / "game" / "TBAddonManager" / "VERSION").read_text().split(".")]
    except Exception as e:
        print(str(e))
        return None

def get_remote_game():
    try:
        return [int(i) for i in requests.get("https://raw.githubusercontent.com/somepoi/TBAddonManager/game-implementation/VERSION").text.split(".")]
    except Exception as e:
        print(str(e))
        return None

def text_game():
    local = get_local_game()
    remote = get_remote_game()
    if not local:
        return ("Cannot get local files! Are game component files installed?", [None])
    if not remote:
        return ("Cannot get remote files! Please, check your internet connection.", [None])
    for i in range(3):
        if remote[i] > local[i]:
            return ("The current version of the game component files ({0}) is outdated.\nPlease update them to the latest version ({1}).", [".".join([str(i) for i in local]), ".".join([str(i) for i in remote])])
    return ("The current version of the game component files is up to date! ({0})", [".".join([str(i) for i in local]), ".".join([str(i) for i in remote])])

class DownloadGameRunner(QObject):

    status = Signal(str, list)
    finished = Signal()

    def run(self):

        target_dir = pathlib.Path(internal.config.working_path) / "game" / "TBAddonManager"

        if target_dir.exists():
            shutil.rmtree(target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)

        tmp_filename = None

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:

            self.status.emit("Starting the download...", [])

            tmp_filename = tmp_file.name

            try:
                downloaded = 0
                with requests.get("https://github.com/somepoi/TBAddonManager/archive/refs/heads/game-implementation.zip", stream=True, timeout=10) as r:
                    r.raise_for_status()
                    for chunk in r.iter_content(chunk_size=1024*1024):
                        tmp_file.write(chunk)
                        downloaded += len(chunk)
                        self.status.emit("{0} bytes downloaded...", [downloaded])
                    tmp_file.flush()
            except:
                self.finished.emit()
                return

            with zipfile.ZipFile(tmp_filename) as z:
                top_folder = z.namelist()[0].split("/", 1)[0]

                total = len(z.namelist())

                for i, member in enumerate(z.namelist()):
                    if not member.startswith(top_folder + "/"):
                        continue
                    rel = pathlib.Path(member[len(top_folder) + 1:])
                    if not rel.parts:
                        continue

                    out_path = target_dir / rel
                    if member.endswith("/"):
                        out_path.mkdir(parents=True, exist_ok=True)
                    else:
                        out_path.parent.mkdir(parents=True, exist_ok=True)
                        with z.open(member) as src, open(out_path, "wb") as dst:
                            shutil.copyfileobj(src, dst)
                    self.status.emit("Unpacking \"{0}\", {1} out of {2} files...", [str(rel), i, total])

        os.remove(tmp_filename)

        self.finished.emit()
