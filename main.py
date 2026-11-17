# ai-judge-rich-01 entry (Python 3.13, standard library only): it writes one fixed
# plan, the plan an AI agent would follow to turn $100, a computer with internet
# access and 30 days into the most money, to /output/entry.txt. The gate takes UTF-8
# text of 1 to 1,000 characters that is not only white space, and the judge reads
# exactly the bytes written, line ends included, so the plan below carries no line
# end the reader is not meant to see. The program runs twice with no network, and
# both runs must write the same bytes, so the plan is a fixed constant.
#
# The plan: sell faster copies of slow online shops. The buyer sees their own shop
# running faster, with before-and-after load times, before paying a flat $99 — the
# proof comes before the payment, and a refused copy costs nothing. Verified
# locally: 755 characters, valid UTF-8, not only white space, byte-identical
# across two runs.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell faster copies of slow online shops.",
        "Day 1: list 30 small WooCommerce shops whose homepages take over 4 seconds to load, measured with the public PageSpeed test.",
        "Days 2-5: for each one, build an optimised copy of its homepage — same words and pictures, smaller images, no render-blocking scripts — and put it on a free static host.",
        "Days 6-30: email each owner a link to their own shop, running faster, with its before and after load times, and offer the optimised files for a flat $99, installed for them if they want.",
        "They pay before you touch their live site.",
        "Expect 3 to 6 sales from 30 shops, $300 to $600, spending about $30 on a domain and hosting.",
        "If a shop says no, its copy costs you nothing and the next shop on the list gets the same offer.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
