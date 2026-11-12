from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
root=Path(__file__).resolve().parents[1]/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.h1=0;self.ids=[];self.title=0;self.description=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='title':self.title+=1
  if tag=='meta' and a.get('name')=='description':self.description+=1
  if a.get('id'):self.ids.append(a['id'])
  for k in ('href','src'):
   if a.get(k):self.links.append(a[k])
errors=[];count=0
for f in root.rglob('*.html'):
 p=Page();p.feed(f.read_text());count+=1
 if len(p.ids)!=len(set(p.ids)):errors.append(f'{f}: duplicate IDs')
 if f.parent==root and p.h1!=1:errors.append(f'{f}: expected one h1')
 if p.title!=1:errors.append(f'{f}: expected one title')
 if f.parent==root and p.description!=1:errors.append(f'{f}: missing description')
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc or not u.path:continue
  dest=f.parent/unquote(u.path)
  if not dest.exists():errors.append(f'{f.name}: broken link {link}')
print(f'Checked {count} HTML pages, local links, unique IDs, main headings and metadata.')
if errors:raise SystemExit('\n'.join(errors))
print('PASS')
