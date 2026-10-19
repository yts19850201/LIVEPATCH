//FIGMA_IOS26_STYLE
await figma.setCurrentPageAsync(await figma.getNodeByIdAsync('21:60'));
await Promise.all(['Regular','Medium','SemiBold','Bold'].map(style=>figma.loadFontAsync({family:'Pretendard',style})));
const created=[],mutated=[],frames=[];
const ids=['70:1886','70:2025','70:2164','70:2317','72:1314','72:1450'];
const coll=await figma.variables.getVariableCollectionByIdAsync('VariableCollectionId:70:1832');const modes={night:'70:4',light:'70:5'};
const vars=await figma.variables.getLocalVariablesAsync(),vm=new Map(vars.map(v=>[v.name,v]));
function rgba(h,a=1){return {r:parseInt(h.slice(0,2),16)/255,g:parseInt(h.slice(2,4),16)/255,b:parseInt(h.slice(4,6),16)/255,a}}
const values={bg:['0B0B0F','F2F2F7'],surface:['1C1C1E','FFFFFF'],subtle:['2C2C2E','F2F2F7'],text:['F5F5F7','1C1C1E'],body:['E5E5EA','3A3A3C'],muted:['AEAEB2','636366'],line:['3A3A3C','D1D1D6'],blue:['0A84FF','007AFF'],onblue:['FFFFFF','FFFFFF']};
const oldValues={};for(const [key,colors]of Object.entries(values)){const v=vm.get('console-'+key);oldValues[v.id]=v.valuesByMode;v.setValueForMode(modes.night,rgba(colors[0]));v.setValueForMode(modes.light,rgba(colors[1]));}
const newValues={glass:[rgba('2C2C2E',.82),rgba('FFFFFF',.78)],'glass-line':[rgba('FFFFFF',.16),rgba('FFFFFF',.92)],selection:[rgba('0A84FF',.16),rgba('007AFF',.10)],field:[rgba('2C2C2E'),rgba('F2F2F7')],'card-line':[rgba('FFFFFF',.07),rgba('FFFFFF',.9)]};
for(const [name,vls]of Object.entries(newValues)){let v=vm.get('console-'+name);if(!v){v=figma.variables.createVariable('console-'+name,coll,'COLOR');v.scopes=['FRAME_FILL','SHAPE_FILL','TEXT_FILL','STROKE_COLOR'];v.setVariableCodeSyntax('WEB','--console-'+name);vm.set(v.name,v)}v.setValueForMode(modes.night,vls[0]);v.setValueForMode(modes.light,vls[1]);}
function paint(n,key,stroke=false){const p=figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:1,g:1,b:1}},'color',vm.get('console-'+key));if(stroke){n.strokes=[p];n.strokeWeight=1}else n.fills=[p];mutated.push(n.id)}
function radius(n,r){if(n.boundVariables?.cornerRadius)n.setBoundVariable('cornerRadius',null);n.cornerRadius=r;n.cornerSmoothing=.6;mutated.push(n.id)}
function glass(n,dark,full=false){paint(n,'glass');paint(n,'glass-line',true);n.effects=[{type:'GLASS',visible:true,lightIntensity:.32,lightAngle:125,refraction:.045,depth:2,dispersion:.015,radius:full?12:6},{type:'DROP_SHADOW',visible:true,blendMode:'NORMAL',color:{r:0,g:0,b:0,a:dark?.20:.06},offset:{x:0,y:full?6:2},radius:full?24:8,spread:0}];mutated.push(n.id)}
function shadow(n,dark){n.effects=[{type:'DROP_SHADOW',visible:true,blendMode:'NORMAL',color:{r:0,g:0,b:0,a:dark?.14:.035},offset:{x:0,y:2},radius:16,spread:0}];mutated.push(n.id)}
for(const [id,active]of [['70:1875',false],['70:1880',true]]){const c=await figma.getNodeByIdAsync(id);radius(c,14);c.resize(200,48);for(const t of c.findAllWithCriteria({types:['TEXT']})){t.layoutSizingHorizontal='FILL';paint(t,active?'blue':'muted')}if(active)paint(c,'selection');else c.fills=[];mutated.push(c.id)}
for(const id of ids){const f=await figma.getNodeByIdAsync(id);const dark=f.name.includes('나이트');frames.push(f);f.paddingTop=16;f.paddingBottom=16;f.paddingLeft=16;f.paddingRight=16;f.itemSpacing=16;mutated.push(f.id);const side=f.children.find(n=>n.name==='좌측 메뉴'),main=f.children.find(n=>n.name==='사용자 작업 영역');side.resize(232,f.height-32);side.paddingTop=24;side.paddingBottom=20;side.paddingLeft=16;side.paddingRight=16;radius(side,28);glass(side,dark,true);main.resize(1640,f.height-32);main.layoutSizingHorizontal='FILL';main.layoutSizingVertical='FILL';main.fills=[];main.strokes=[];mutated.push(main.id);const top=main.children.find(n=>n.name==='상단 맥락'),body=main.children.find(n=>n.name==='본문');top.resize(main.width,72);top.strokes=[];top.fills=[];top.paddingLeft=24;top.paddingRight=24;mutated.push(top.id);body.resize(main.width,main.height-72);body.layoutSizingVertical='FILL';for(const k of ['paddingTop','paddingRight','paddingBottom','paddingLeft']){body.setBoundVariable(k,null);body[k]=32}mutated.push(body.id);
const all=f.findAll(()=>true);for(const n of all){let p=n.parent,inInstance=false;while(p&&p.id!==f.id){if(p.type==='INSTANCE'){inInstance=true;break}p=p.parent}if(inInstance)continue;
if(n.type==='INSTANCE'&&n.mainComponent?.parent?.id==='21:76'){const primary=n.findAllWithCriteria({types:['TEXT']}).some(t=>t.fills.some(p=>p.type==='SOLID'&&p.boundVariables?.color?.id===vm.get('console-onblue').id));radius(n,26);n.resize(n.width,52);n.counterAxisSizingMode='FIXED';if(primary){paint(n,'blue');n.strokes=[];n.effects=[{type:'DROP_SHADOW',visible:true,blendMode:'NORMAL',color:{r:0,g:.35,b:1,a:dark?.16:.10},offset:{x:0,y:3},radius:10,spread:0}]}else glass(n,dark);for(const t of n.findAllWithCriteria({types:['TEXT']})){t.fontSize=16;t.lineHeight={unit:'PIXELS',value:24}}mutated.push(n.id)}
if(n.type!=='FRAME')continue;
if(['내 사이트와 수정 시작','확인할 일','최근 반영','크레딧','현재 연결 단계','연결 요약','진행 순서'].includes(n.name)){radius(n,24);paint(n,'surface');paint(n,'card-line',true);shadow(n,dark)}
if(['내 사이트와 수정 시작','현재 연결 단계'].includes(n.name))n.layoutSizingHorizontal='FILL';
if(n.name==='내 사이트와 수정 시작')n.layoutSizingVertical='FILL';
if(n.name==='연결된 사이트'){radius(n,20);paint(n,'subtle');n.strokes=[];n.effects=[]}
if(n.name==='수정 시작'){radius(n,24);glass(n,dark);n.resize(n.width,116)}
if(n.name==='내 작업 공간'){radius(n,18);paint(n,'subtle');n.strokes=[]}
if(n.name==='화면 테마 전환'){radius(n,24);glass(n,dark);n.paddingTop=4;n.paddingBottom=4;n.paddingLeft=4;n.paddingRight=4;n.itemSpacing=4}
if(n.name.startsWith('테마 ')){radius(n,20);n.resize(94,44);const selected=n.name===(dark?'테마 나이트':'테마 라이트');if(selected){paint(n,'surface');shadow(n,dark)}else{n.fills=[];n.effects=[]}n.strokes=[]}
if(n.name.startsWith('상태 ')){radius(n,12);paint(n,'subtle');n.strokes=[]}
if(n.name.startsWith('연결 단계 ')){radius(n,18);const active=n.name==='연결 단계 1 기본 정보';paint(n,active?'selection':'surface');n.strokes=[];n.effects=[];for(const t of n.children.filter(n=>n.type==='TEXT'))paint(t,active?'blue':'muted')}
if(n.name.endsWith('입력값')){radius(n,12);paint(n,'field');n.strokes=[];n.resize(n.width,52)}
if(['현재 지원 환경'].includes(n.name)){radius(n,16);paint(n,'subtle');n.strokes=[]}
}
const cols=f.findAll(n=>n.type==='FRAME'&&['기본 정보 입력','저장소와 브랜치'].includes(n.name));for(const r of cols)for(const c of r.children)c.layoutSizingHorizontal='FILL';
}
const results=frames.map(f=>{const all=f.findAll(()=>true),overflow=all.filter(n=>n.type==='FRAME'&&n.layoutMode!=='NONE').flatMap(n=>n.children.filter(c=>c.visible&&(c.x+c.width>n.width+2||c.y+c.height>n.height+2)).map(c=>({id:c.id,name:c.name,parent:n.name,parentId:n.id,w:n.width,h:n.height,childX:c.x,childY:c.y,childW:c.width,childH:c.height})));return {id:f.id,name:f.name,overflow,fonts:[...new Set(all.filter(n=>n.type==='TEXT').map(n=>n.fontName.family))],images:all.filter(n=>Array.isArray(n.fills)&&n.fills.some(p=>p.type==='IMAGE')).length,descendants:all.length}});
figma.viewport.scrollAndZoomIntoView([frames[0],frames[2]]);
return {createdNodeIds:created,mutatedNodeIds:[...new Set(mutated)],oldThemeValues:oldValues,screens:results,reference:'iOS and iPadOS 26 · Liquid Glass controls, rounded grouped surfaces, inset sidebar, segmented theme control',limitation:'라이브러리 직접 가져오기는 권한 제한. 기존 편집 가능 컴포넌트에 스타일 참조 적용.',scope:'현재 C01 상태와 C02 첫 화면에만 적용. 후속 단계·M01·C13·원본 HTML 미수정.'};
