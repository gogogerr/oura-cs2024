# Oura Ring 4 — CS2024 website

This package publishes directly from the repository root. No hidden workflow folder, package installation or custom build is required.

1. Upload all contents of Oura-GitHub-Upload into the existing gogogerr/cs2024-oura repository. index.html must appear beside assets and project-source at the top level. Upload extracted files, not the ZIP.
2. Commit changes to main.
3. Open Settings → Pages. Choose Deploy from a branch, then main and /(root). Save.
4. Use Visit site when GitHub Pages finishes publishing. Expected address: https://gogogerr.github.io/cs2024-oura/

Complete editable HTML, CSS and JavaScript are at the root and in assets. The generator, original templates, research/planning documents, complete generated site and QA scripts are preserved in project-source. Do not mix this branch/root method with the older GitHub Actions instructions in project-source/README.md.

## Local preview
Run python3 -m http.server 8000 in this folder, then visit http://localhost:8000/. Opening index.html directly also supports the buildless scripts. No form submissions are transmitted.

## Rebuild after editing the generator
Run python3 scripts/package_github.py from the original project. The full-source download also contains the optional Actions-based publishing setup.

## Before assessment submission
Team roles are confirmed and the group-number line has been removed as requested. The PPTX reflects the current persona and conversion changes. Verify the live website on actual phones. Offer terms are project placeholders. Submit the published website link plus PowerPoint through NTULearn as directed in the brief.
