"""
Gonka Tokenomics - Chart Utility Functions

Two helpers for Excel workbook post-processing and column manipulation:

1. fix_chart_rendering(xlsx_path)
   Post-processes a saved .xlsx to fix openpyxl 3.1.5 chart rendering
   issue in Excel.  Excel sometimes fails to render charts from files
   whose docProps/app.xml advertises "Openpyxl" as the Application.
   This replaces the string with "Microsoft Excel" so that Excel
   treats the file like its own.

2. col_to_num(col_letter)
   Converts a single column letter (A-Z) to its 1-based column number.

Only stdlib imports -- no openpyxl dependency.
"""

import os
import re
import shutil
import zipfile


def fix_chart_rendering(xlsx_path):
    """Patch the Application string inside an .xlsx so Excel renders charts.

    openpyxl 3.1.5 writes ``<Application>Openpyxl</Application>`` in
    ``docProps/app.xml``.  Some versions of Excel skip chart rendering
    when they see a non-Microsoft application tag.  This function
    rewrites the tag to ``Microsoft Excel`` via a temp-file swap.

    Args:
        xlsx_path: Path (str or Path-like) to the .xlsx file on disk.
                   The file is modified in-place.

    Raises:
        FileNotFoundError: If *xlsx_path* does not exist.
    """
    xlsx_path = str(xlsx_path)
    tmp_path = xlsx_path + ".tmp"

    with zipfile.ZipFile(xlsx_path, "r") as zin, \
         zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "docProps/app.xml":
                text = data.decode("utf-8")
                text = re.sub(
                    r"<Application>.*?</Application>",
                    "<Application>Microsoft Excel</Application>",
                    text,
                )
                data = text.encode("utf-8")
            zout.writestr(item, data)

    shutil.move(tmp_path, xlsx_path)


def col_to_num(col_letter):
    """Convert a single column letter to a 1-based column number.

    Examples:
        col_to_num('A') -> 1
        col_to_num('J') -> 10
        col_to_num('Z') -> 26

    Args:
        col_letter: A single uppercase or lowercase letter A-Z.

    Returns:
        int: 1-based column number.
    """
    return ord(col_letter.upper()) - ord("A") + 1
