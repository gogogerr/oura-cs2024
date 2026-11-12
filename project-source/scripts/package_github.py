#!/usr/bin/env python3
"""Create a simple branch/root GitHub Pages upload with full editable source."""
from pathlib import Path
import argparse, json, shutil, subprocess, sys, tempfile, zipfile
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--base-url',default='https://gogogerr.github.io/cs2024-oura');args=p.parse_args()
with tempfile.TemporaryDirectory(prefix='oura-github-') as td:
 staging=Path(td)/'Oura-GitHub-Upload';project=staging/'project-source';project.mkdir(parents=True)
 for folder in ['dist','src','scripts','docs','qa']:
  shutil.copytree(ROOT/folder,project/folder,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.png','*.jpg'))
 config=json.loads((ROOT/'site.config.json').read_text());config['base_url']=args.base_url.rstrip('/')
 (project/'site.config.json').write_text(json.dumps(config,indent=2)+'\n')
 shutil.copy2(ROOT/'README.md',project/'README.md')
 subprocess.run([sys.executable,str(project/'scripts/build_site.py'),'--base-url',args.base_url],check=True)
 subprocess.run([sys.executable,str(project/'qa/check_source.py')],check=True)
 for item in (project/'dist').iterdir():
  if item.is_dir():shutil.copytree(item,staging/item.name)
  else:shutil.copy2(item,staging/item.name)
 (staging/'README.md').write_text('''# Oura Ring 4 — CS2024 website\n\nThis package publishes directly from the repository root. No hidden workflow folder, package installation or custom build is required.\n\n1. Upload all contents of Oura-GitHub-Upload into the existing gogogerr/cs2024-oura repository. index.html must appear beside assets and project-source at the top level. Upload extracted files, not the ZIP.\n2. Commit changes to main.\n3. Open Settings → Pages. Choose Deploy from a branch, then main and /(root). Save.\n4. Use Visit site when GitHub Pages finishes publishing. Expected address: https://gogogerr.github.io/cs2024-oura/\n\nComplete editable HTML, CSS and JavaScript are at the root and in assets. The generator, original templates, research/planning documents, complete generated site and QA scripts are preserved in project-source. Do not mix this branch/root method with the older GitHub Actions instructions in project-source/README.md.\n\n## Local preview\nRun python3 -m http.server 8000 in this folder, then visit http://localhost:8000/. Opening index.html directly also supports the buildless scripts. No form submissions are transmitted.\n\n## Rebuild after editing the generator\nRun python3 scripts/package_github.py from the original project. The full-source download also contains the optional Actions-based publishing setup.\n\n## Before assessment submission\nTeam roles are confirmed and the group-number line has been removed as requested. The PPTX reflects the current persona and conversion changes. Verify the live website on actual phones. Offer terms are project placeholders. Submit the published website link plus PowerPoint through NTULearn as directed in the brief.\n''')
 output=ROOT/'Oura-GitHub-Upload.zip'
 with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
  for f in sorted(staging.rglob('*')):
   if f.is_file():z.write(f,'Oura-GitHub-Upload/'+f.relative_to(staging).as_posix())
 print(f'Created {output.name}: {len(list(staging.rglob("*")))} entries; index.html at upload root.')
