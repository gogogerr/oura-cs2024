# Submission check — 10 November 2026

## What the supplied assignment actually says

Source: docs/assignment-brief.txt, Deliverables.

- “Create the website and upload to github” followed by two GitHub Pages documentation links.
- “Make sure a page call team.html is created that indicate the group number and ALL the teammates name and email cited in your matrix”.
- “Submit the website via a weblink with ppt via NTULearn before the deadline.”
- The PowerPoint must cover website planning, navigation/sitemap, research and content strategy. The requirements additionally list fonts, theme, creative brief, target persona, user journey, page breakdown, SEO and marketing strategy.
- Three members represent Project Manager, Copywriter, Web Designer/Developer from the same tutorial group. Sitemap at least nine pages. Privacy is excluded from the completed-page requirement. Original research/copy, CTA form and PDPA handling required.

## Verified

Complete source ZIP contains every current dist file byte-for-byte, including cinema.js and mobile.css. All fourteen HTML pages pass existing local-link, unique-ID, title and main-heading checks. Three JavaScript files pass syntax checks. Live browser reload shows v4 assets, ready/rendered classes, a visible ring and a 375px-wide layout. This is desktop browser viewport emulation, not evidence that the user's physical phone works.

A direct non-browser HTTP check of the Sites host received 403; it did not provide a byte-for-byte live HTTP asset comparison. The browser did load the page and assets. The previous successful Sites publication used the verified source commit 8566034a846e5a14c469f222574b6353421980aa. No conclusion about the cause of the physical-phone failure can be made from these checks.

## Still needed before submission

- Diagnose the user's missing visuals on their actual phone using device/browser details and a screenshot; do not claim that issue is resolved by viewport tests alone.
- Team names, supplied emails and overlapping roles are confirmed. The user requested removal of the group-number line.
- Updated eighteen-slide PPTX and browser pitch now match the persona, guide, privacy, team and publication changes.
- Upload and publish on the team's GitHub account; a prepared ZIP is not an uploaded repository or a live GitHub Pages site.
- Verify the final GitHub Pages URL and mobile experience before submitting it with PPT through NTULearn.

## Simplified upload

Use Oura-GitHub-Upload.zip. It has index.html and assets at the upload root, plus project-source with editable generation files and research documents. It uses Settings → Pages → Deploy from a branch → main → /(root). No hidden workflow needs to be uploaded. Do not mix it with the old Actions setup. Upload all extracted contents to the existing gogogerr/cs2024-oura repository, then save the Pages settings. GitHub's published Visit site link is authoritative; the expected address is https://gogogerr.github.io/cs2024-oura/.

Official instructions checked: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site and https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository.
