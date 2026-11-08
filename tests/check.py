# -*- coding: utf-8 -*-
"""Diagram regression suite. Run after ANY change to the diagram section.
   python tests/check.py            -> full report
   python tests/check.py --quick    -> failures only
"""
import os, sys, pathlib, json
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL  = (ROOT/'forearm_mass_anatomy.html').as_uri()
PLATES = ['palmar_sup','palmar_deep','dorsal_sup','dorsal_deep']
EXPECT = {'palmar_sup':6,'palmar_deep':3,'dorsal_sup':10,'dorsal_deep':7}

R=[]
def check(ok, name, detail=''):
    R.append((bool(ok), name, detail))

def main():
    with sync_playwright() as p:
        channel=os.environ.get('PLAYWRIGHT_CHANNEL','chrome')
        br=p.chromium.launch() if channel=='chromium' else p.chromium.launch(channel=channel)
        pg=br.new_page(viewport={'width':1500,'height':1100})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto(URL); pg.wait_for_timeout(600)

        # T1 no js errors
        check(not errs,'T1 no JavaScript errors', '; '.join(errs))

        # T2 all four views exist
        for pl in PLATES:
            n=pg.eval_on_selector_all('#view-%s'%pl,'els=>els.length')
            check(n==1,'T2 view exists: %s'%pl,'found %d'%n)

        # T3 same mechanism on all four: bitmap base + per-muscle reveal group
        for pl in PLATES:
            img=pg.eval_on_selector_all('#view-%s img'%pl,'e=>e.length')
            mg =pg.eval_on_selector_all('#view-%s .mg'%pl,'e=>e.length')
            sv =pg.eval_on_selector_all('#view-%s svg.ov'%pl,'e=>e.length')
            check(img==1 and mg==EXPECT[pl] and sv==1,
                  'T3 mechanism complete: %s'%pl,'img=%d mg=%d svg=%d (want 1/%d/1)'%(img,mg,sv,EXPECT[pl]))

        # T4 label count matches muscle count on every view
        for pl in PLATES:
            t=pg.eval_on_selector_all('#view-%s .tag'%pl,'e=>e.length')
            check(t==EXPECT[pl],'T4 label count: %s'%pl,'tags=%d want %d'%(t,EXPECT[pl]))

        def show(pl):
            pg.click('#tb-'+pl); pg.wait_for_timeout(180)

        # T5 hover a label -> exactly its muscle lights, others off
        for pl in PLATES:
            show(pl)
            for i in range(EXPECT[pl]):
                pg.eval_on_selector_all('.mg','e=>e.forEach(x=>x.classList.remove("on"))')
                pg.hover('#tg-%s-%d'%(pl,i)); pg.wait_for_timeout(120)
                on=pg.evaluate("()=>[...document.querySelectorAll('.mg.on')].map(e=>e.id)")
                check(on==['mg-%s-%d'%(pl,i)],'T5a hover label lights its muscle: %s-%d'%(pl,i),str(on))

        # T6 hover the muscle -> its own label activates
        for pl in PLATES:
            show(pl)
            for i in range(EXPECT[pl]):
                box=pg.evaluate("""(a)=>{const [pl,i]=a;
                    const me=document.getElementById('hit-'+pl+'-'+i); if(!me) return null;
                    const others=[...document.querySelectorAll('#view-'+pl+' .hitp')].filter(e=>e!==me);
                    const rMe=me.getBoundingClientRect();
                    const pt=(x,y)=>({x,y});
                    // pick a point inside this polygon that no other polygon covers
                    const el=document.elementFromPoint(rMe.x+rMe.width/2, rMe.y+rMe.height/2);
                    const cand=[[rMe.x+rMe.width/2,rMe.y+rMe.height/2]];
                    for(let fx=0.2;fx<=0.8;fx+=0.1)for(let fy=0.2;fy<=0.8;fy+=0.1)
                        cand.push([rMe.x+rMe.width*fx, rMe.y+rMe.height*fy]);
                    for(const [x,y] of cand){
                      const e=document.elementFromPoint(x,y);
                      if(e===me) return {x,y};
                    }
                    return {x:rMe.x+rMe.width/2,y:rMe.y+rMe.height/2};}""",[pl,i])
                if not box:
                    check(False,'T6 hover muscle activates label: %s-%d'%(pl,i),'no hit area'); continue
                pg.mouse.move(4,4); pg.wait_for_timeout(40)
                pg.mouse.move(box['x'],box['y']); pg.wait_for_timeout(120)
                act=pg.evaluate("()=>[...document.querySelectorAll('.tag.act')].map(e=>e.id)")
                check('tg-%s-%d'%(pl,i) in act,'T6 hover muscle activates label: %s-%d'%(pl,i),str(act))

        # T7 reveal follows the muscle, not a box: mask is a polygon/path, not rect
        for pl in PLATES:
            shapes=pg.evaluate("""(pl)=>[...document.querySelectorAll('#view-'+pl+' .mg')].map(g=>{
                 const m=g.querySelector('.mask, polygon, path'); 
                 return m? m.tagName.toLowerCase():null;})""",pl)
            ok=all(s in ('polygon','path') for s in shapes) and len(shapes)==EXPECT[pl]
            check(ok,'T7 reveal is muscle-shaped, not a box: %s'%pl,str(shapes[:4]))

        # T8 clicking a muscle loads the inspector with that muscle's name
        names=pg.evaluate(r"""()=>{const o={};
                 document.querySelectorAll('.tag').forEach(t=>{
                   const m=t.id.match(/^tg-(.+)-(\d+)$/); if(!m) return;
                   const sp=t.querySelector('span:nth-child(2)')||t;
                   o[m[1]+'-'+m[2]]=sp.textContent.trim();});
                 return o;}""")
        for pl in PLATES:
            show(pl)
            for i in range(EXPECT[pl]):
                okc=pg.evaluate("""(a)=>{const el=document.getElementById('hit-'+a[0]+'-'+a[1]);
                    if(!el) return false;
                    el.dispatchEvent(new MouseEvent('click',{bubbles:true})); return true;}""",[pl,i])
                if not okc:
                    check(False,'T8 click loads inspector: %s-%d'%(pl,i),'no clickable muscle group'); continue
                pg.wait_for_timeout(60)
                got=pg.evaluate("()=>document.getElementById('card-name').textContent")
                want=names['%s-%d'%(pl,i)]
                check(got.lower().startswith(want.split('(')[0].strip().lower()),
                      'T8 click loads inspector: %s-%d'%(pl,i),'got "%s" want "%s"'%(got,want))

        # T9 leader lines have no fill (no dark triangles)
        fills=pg.evaluate("""()=>[...document.querySelectorAll('.leader-line,.ll')]
                 .map(e=>getComputedStyle(e).fill)""")
        check(all(f in ('none','rgba(0, 0, 0, 0)') for f in fills),'T9 leaders are unfilled lines',str(set(fills)))

        # T10 tags are ranked and do not overlap each other
        for pl in PLATES:
            ranks=pg.evaluate("""(pl)=>[...document.querySelectorAll('#view-'+pl+' .tag .rank')]
                     .map(e=>e.textContent.trim())""",pl)
            check(len(ranks)==EXPECT[pl] and all(r.startswith('#') for r in ranks),
                  'T10 every tag shows a rank: %s'%pl,str(ranks))
            ov=pg.evaluate("""(pl)=>{const b=[...document.querySelectorAll('#view-'+pl+' .tag')]
                     .map(e=>e.getBoundingClientRect());let n=0;
                     for(let i=0;i<b.length;i++)for(let j=i+1;j<b.length;j++){
                       const A=b[i],B=b[j];
                       if(A.left<B.right-2&&B.left<A.right-2&&A.top<B.bottom-2&&B.top<A.bottom-2)n++;}
                     return n;}""",pl)
            check(ov==0,'T11 tags do not overlap: %s'%pl,'%d overlaps'%ov)

        # T12 anatomy is an illustration, not robotic primitives: the base image must exist and carry detail
        for pl in PLATES:
            ok=pg.evaluate("""(pl)=>{const i=document.querySelector('#view-'+pl+' img');
                 return !!(i && i.naturalWidth>800);}""",pl)
            check(ok,'T12 realistic artwork present: %s'%pl)

        br.close()

    fails=[r for r in R if not r[0]]
    quick='--quick' in sys.argv
    for ok,name,detail in R:
        if ok and quick: continue
        print(('PASS ' if ok else 'FAIL ')+name+(('   ['+detail+']') if detail and not ok else ''))
    print('\n%d/%d passed, %d failed'%(len(R)-len(fails),len(R),len(fails)))
    return 1 if fails else 0

if __name__=='__main__':
    sys.exit(main())
