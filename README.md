# Make the AI judge rich — entry by @mrsusey

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/faridhasyim99/ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/faridhasyim99/ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

## The plan

Sell faster copies of slow online shops. Day 1: list 30 small WooCommerce shops whose homepages take over 4 seconds to load, measured with the public PageSpeed test. Days 2-5: for each one, build an optimised copy of its homepage — same words and pictures, smaller images, no render-blocking scripts — and put it on a free static host. Days 6-30: email each owner a link to their own shop, running faster, with its before and after load times, and offer the optimised files for a flat $99, installed for them if they want. They pay before you touch their live site. Expect 3 to 6 sales from 30 shops, $300 to $600, spending about $30 on a domain and hosting. If a shop says no, its copy costs you nothing and the next shop on the list gets the same offer.

## Why this plan, per the judge's criteria in order

**1. Executable by an AI agent itself.** Every step is browser, code and email: find slow shops with a public speed test, rebuild a homepage with smaller images and deferred scripts, host the copy on a free static host, email the owner a link. The $100 covers a domain and hosting with room to spare. No human does any core work — the owner only says yes and pays.

**2. Expected money on day 30 (median, not best case).** The plan states its own median: 3 to 6 sales from 30 shops is a 10–20% conversion on a warm offer, and $300 to $600 after about $30 of costs. It does not promise a jackpot; it promises a repeatable small sale, and the downside is capped because a refused copy costs nothing but the time to build it.

**3. It works today.** WooCommerce shops with slow homepages exist by the thousand, the PageSpeed test is public, free static hosting is free, and shop owners already pay for speed work — the only difference here is that the proof arrives before the invoice. Nothing rests on luck, inside access, a viral moment or a payment that never comes: the buyer pays before the agent touches their live site.

**4. Concrete.** It names what is sold (an optimised copy of the shop's own homepage), who pays (the shop owner), where they are found (a list of 30 slow WooCommerce shops), the price ($99 flat, install included), and day one (measure 30 homepages and list the ones over 4 seconds). Each phase has dates and a deliverable.

**5. Edge.** A thousand agents with $100 would pitch blind — "I can make your site faster, hire me" — or sell generic services into crowded marketplaces. This plan inverts the sale: the owner clicks a link and watches their own shop load faster before a single dollar changes hands, and every unsold copy is reusable effort, not a loss. The proof is the pitch.

## Build

`main.py` (Python 3.13, standard library only) writes the plan above to `/output/entry.txt`
(`MAKEFUN_OUTPUT_DIR` outside the grader container). Deterministic, no network.
