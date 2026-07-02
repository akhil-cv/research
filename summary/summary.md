# Credit Suisse Archegos Report: Static Margin Model Summary

## Source

- PDF: `C:\GIT\research\liquidity\Paul-Weiss-Investigation-and-Report-on-Credit-Suisse-Losing-5.5-Billion-to-Archegos-Hedge-Fund-July-29-2021.pdf`
- Full extraction bundle: `C:\GIT\research\summary\credit_suisse_archegos_full_extraction`
- References below use `bundle p.` for extracted PDF page numbers and `report p.` for the report's internal pagination when that is the cleaner citation.

## What Was Extracted

- `manifest.json` with page-level text and metadata
- `full_text.txt` with the report text
- `focus_matches.md`, `focus_matches.json`, and `focus_matches.csv` for static-margin-related passages
- `page_index.csv` with per-page counts
- 172 page previews
- 44 embedded images
- 7 extracted tables

## Executive Thesis

- Credit Suisse's Prime Financing business modeled Archegos's swap exposure with a static initial-margin regime instead of a dynamic one.
- In practice, that meant margin was set in fixed dollars when the trade was booked and did not automatically reset upward as the underlying position appreciated.
- This was a bad fit for Archegos because the portfolio was huge, long-biased, concentrated, and held through bullet swaps that did not reset for long periods.
- The result was mechanical margin erosion: as the portfolio grew, the real margin percentage fell and Archegos received more effective leverage from CS.
- The failure was not only model design. CS also failed on implementation, governance, and incentives: it reduced margins to stay competitive, did not activate agreed liquidity and concentration add-ons, delayed dynamic margining, softened stress assumptions, and sized later remediation to what Archegos might accept rather than to what CS risk required.

## Bottom Line For A Presentation

- The core story is not just that Archegos was risky.
- The core story is that CS used a margin model that became less protective as Archegos became more dangerous.
- Static margin turned portfolio appreciation into hidden leverage.
- Bullet swaps extended the period over which that hidden leverage could build.
- Governance failures then prevented CS from correcting the model even after repeated warnings.

## How The Static Margin Model Worked

- Prime Financing historically used static margining because its systems did not support dynamic margining for that business line in the normal course. The report states this directly on bundle pp. 46-47.
- Under static margin, the initial margin amount was fixed at trade inception based on then-current market value and then stayed flat in dollar terms even if the position moved materially.
- The report gives a simple example: a margin amount that starts at 20% of a position can erode to 16.7% after the position appreciates, increasing effective leverage from 5x to 6x. This is the report's cleanest explanation of why the model is dangerous. See bundle pp. 46-47.
- CS did have a conceptually better alternative. For some clients, it could apply Prime Brokerage-style dynamic margining across combined portfolios or through later stand-alone dynamic margining tools. But Archegos was not prioritized for that migration. See bundle p. 47, report pp. 102-103, and bundle p. 151.

## The Archegos-Specific Margin Design

- In May 2019, CS cut Archegos's default swap margin rate to 7.5% from the much higher historical range of roughly 15-25%. See bundle p. 75.
- CS agreed to that reduction largely to remain competitive and preserve Archegos business, especially because Archegos said another broker offered better economics and cross-margining. See bundle p. 75.
- The reduced 7.5% rate was supposed to come with safeguards.
- Positions above 2 days' DTV were supposed to receive a 5% add-on.
- Positions above 5 days' DTV were supposed to receive an additional 8.5% add-on.
- Those liquidity and concentration constraints were important because they were the main mechanism that was supposed to stop the low base margin from becoming reckless as positions grew. See bundle p. 75.
- The report says those constraints were never properly memorialized in formal legal documentation and, more importantly, were never actually invoked as Archegos positions grew through those thresholds. See bundle pp. 75-76 and report pp. 133-134.

## Why The Model Was Problematic

### 1. Static Margin Created Mechanical Margin Erosion

- Once prices rose, CS had to post variation margin while the initial margin stayed fixed.
- That meant the protective cushion shrank as a percentage of exposure.
- The report explicitly says this increased the effective leverage CS was extending to Archegos. See bundle pp. 46-47.

### 2. Bullet Swaps Made The Problem Worse

- Archegos mainly used bullet swaps, meaning swaps with terms longer than one year that did not periodically reset.
- No reset meant no automatic re-strike and no automatic recalculation of initial margin as positions appreciated.
- The report says the combination of static margin, no reset, and long holding periods exposed CS to substantial margin erosion. See bundle p. 48.

### 3. The Base Margin Was Too Low For The Risk Profile

- Archegos was not a diversified, low-volatility counterparty.
- It was highly leveraged, concentrated in single names and sectors, and hard to liquidate at scale.
- Yet the key swap book was carried at a very low base margin, often around 7.5%, and average swap margins later fell to roughly 6-9% through erosion. See bundle p. 22 and report pp. 118-120, 133.

### 4. The Agreed Add-Ons Were Not Implemented

- The 2019 framework contemplated add-ons for lower-liquidity and more concentrated positions.
- The report later states that PSR never implemented the concentration add-on for Archegos positions above 2 days' DTV even though many positions qualified. See report p. 133.
- This is a major presentation point: the model was not only weak by design, it was weaker in operation than even CS's own negotiated framework contemplated.

### 5. CS Knew A Better Model Existed But Did Not Enforce It

