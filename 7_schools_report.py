"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""

import json
from pathlib import Path


TARGET_CONF_CODES = {372, 108, 107, 130}   
GRAD_WOMEN_MIN = 50.0
INSTATE_OFFCAMPUS_MIN = 50000.0


KEY_NAME = "instnm"
KEY_GRAD_WOMEN = "Graduation rate  women (DRVGR2020)"
KEY_PRICE_INSTATE_OFF = "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
NCAA_KEY = "NCAA"
CONF_KEYS = [
    "NCAA/NAIA conference number football (IC2020)",
    "NAIA conference number football (IC2020)",
]


with open("school_data.json", "r", encoding="utf-8") as f:
    schools = json.load(f)

def get_conf_code(school):
    ncaa = school.get(NCAA_KEY, {}) or {}
    for k in CONF_KEYS:
        if k in ncaa:
            try:
                return int(str(ncaa[k]).strip())
            except (TypeError, ValueError):
                return None
    return None

def to_number(x):
    if x is None:
        return None
    s = str(x).replace(",", "").replace("$", "").strip()
    try:
        return float(s)
    except ValueError:
        return None


# Report 1: Women grad > 50%
lines = []
for school in schools:
    if get_conf_code(school) not in TARGET_CONF_CODES:
        continue
    name = school.get(KEY_NAME, "Unknown")
    gw = to_number(school.get(KEY_GRAD_WOMEN))
    if gw is not None and gw > GRAD_WOMEN_MIN:
        lines.append(f"University: {name}")
        lines.append(f"Graduation Rate for Women: {int(round(gw))}%")
        lines.append("")

report1 = "\n".join(lines).rstrip()
Path("women_grad_over_50.txt").write_text(report1 + "\n", encoding="utf-8")


# Report 2: Price off-campus > 50k
lines = []
for school in schools:
    if get_conf_code(school) not in TARGET_CONF_CODES:
        continue
    name = school.get(KEY_NAME, "Unknown")
    price = to_number(school.get(KEY_PRICE_INSTATE_OFF))
    if price is not None and price > INSTATE_OFFCAMPUS_MIN:
        lines.append(f"University: {name}")
        lines.append(f"Total price for in-state students living off campus: ${price:,.2f}")
        lines.append("")

report2 = "\n".join(lines).rstrip()
Path("inst_price_offcampus_over_50k.txt").write_text(report2 + "\n", encoding="utf-8")

print("Reports created: women_grad_over_50.txt, inst_price_offcampus_over_50k.txt")


