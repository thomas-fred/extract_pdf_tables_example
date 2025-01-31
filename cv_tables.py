import os
import sys
from typing import Any

from img2table.ocr import TesseractOCR
from img2table.document import PDF


if __name__ == "__main__":

    _, pdf_path = sys.argv

    pdf = PDF(
        pdf_path,
        pages=list(range(27, 31)),
        detect_rotation=False,
        pdf_text_extraction=True
    )

    ocr = TesseractOCR(n_threads=4, lang="eng")

    tables = pdf.extract_tables(
        ocr=ocr,
        implicit_rows=False,
        implicit_columns=False,
        borderless_tables=False,
        min_confidence=30
    )

    def substitute_newline(value: Any) -> Any:
        if isinstance(value, str):
            return value.replace("\n", " ")
        else:
            return value

    os.makedirs("tables", exist_ok=True)

    for page_number, table_list in tables.items():
        for table_i, table in enumerate(table_list):
            df = table.df
            df = df.map(substitute_newline)
            df = df.rename(columns=df.iloc[0])
            df = df.drop(df.index[0])
            df.to_csv(f"tables/page-{page_number + 1}_table-num-{table_i}.csv", index=False)