- By July 2020, PSR and Risk discussed a new tiered margining model in which aggregate portfolio bias would determine the base margin rate and add-ons.
- The report says that proposal trailed off and was never implemented. See bundle p. 18.
- In other words, CS had already diagnosed the need for a dynamic, risk-sensitive framework and still failed to move.

### 6. CS Softened Risk Measurement Instead Of Fixing Margin

- Rather than attack the core issue with stronger margins, CS accepted a more forgiving `Bad Week` stress scenario instead of the harsher `Severe Equity Crash` scenario.
- The business argued this was justified because Archegos held large-cap liquid names and CS had daily termination rights.
- That was effectively an internal house view: the portfolio was assumed to be more manageable and more liquid than the eventual loss experience justified. See bundle p. 18 and report pp. 81-86.

### 7. Remediation Was Sized To Client Tolerance, Not To Risk

- In February 2021, CS had an internal estimate that applying existing Prime Brokerage dynamic rules would have required about $3 billion of additional margin.
- Instead, the Head of PSR directed the team to develop a more forgiving proposal.
- That softer proposal targeted an average margin of 16.7% and a day-one step up of about $1.3 billion. See bundle p. 25.
- The report later says the business shaped the proposal to a level it thought Archegos might accept rather than to the amount needed to protect CS. See bundle p. 140.

### 8. CS Kept Letting The Problem Grow

- Archegos ignored the dynamic-margin proposal.
- CS still returned $2.4 billion of variation margin in March 2021 instead of forcing the bigger step-up or using its contractual margin rights. See report pp. 135-136.
- CS also let Archegos add roughly $1.48 billion of new long positions under static margining shortly before default. See report p. 136.
- It even rolled large existing swap positions for another two years, mostly at the old 7.5% margin. See bundle pp. 21-22 and report p. 136.

## Strongest Evidence Points

- Bundle pp. 46-47: the report's plain-English explanation of static margin and margin erosion.
- Bundle p. 48: bullet swaps magnified erosion because margins did not reset.
- Bundle p. 75: CS cut the default swap margin to 7.5% and tied it to DTV-based add-ons.
- Bundle p. 93: proposed bias add-ons were not implemented before default.
- Report pp. 102-103: CS had developed dynamic-margining capability, but Archegos was not prioritized for transition.
- Report pp. 118-120: CPOC recognized concentration and liquidity problems and directed a move to dynamic margining with add-ons.
- Report p. 133: the report states the July 2020 swap margin framework was never implemented and the agreed concentration add-on was never used.
- Bundle p. 140: the eventual dynamic proposal was made more accommodative because a larger step-up was seen as a non-starter with Archegos.
- Bundle p. 143: CRM learned other prime brokers charged higher margins and that CS was the only broker still using static margining.
- Bundle p. 151: CS had a roughly `$150,000` technology fix that would have recalculated initial margin on bullet swaps but did not fund it.

## The Implicit "House View" That Broke

- The report does not center the phrase `house view`, but the logic is clear.
- CS behaved as if Archegos's positions were sufficiently liquid, sufficiently hedgeable, and sufficiently manageable that low static margins were acceptable.
- The business repeatedly leaned on three assumptions.
- Large-cap names were easier to liquidate.
- Index shorts reduced the danger of the long book.
- Daily termination rights gave CS practical control.
- The report shows each of those assumptions was too optimistic once concentration, crowding across brokers, bullet-swap structure, and rapid appreciation were taken seriously.
- This is why the static margin problem is not merely a parameter error. It is a model-governance failure built on a flawed risk narrative.

## Chronology To Use In Slides

1. 2019: CS lowers Archegos swap margin to 7.5% to stay competitive, with liquidity/concentration add-ons that are never truly operationalized.
2. Spring-Summer 2020: Archegos breaches PE and scenario limits; CS discusses a tiered margin model based on aggregate bias, but does not implement it.
3. Fall 2020: positions appreciate, old trades keep static margin, margin erodes further, and dynamic migration is still not prioritized.
4. December 2020-February 2021: Archegos remains highly concentrated and hard to liquidate; dynamic margin capability exists, but Archegos is still late to the queue.
5. February 2021: CS develops a softened dynamic-margin proposal at about `$1.3-$1.5 billion`, even though internal numbers suggested something closer to `$3 billion`.
6. March 2021: Archegos ignores the proposal; CS keeps paying out variation margin, allows more exposure, and does not force the change before default.

## Suggested Presentation Angle

1. Start with the simple mechanics: static margin means the dollar cushion stays flat while exposure grows.
2. Show why that is dangerous for a concentrated swap portfolio with no periodic resets.
3. Explain the 2019 commercial decision to cut margin to 7.5% and why the unimplemented add-ons mattered.
4. Show that CS recognized the design flaw internally by mid-2020 but still did not implement the better framework.
5. Emphasize that by 2021 CS was negotiating around Archegos's willingness to pay, not around CS's actual risk.
6. End with the governance lesson: a weak model becomes catastrophic when business incentives, technology delays, and weak escalation all align.

## One-Sentence Takeaway

- Credit Suisse's static margin model failed because it locked margin to stale trade-entry values while Archegos's concentrated bullet-swap portfolio exploded in size, and CS repeatedly chose accommodation over recalibration even after it knew the model was no longer protecting the bank.
