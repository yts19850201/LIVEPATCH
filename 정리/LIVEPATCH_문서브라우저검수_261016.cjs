const fs=require('node:fs');const path=require('node:path');const {pathToFileURL}=require('node:url');
const {chromium}=require('C:/Users/User/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const root=path.resolve(__dirname,'..');const results={};
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1000}});const errors=[];
  page.on('pageerror',error=>errors.push(error.message));
  await page.route('https://**/*',route=>route.abort());
  await page.goto(pathToFileURL(path.join(root,'LIVEPATCH_사업기획서.html')).href);
  results.master=await page.evaluate(()=>({title:document.title,chapter27:!!document.getElementById('sec27'),missingAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.getAttribute('href').slice(1))).map(a=>a.getAttribute('href')),brokenImages:[...document.images].filter(i=>i.complete&&!i.naturalWidth).length}));
  await page.screenshot({path:path.join(__dirname,'LIVEPATCH_통합명세열람검수_261016.png')});
  await page.goto(pathToFileURL(path.join(root,'LIVEPATCH_v5.6_화면목업.html')).href+'#C13');
  await page.locator('#chips button[data-f="alpha"]').click();results.mvpFilter=await page.locator('.g-item').count();
  await page.locator('#chips button[data-f="embedded"]').click();results.embeddedFilter=await page.locator('.g-item').count();
  await page.locator('#chips button[data-f="later"]').click();results.laterFilter=await page.locator('.g-item').count();
  results.mockup=await page.evaluate(()=>({templates:document.querySelectorAll('template[id^="t-"]').length,title:document.getElementById('ttl').textContent,cta:document.getElementById('gc').textContent}));
  results.errors=errors;
  if(results.mvpFilter!==63||results.embeddedFilter!==58||results.laterFilter!==52||results.master.missingAnchors.length||errors.length)throw Error(JSON.stringify(results));
  fs.writeFileSync(path.join(__dirname,'LIVEPATCH_브라우저검수결과_261016.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results));
 }finally{await browser.close();}
})().catch(e=>{console.error(e.message);process.exitCode=1});
