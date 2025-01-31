# Installation

## Linux

```sh
micromamba create -f env.yml -y
sudo apt install tesseract
```

# Usage

# PDF to text

```sh
pdftotext -layout CDF-Report-2023-AG.pdf
```

# PDF tables to CSV

```sh
python cv_tables.py CDF-Report-2023-AG.pdf
```
