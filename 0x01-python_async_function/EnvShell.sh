#!/usr/bin/bash
python3 -m venv ./py37async
source ./py37async/bin/activate
pip install --upgrade pip aiohttp aiofiles
