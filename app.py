import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

my_zip = Path("./HISTDATA_COM_XLSX_EURUSD_M12018.zip")
current_dir = Path.cwd()

with zipfile.ZipFile(my_zip, "r") as zip_ref:
    zip_ref.extractall(current_dir)

with zipfile.ZipFile("./DAT_XLSX_EURUSD_M1_2018.xlsx", "r") as zip_ref:
    zip_ref.extractall(current_dir)

text_file_names = current_dir.glob("*txt")

for file in list(text_file_names):
    # with open(file) as txt:
    #     data = txt.readlines()
    print(file.read_text())

data_files = current_dir.glob("**/*.xml")
roots: list[ET.Element] = []
for file in list(data_files):
    tree = ET.parse(file)
    roots.append(tree.getroot())

for root in roots:
    for i in root.iter():
        print(f"data {i}")
