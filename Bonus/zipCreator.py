import zipfile
import pathlib
def compress(what,where):
    with zipfile.ZipFile(pathlib.Path(where,"compressed.zip"),"w") as zip:
        for filepath in what:
            filepath = pathlib.Path(filepath)
            zip.write(filepath,arcname=filepath.name)
