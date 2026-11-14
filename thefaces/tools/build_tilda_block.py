"""Builds tilda/04-menu-booking-builder.html from index.html.

The block holds the "Menu & prices + Your ritual" section (menu, salon choice,
WhatsApp / Altegio buttons and dataLayer events) so it can be pasted into a
Tilda T123 "HTML code" block. Run after editing index.html:

    python3 thefaces/tools/build_tilda_block.py
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf-8")

css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
# keep tokens, base buttons and the menu/builder/toast rules
keep_prefixes = (":root", ".wrap", ".eyebrow", ".h2", ".muted", ".btn", ".link", ".rv",
                 ".sec", ".menu", ".tabs", ".salon-switch", ".items", ".item", ".plus",
                 ".note", ".builder", ".bl", ".tot", ".step", ".choice", ".go", ".toast")
rules = re.findall(r"([^{}]+)\{([^{}]*)\}", re.sub(r"@media[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}", "", css))
out = []
for sel, body in rules:
    sel = sel.strip()
    if any(part.strip().startswith(keep_prefixes) for part in sel.split(",")):
        scoped = sel if sel.startswith(":root") else ",".join("#tf-booking " + p.strip() for p in sel.split(","))
        out.append(f"{scoped}{{{body}}}")
out.append("#tf-booking{font-family:Montserrat,Arial,sans-serif;font-weight:300;color:var(--text);line-height:1.6}"
           "#tf-booking *{box-sizing:border-box}#tf-booking button{font:inherit;background:none;border:0;cursor:pointer;color:inherit}"
           "#tf-booking .rv{opacity:1;transform:none}#tf-booking a{color:inherit;text-decoration:none}"
           "#tf-booking .btn{text-decoration:none}#tf-booking .toast a{border-bottom:1px solid}"
           "@media (max-width:1100px){#tf-booking .menu-layout{grid-template-columns:1fr}#tf-booking .builder{position:relative;top:0}}"
           "@media (max-width:820px){#tf-booking .sec-head{grid-template-columns:1fr}"
           "#tf-booking .item{grid-template-columns:1fr auto 44px;gap:10px 14px}"
           "#tf-booking .item .du{grid-column:1;grid-row:2}#tf-booking .item .pc{grid-column:2;grid-row:1}"
           "#tf-booking .item .plus{grid-column:3;grid-row:1/3}}")

section = re.search(r'(<section class="menu-sec sec" id="menu">.*?</section>)', src, re.S).group(1)
toast = re.search(r'(<div class="toast" id="toast".*?</div>)', src, re.S).group(1)
script = re.search(r"<script>(.*?)</script>", src, re.S).group(1)

block = f"""<!-- THE FACES · Menu & prices + Your ritual (booking builder)
     Paste into a Tilda T123 block. Generated from thefaces/index.html by tools/build_tilda_block.py -->
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500;600&display=swap" rel="stylesheet">
<style>
{chr(10).join(out)}
</style>
<div id="tf-booking">
{section}
{toast}
</div>
<script>
(function(){{
{script}
}})();
</script>
"""
dest = root / "tilda" / "04-menu-booking-builder.html"
dest.parent.mkdir(exist_ok=True)
dest.write_text(block, encoding="utf-8")
print(dest, len(block), "bytes")
