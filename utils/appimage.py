from genericpath import isfile
from subprocess import check_call
import subprocess
from tqdm import tqdm
import requests
import os, sys
import tarfile
import shutil

class AppImage:
  url = ""
  output_path = os.path.join(os.environ["HOME"], ".dotfiles", ".app_installs")
  name = ""
  saveName = ""

  def __init__(self, url: str, name: str, saveName: str) -> None:
    self.url = url
    self.name = name
    self.saveName = saveName
    # return cls

  def install(self) -> None:
    res = requests.get(self.url, stream=True)
    total_size = int(res.headers.get('content-length', 0))
    chunk_size = 1024

    # output = f"{self.output_path}/{self.name}.tar.gz"
    output = os.path.join(self.output_path, f"{self.name}")
    with open(f"{output}.tar.gz", "wb") as file, tqdm(
      desc=output,
      total = total_size,
      unit="B",
      unit_scale=True,
      unit_divisor=chunk_size) as bar:
        for chunk in res.iter_content(chunk_size=chunk_size):
           file.write(chunk)
           bar.update(len(chunk))

    tar = tarfile.open(f"{output}.tar.gz", "r:gz")
    tar.extractall(f"{self.output_path}")
    tar.close()

    if sys.platform == "linux":
       res = subprocess.Popen(["which", self.saveName], stdout=subprocess.PIPE)
       out, _ = res.communicate()
       out = out.decode().strip()

       if out:
         if os.path.isfile(os.path.realpath(out)):
            if os.path.islink(out):
             os.unlink(out)
            else:
              shutil.rmtree(out)
         if not os.path.exists(f"/opt/{self.name}"):
            shutil.copytree(src=output, dst=f"/opt/{self.name}")

       os.symlink(src=f"/opt/{self.name}/bin/{self.saveName}", dst=f"/usr/bin/{self.saveName}")
          

