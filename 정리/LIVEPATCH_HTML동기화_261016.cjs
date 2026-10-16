const fs = require('node:fs');
const path = require('node:path');
const {marked, Renderer} = require('C:/Users/User/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/marked');
const root=path.resolve(__dirname,'..');
const md=fs.readFileSync(path.join(root,'LIVEPATCH_사업기획서.md'),'utf8');
const safe=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const toc=[];const used=new Set([...md.matchAll(/\bid=["']([^"']+)/g)].map(x=>x[1]));const renderer=new Renderer();
renderer.heading=function(token){
  const text=this.parser.parseInline(token.tokens);
  const plain=token.text.replace(/<[^>]*>/g,'').replace(/[`*]/g,'');
  const match=plain.match(/^(\d+(?:[-.]\d+)*(?:-앞)?)[.\s]/);
  let id=match?'sec'+match[1].replaceAll('.','-'):'heading-'+toc.length+'-'+used.size;
  while(used.has(id))id+='-next'; used.add(id);
  const screen=plain.match(/^([MCAO]\d{2})\s/);let alias='';
  if(screen&&!used.has(screen[1].toLowerCase())){const target=screen[1].toLowerCase();used.add(target);alias=`<span id="${target}"></span>`;}
  if(token.depth===2)toc.push({id,title:plain});
  return `${alias}<h${token.depth} id="${safe(id)}">${text}</h${token.depth}>\n`;
};
// 한국어 조사와 붙은 굵은 글씨도 안정적으로 표시한다. 코드 블록은 보존한다.
let inFence=false;
const renderSource=md.split('\n').map(line=>{
 if(/^\s*```/.test(line)){inFence=!inFence;return line;}
 return inFence?line:line.replace(/\*\*([^*\n]+)\*\*/g,'<strong>$1</strong>');
}).join('\n');
const body=marked.parse(renderSource,{gfm:true,breaks:false,renderer});
const page=`<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>LIVEPATCH v5.7 출시 MVP와 통합 명세</title><style>
:root{color-scheme:light;--ink:#171717;--muted:#525252;--line:#e5e5e5;--primary:#2563eb}
*{box-sizing:border-box}body{margin:0;background:#fafafa;color:var(--ink);font:15px/1.75 "Malgun Gothic",system-ui,sans-serif;word-break:keep-all;overflow-wrap:anywhere}
aside{position:fixed;left:0;top:0;bottom:0;width:272px;padding:24px 18px;background:#fff;border-right:1px solid var(--line);overflow:auto}
aside strong{display:block;margin-bottom:12px;font-size:19px}aside a{display:block;padding:7px 8px;color:var(--muted);text-decoration:none;font-size:12px;border-radius:5px}aside a:hover,aside a:focus{background:#eff6ff;color:var(--primary)}
main{margin-left:272px;padding:40px 48px;max-width:1560px}header{padding:18px 24px;border:1px solid var(--line);background:#fff;border-radius:12px;margin-bottom:28px}header a{color:var(--primary)}
h1{font-size:30px}h2{font-size:24px;margin-top:56px;border-top:1px solid var(--line);padding-top:24px}h3{font-size:19px;margin-top:32px}h4{font-size:16px;margin-top:24px}h1,h2,h3,h4{scroll-margin-top:24px;line-height:1.5}p,li{max-width:1120px}
a{color:#1d4ed8}a:focus-visible,summary:focus-visible{outline:3px solid #2563eb;outline-offset:3px}table{display:block;overflow:auto;border-collapse:collapse;font-size:12px;margin:20px 0;width:100%;background:white}th,td{padding:10px 12px;border:1px solid var(--line);vertical-align:top;min-width:110px;max-width:480px}th{background:#f5f5f5;text-align:left}blockquote{margin:18px 0;padding:12px 20px;background:#f5f5f5;border-left:3px solid #737373}blockquote p{margin:6px 0}
pre{overflow:auto;background:#171717;color:white;border-radius:8px;padding:18px;font:12px/1.6 Consolas,monospace}code{font-family:Consolas,monospace;font-size:.92em}img{max-width:100%;height:auto;border:1px solid var(--line);border-radius:8px}hr{border:0;border-top:1px solid var(--line);margin:32px 0}input[type=checkbox]{pointer-events:none}
.status{display:flex;gap:10px;flex-wrap:wrap}.status span{background:#f5f5f5;padding:5px 10px;border-radius:5px;font-size:13px}
@media(max-width:900px){aside{position:static;width:auto;height:auto;max-height:240px;border-right:0;border-bottom:1px solid var(--line)}main{margin:0;padding:24px 16px}h1{font-size:25px}h2{font-size:21px}}
@media print{aside{display:none}main{margin:0;padding:0}h2{break-before:page}table{display:table;font-size:9px}img{max-height:600px;object-fit:contain}}
</style></head><body><aside><strong>LIVEPATCH v5.7</strong><a href="#sec27">현재 MVP와 Figma 작업 순서</a>${toc.map(x=>`<a href="#${safe(x.id)}">${safe(x.title)}</a>`).join('')}</aside>
<main><header><div class="status"><span>44페이지 + 19공용 오버레이</span><span>58개 ID 내부 통합</span><span>52개 ID 후속</span></div><p>현재 기준은 <a href="#sec27">27장</a>입니다. JSON v5.7에서 필드 명세와 체크리스트를 동기화했습니다. 이전 PNG는 참고 스냅샷이며 구현·검수 완료 증거가 아닙니다.</p></header>${body}</main></body></html>`;
fs.writeFileSync(path.join(root,'LIVEPATCH_사업기획서.html'),page,'utf8');
console.log(JSON.stringify({sections:toc.length,bytes:Buffer.byteLength(page),source:'LIVEPATCH_사업기획서.md',output:'LIVEPATCH_사업기획서.html'}));
