# Communication and conversion rework

## Problem → design thinking → solution

The visual experience attracted attention but visitors lacked a clear personal reason to choose the ring, evidence to assess it and a coherent next step. We developed three proposed Singapore personas, mapped their objections to feature pages, and gave each route one primary conversion: create a personalised buying guide. The approved cinematic design remains. Search-led headings make the pages easier to identify, evidence and cost sections answer objections, and a short form produces a useful guide with the matching Shopee product. These personas are design hypotheses, not completed interview research. We must test them with representative users before claiming conversion improvements.

## Personas and journeys

| Persona | Demographic and lifestyle | Pain and Google search | Landing and objection | Exact answer and path |
|---|---|---|---|---|
| Michelle, 27 | Singapore marketing executive; segment 22–30; busy workdays, variable bedtimes | Wants context for inconsistent rest; “Oura Ring 4 sleep tracker Singapore” | Sleep; “Will this add anything beyond another score?” | Sleep's annotated example and “Will I learn anything beyond another score?” section → Technology evidence → Price & buying → Sleep-selected guide form → guide → matching Shopee listing |
| Daniel, 36 | Singapore product manager; segment 31–45; working parent and recreational runner, already owns a smartwatch | Balances work and training; “Oura readiness HRV recovery ring” | Recovery; “Why add a ring if I own a watch?” | Recovery objection answer plus Ring vs watch comparison of screen, overnight wear and workout needs → sizing → Recovery-selected guide → exact finish listing |
| Farid, 49 | Singapore facilities manager; segment 46–60; walks at work and wants discreet everyday tracking | Wants understandable movement trends without another screen; “smart ring fitness tracker Singapore” | Activity; “Why choose this instead of a fitness band?” | Activity everyday-movement example and format/limitations answer → Ring vs watch → membership and costs → Activity-selected guide → matching listing |

## Storytelling and page jobs

Overview makes the product memorable and lets visitors skip directly to needs. Sleep, Recovery and Activity answer a relevant personal problem. The Ring compares form factors. Technology and Research establish the limits of the evidence. Find your ring resolves finish and sizing doubts. Price & buying explains ownership cost and specific product destinations. The guide form connects interest, fit and product, then provides a downloadable next step. Privacy explains actual processing. Team, Sitemap and Project pitch support assessment transparency and navigation.

## SEO and supporting vocabulary

Every main page has an individual title (<60 characters), description (<155), canonical URL and one H1. Product pages use descriptive H2s, FAQs and internal links. The XML sitemap lists indexable content; team, privacy, HTML sitemap and pitch use noindex. FAQ JSON-LD matches visible questions and answers; it is descriptive structure, not a promised Google rich result. Google retired FAQ rich results in 2026. Rankings are not guaranteed.

| Page | Main search intent | Supporting vocabulary |
|---|---|---|
| Overview | Oura Ring 4 Singapore | smart ring Singapore, sleep tracker, recovery tracking, daily activity |
| The ring | Oura Ring 4 features | smart ring vs smartwatch, titanium ring, screenless wearable, overnight comfort |
| Sleep | Oura Ring 4 sleep tracker | estimated sleep stages, bedtime consistency, sleep duration, nightly patterns |
| Recovery | Oura Ring 4 readiness | recovery tracking, HRV trends, resting heart rate, personal baseline |
| Activity | Oura Ring 4 fitness tracking | daily movement, activity goals, fitness wearable, smartwatch comparison |
| Technology | Oura Ring 4 accuracy | optical sensors, Smart Sensing, temperature trends, research limitations |
| Find your ring | Oura Ring 4 sizes and colours | sizing kit, ring fit, silver finish, gold finish |
| Price & buying | Oura Ring 4 price Singapore | Oura membership, ownership cost, Shopee Singapore, size availability |
| Guide form | personalised Oura buying guide | sizing advice, launch voucher, free sizing kit, membership guidance |
| Research | Oura Ring 4 research | sensing evidence, manufacturer study, study limitations, product specifications |
| Privacy | buying-guide privacy policy | consent, retention, withdraw consent, marketing preference |
| Team | CS2024 project team | Singapore student project, research, copywriting, development |
| Sitemap | Oura Ring 4 sitemap | sizing, features, buying guide, recovery |
| Project pitch | Oura website project | personas, customer journey, conversion, SEO |

Exact title/meta/H1 text is reviewable in scripts/build_site.py. Alt text describes the artistic ring and explicitly illustrative charts; artwork is not described as a product photograph or real user data. No fabricated price/rating/availability is placed in structured data.

## Form decisions

Tracking interest selects the persona route. No email address is requested because this version has no email delivery service. Optional first name personalises the result; optional finish/size can be carried from the configurator. No address, phone, ID or health measurements are requested. Required request-processing consent and optional marketing consent are separate and unchecked. The guide works with marketing unchecked. The browser generates the guide, clears the email and does not make a live mailing subscription. The proposed S$20 voucher and sizing-kit support are subject to retailer approval and are not redeemable. Read the privacy page before enabling any live collection.

## Evaluation

Check all pages at 375px and desktop: navigation, heading wrapping, ring picker, comparison cards, form, illustration sizing and no horizontal overflow. Exercise all three guide priorities, missing request consent, optional marketing, preference transfer and correct product destination. Existing cinematic IDs and scripts are retained. Conversion and search gains require later user testing, actual analytics consent planning and real Search Console data; no uplift is claimed here.
