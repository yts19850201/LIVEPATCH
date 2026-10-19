//FIGMA_ROLLBACK_IOS26
await figma.setCurrentPageAsync(await figma.getNodeByIdAsync('21:60'));
await Promise.all(['Regular','Medium','SemiBold','Bold'].map(style=>figma.loadFontAsync({family:'Pretendard',style})));
const mutated=[],ids=['70:1886','70:2025','70:2164','70:2317','72:1314','72:1450'];
const vars=await figma.variables.getLocalVariablesAsync(),map=new Map(vars.map(v=>[v.id,v])),byName=new Map(vars.map(v=>[v.name,v]));
for(const [id,values]of Object.entries(OLD_THEME_VALUES)){const v=map.get(id);for(const [mode,value]of Object.entries(values))v.setValueForMode(mode,value)}
function paint(n,key,stroke=false){const v=byName.get('console-'+key),p=figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',v);if(stroke){n.strokes=[p];n.strokeWeight=1}else n.fills=[p];mutated.push(n.id)}
function radius(n,r){n.setBoundVariable('cornerRadius',null);n.cornerRadius=r;n.cornerSmoothing=0;mutated.push(n.id)}
function noEffects(n){n.effects=[]}
for(const [id,active]of [['70:1875',false],['70:1880',true]]){const n=await figma.getNodeByIdAsync(id);n.resize(208,48);radius(n,4);if(active)paint(n,'subtle');else n.fills=[];for(const t of n.findAllWithCriteria({types:['TEXT']}))paint(t,active?'text':'muted')}
for(const id of ids){const f=await figma.getNodeByIdAsync(id);f.paddingTop=f.paddingBottom=f.paddingLeft=f.paddingRight=0;f.itemSpacing=0;paint(f,'bg');const side=f.children.find(n=>n.name==='좌측 메뉴'),main=f.children.find(n=>n.name==='사용자 작업 영역');side.resize(256,f.height);side.paddingTop=side.paddingBottom=side.paddingLeft=side.paddingRight=24;radius(side,0);noEffects(side);paint(side,'bg');paint(side,'line',true);main.resize(1664,f.height);main.layoutSizingHorizontal='FIXED';main.layoutSizingVertical='FIXED';paint(main,'bg');noEffects(main);const top=main.children.find(n=>n.name==='상단 맥락'),body=main.children.find(n=>n.name==='본문');top.resize(1664,80);paint(top,'bg');paint(top,'line',true);body.resize(1664,f.height-80);body.layoutSizingVertical='FIXED';body.paddingTop=body.paddingBottom=body.paddingLeft=body.paddingRight=40;mutated.push(side.id,main.id,top.id,body.id);
for(const n of f.findAll(()=>true)){let p=n.parent,inside=false;while(p&&p.id!==f.id){if(p.type==='INSTANCE'){inside=true;break}p=p.parent}if(inside)continue;
if(n.type==='INSTANCE'&&n.mainComponent?.parent?.id==='21:76'){const primary=n.findAllWithCriteria({types:['TEXT']}).some(t=>t.fills.some(p=>p.type==='SOLID'&&p.boundVariables?.color?.id===byName.get('console-onblue').id));radius(n,4);n.setBoundVariable('cornerRadius',byName.get('main-radius-control'));noEffects(n);paint(n,primary?'blue':'subtle');paint(n,primary?'blue':'line',true);for(const t of n.findAllWithCriteria({types:['TEXT']}))paint(t,primary?'onblue':'text')}
if(n.type!=='FRAME')continue;
if(['내 사이트와 수정 시작','확인할 일','최근 반영','크레딧','현재 연결 단계','연결 요약','진행 순서','연결된 사이트'].includes(n.name)){radius(n,8);n.setBoundVariable('cornerRadius',byName.get('main-radius-card'));noEffects(n);paint(n,'surface');paint(n,'line',true)}
if(n.name==='내 사이트와 수정 시작'){n.resize(1200,920);n.layoutSizingHorizontal='FIXED';n.layoutSizingVertical='FIXED'}
if(n.name==='현재 연결 단계'){n.resize(1200,742);n.layoutSizingHorizontal='FIXED';n.layoutSizingVertical='FIXED'}
if(n.name==='수정 시작'){n.resize(n.width,118);radius(n,8);noEffects(n);paint(n,'bg');paint(n,'line',true)}
if(n.name==='내 작업 공간'){radius(n,8);n.fills=[];noEffects(n);paint(n,'line',true)}
if(n.name==='화면 테마 전환'){radius(n,6);n.fills=[];noEffects(n);paint(n,'line',true);n.itemSpacing=8}
if(n.name.startsWith('테마 ')){radius(n,0);n.resize(96,44);noEffects(n);n.strokes=[];const selected=n.name===(f.name.includes('나이트')?'테마 나이트':'테마 라이트');if(selected)paint(n,'subtle');else n.fills=[]}
if(n.name.startsWith('상태 ')){radius(n,4);n.fills=[];noEffects(n);paint(n,'line',true)}
if(n.name.startsWith('연결 단계 ')){radius(n,8);noEffects(n);paint(n,'surface');const active=n.name==='연결 단계 1 기본 정보';paint(n,active?'blue':'line',true);for(const t of n.children.filter(c=>c.type==='TEXT'))paint(t,active?'text':'muted')}
if(n.name.endsWith('입력값')){radius(n,4);n.resize(n.width,48);noEffects(n);paint(n,'bg');paint(n,'line',true)}
if(n.name==='현재 지원 환경'){radius(n,8);paint(n,'subtle');noEffects(n);n.strokes=[]}
}
}
const cols=await figma.variables.getLocalVariableCollectionsAsync(),defaults=new Map(cols.map(c=>[c.id,c.defaultModeId]));
function resolve(id,n){const v=map.get(id);if(!v)return null;const val=v.valuesByMode[n.resolvedVariableModes[v.variableCollectionId]||defaults.get(v.variableCollectionId)]||Object.values(v.valuesByMode)[0];return val?.type==='VARIABLE_ALIAS'?resolve(val.id,n):val}
const result=[];for(const id of ids){const f=await figma.getNodeByIdAsync(id);for(const n of [f,...f.findAll(()=>true)])for(const prop of ['fills','strokes'])if(Array.isArray(n[prop])){let changed=false;const arr=n[prop].map(p=>{if(p.type!=='SOLID'||!p.boundVariables?.color)return p;const c=resolve(p.boundVariables.color.id,n);if(c?.r===undefined)return p;changed=true;return {...p,color:{r:c.r,g:c.g,b:c.b},opacity:c.a??1}});if(changed){n[prop]=arr;mutated.push(n.id)}}const all=f.findAll(()=>true);result.push({id,name:f.name,glassNodes:all.filter(n=>Array.isArray(n.effects)&&n.effects.some(e=>e.type==='GLASS')).length,overflow:all.filter(n=>n.type==='FRAME'&&n.layoutMode!=='NONE').flatMap(n=>n.children.filter(c=>c.visible&&(c.x+c.width>n.width+2||c.y+c.height>n.height+2)).map(c=>({parent:n.name,name:c.name,id:c.id})))})}
figma.viewport.scrollAndZoomIntoView(await Promise.all(['70:1886','70:2164'].map(id=>figma.getNodeByIdAsync(id))));
return {mutatedNodeIds:[...new Set(mutated)],screens:result,c02Frames:figma.currentPage.children.filter(n=>n.type==='FRAME'&&n.name.startsWith('C02 ')).map(n=>({id:n.id,name:n.name})),note:'iOS 26 스타일 적용 전의 색·직각 사이드바·버튼·필드·간격 복원. C02 첫 화면만 유지.'};
