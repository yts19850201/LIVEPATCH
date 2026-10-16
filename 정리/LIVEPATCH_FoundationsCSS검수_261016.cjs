const fs=require('node:fs');const path=require('node:path');
const {chromium}=require('C:/Users/User/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const root=path.resolve(__dirname,'..');const css=fs.readFileSync(path.join(root,'src/styles/design-tokens.css'),'utf8');
 const defined=new Set([...css.matchAll(/(--[a-z0-9-]+)\s*:/g)].map(x=>x[1]));const unresolved=[...css.matchAll(/var\((--[a-z0-9-]+)/g)].map(x=>x[1]).filter(x=>!defined.has(x));
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 try{const page=await browser.newPage({viewport:{width:1920,height:1080}});await page.setContent('<style>body{margin:0}</style><section id="outside"><h1>고객 사이트 제목</h1><p class="eyebrow">원래 안내</p><div class="container">원래 컨테이너</div><img></section><main data-livepatch-app><div class="container" id="container"><h1 id="h1">사이트 선택</h1><h2 id="h2">변경 확인</h2><p class="lp-caption" id="caption">예약 크레딧</p><p class="eyebrow" id="muted">미리보기에서는 예약만 합니다.</p></div></main>');
 const getOutside=()=>page.evaluate(()=>[...document.querySelectorAll('#outside,#outside *')].map(n=>{const s=getComputedStyle(n);return [n.tagName,s.color,s.fontSize,s.margin,s.display,s.boxSizing,s.width].join('|')}));
 const before=await getOutside();await page.addStyleTag({content:css});const after=await getOutside();
 const actual=await page.evaluate(()=>{const app=document.querySelector('[data-livepatch-app]');const a=getComputedStyle(app);const get=id=>{const s=getComputedStyle(document.getElementById(id));return {fontSize:s.fontSize,lineHeight:s.lineHeight,fontWeight:s.fontWeight,color:s.color,width:s.width}};return {primary:a.getPropertyValue('--project-primary').trim(),studioBar:a.getPropertyValue('--studio-topbar-height').trim(),container:get('container'),h1:get('h1'),h2:get('h2'),caption:get('caption'),muted:get('muted')}});
 const result={unresolvedVariables:unresolved,outsideUnchanged:JSON.stringify(before)===JSON.stringify(after),actual};
 if(unresolved.length||!result.outsideUnchanged||actual.container.width!=='1440px'||actual.h1.fontSize!=='32px'||actual.h1.lineHeight!=='42px'||actual.h2.fontWeight!=='600'||actual.caption.fontSize!=='13px'||actual.muted.color!=='rgb(85, 92, 102)')throw Error(JSON.stringify(result));
 fs.writeFileSync(path.join(__dirname,'LIVEPATCH_FoundationsCSS검수결과_261016.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result));
 }finally{await browser.close();}
})().catch(e=>{console.error(e.message);process.exitCode=1;});
