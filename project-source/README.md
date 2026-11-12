# Oura Ring 4 — CS2024 website

Complete static source for the Form / Function student project. HTML, CSS and plain JavaScript; no paid services, API keys, npm packages or private assets are required to run the website.

## View locally

1. Download and unzip `Oura-CS2024-source.zip`.
2. Open `dist/index.html` in a browser. For the best preview, use a local server instead:

```sh
python3 -m http.server 8000
```

Visit **http://localhost:8000/dist/index.html**. Python is only needed for this optional server and rebuilding pages. The published website itself needs no Python.

## Publish on your GitHub account

1. Create a repository and upload the extracted project contents, including the hidden `.github` folder. Keep the `dist`, `src`, `scripts` and `docs` folders together.
2. Use `main` as the branch.
3. In repository **Settings → Pages → Build and deployment → Source**, choose **GitHub Actions**.
4. Open **Actions → Publish GitHub Pages → Run workflow** (or push a change). The included workflow publishes `dist` and automatically rebuilds the canonical URLs for your GitHub Pages address.
5. Open the Pages link shown by the successful workflow.

Do not upload this ZIP as the website itself: upload its extracted contents. If using a branch-based Pages setup instead, copy the contents of `dist` to that branch's root and set Pages to that root. Rebuild with your public URL before doing so.

## Edit the project

- `dist/`: complete ready-to-run website, all fourteen HTML pages and assets.
- `scripts/build_site.py`: editable page copy, titles, descriptions, navigation, FAQs and product mapping. Python 3.10+; standard library only.
- `src/home-cinema.html`: preserved original animated homepage structure.
- `src/project-pitch.html`: original pitch page template.
- `dist/assets/cinema.js` and `cinema.css`: original WebGL ring, scroll scenes and falling-ring toy.
- `dist/assets/app.js` and `style.css`: shared design and supporting-page ring renderer.
- `dist/assets/mobile.css`: dedicated phone scene composition and touch controls.
- `dist/assets/conversion.js` and `conversion.css`: personalised guide, responsive conversion components and preference transfer.
- `site.config.json`: public URL, project offer placeholders, group number and privacy contact.
- `docs/product-links.json`: recovered product destinations and verification limits.
- `docs/conversion-plan.md`: personas, journeys, keyword map and presentation explanation.
- `dist/docs/Oura-CS2024-Pitch.pptx`: existing assessment pitch deck. The eighteen-slide deck and online pitch use the current persona, guide, privacy, team and publication content.

After editing the generator, templates or configuration:

```sh
python3 scripts/build_site.py
python3 qa/check_source.py
```

For another host:

```sh
python3 scripts/build_site.py --base-url https://YOUR-USERNAME.github.io/YOUR-REPOSITORY
```

The generator is repeatable. Direct changes to generated HTML are overwritten when rebuilding. Direct CSS/JS edits are retained.

## What the form actually does

The form creates a personalised, downloadable text guide in the current browser. It carries Sleep / Recovery / Activity, finish and optional size to the guide and matching Ring 4 Shopee listing. Request consent is required; marketing consent is separate, optional and unticked. No email address is requested. An optional name and selected preferences personalise the guide in this browser only. No cookies, submission database, browser storage, emails, mailing subscriptions, orders or payments are created. The privacy page describes this behaviour. The guide download uses the browser's normal download function; allow downloads if prompted.

The proposed S$20 voucher and sizing-kit support are a campaign concept subject to retailer approval; no code, expiry, entitlement or delivery promise is invented. Do not represent these as redeemable offers or activate collection without implementing the necessary service and updating the privacy notice.

## Remaining team inputs

Team roles are confirmed in site.config.json and team.html. No group-number line is displayed, as requested. The project contact is Alger Goh at agoh039@e.ntu.edu.sg. Confirm an accountable operator and service arrangements before enabling live enquiries. Student ID numbers are intentionally excluded from the public pages. School emails were supplied by the team for assessment identification.

## Accuracy and ownership

Wellness information is not medical diagnosis. No invented reviews, sales data, stock, retail price or warranty promises are used. Shopee listing identity is mapped to each finish; live availability and seller terms must be confirmed on Shopee. Ring 5 catalog links are separated from Ring 4 and use their own generation's sizing kit. See the Research page and product-link file for limitations.

All ring illustrations, shaders, charts and animations are included as original project code. Oura product names and marks belong to their respective owner. This independent student concept is not affiliated with Oura or OURA SG. Source is supplied for the team's coursework and modification; no third-party brand rights are granted.
