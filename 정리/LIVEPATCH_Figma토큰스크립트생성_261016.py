from pathlib import Path
import json
root=Path(__file__).resolve().parent
skills=Path('C:/Users/User/.codex/plugins/cache/openai-curated-remote/figma/16.0.0/skills')
data=json.loads((root/'LIVEPATCH_Foundations토큰_261016.json').read_text(encoding='utf-8'))
helpers='\n'.join((skills/'figma-generate-library/scripts'/f).read_text(encoding='utf-8') for f in ['createVariableCollection.js','createSemanticTokens.js'])
code=helpers+'\nconst SOURCE='+json.dumps(data,ensure_ascii=False)+';\n'+'''
const existing = await figma.variables.getLocalVariableCollectionsAsync();
if(existing.some(c=>c.name.startsWith('LP '))) throw new Error('LP collections already exist. Read state and reconcile before creation.');
await Promise.all(['Regular','Medium','SemiBold','Bold'].map(style=>figma.loadFontAsync({family:'Pretendard',style})));
const ledger={runId:'livepatch-foundations-261016',scope:'Foundations only',fileKey:'VwuyN75CQK9Kn0ZyIVmF4S',step:'tokens-created',entities:{collections:{},variables:{},primitives:{},textStyles:{},effectStyles:{}},completedSteps:['discovery'],pendingValidations:['foundations-canvas']};
const cols={};
for(const name of ['Primitives','Color','Metrics','Typography']){
 const {collection,modeIds}=await createVariableCollection('LP '+name,[name==='Color'?'Light':'Value']);cols[name]={collection,modeIds};ledger.entities.collections[name]={id:collection.id,modes:modeIds};
}
const dedup=new Map();const primTokens=[];
for(const token of SOURCE.tokens){const key=token.type+':'+JSON.stringify(token.value);if(dedup.has(key))continue;
 const name=token.type==='COLOR'?'Color '+token.value.replace('#','').toUpperCase():token.type==='STRING'?'Font '+token.value:'Number '+String(token.value).replaceAll('.','p');
 dedup.set(key,name);primTokens.push({name,type:token.type,values:{Value:token.value},scopes:[],codeSyntax:{WEB:'var('+token.css+')'}});
}
const {variables:prims}=await createSemanticTokens(cols.Primitives.collection,cols.Primitives.modeIds,primTokens);
for(const [name,v] of Object.entries(prims))ledger.entities.primitives[name]=v.id;
const vars={};
for(const group of ['Color','Metrics','Typography']){
 const tokens=SOURCE.tokens.filter(t=>t.group===group).map(t=>({name:t.name,type:t.type,values:{[group==='Color'?'Light':'Value']:{type:'VARIABLE_ALIAS',id:prims[dedup.get(t.type+':'+JSON.stringify(t.value))].id}},scopes:t.scopes,codeSyntax:{WEB:'var('+t.css+')'}}));
 const {variables}=await createSemanticTokens(cols[group].collection,cols[group].modeIds,tokens);
 for(const t of SOURCE.tokens.filter(t=>t.group===group)){vars[t.css]=variables[t.name];ledger.entities.variables[t.css]={id:variables[t.name].id};}
}
// 호환/역할 별칭은 직접 semantic token으로 연결한다.
for(const token of SOURCE.tokens.filter(t=>t.alias_css&&vars[t.alias_css])){
 const mode=cols[token.group].modeIds[token.group==='Color'?'Light':'Value'];vars[token.css].setValueForMode(mode,{type:'VARIABLE_ALIAS',id:vars[token.alias_css].id});
}
for(const spec of SOURCE.text_styles){
 const style=figma.createTextStyle();style.name=spec.name;style.fontName={family:'Pretendard',style:spec.weight};style.fontSize=spec.size;style.lineHeight={unit:'PIXELS',value:spec.line};style.letterSpacing={unit:'PERCENT',value:spec.size>=24?-1:0};
 style.setBoundVariable('fontFamily',vars['--font-sans']);style.setBoundVariable('fontSize',vars[spec.size_css]);style.setBoundVariable('lineHeight',vars[spec.line_css]);
 ledger.entities.textStyles[spec.name]={id:style.id,font:spec.weight,size:spec.size,line:spec.line};
}
for(const [name,y,radius,opacity] of [['LP Floating',8,24,.08],['LP Overlay',20,60,.14]]){
 const style=figma.createEffectStyle();style.name=name;style.effects=[{type:'DROP_SHADOW',color:{r:17/255,g:19/255,b:23/255,a:opacity},offset:{x:0,y},radius,spread:0,visible:true,blendMode:'NORMAL'}];ledger.entities.effectStyles[name]=style.id;
}
const all=await figma.variables.getLocalVariablesAsync();const ids=Object.values(ledger.entities.variables).map(v=>v.id);const bad=all.filter(v=>ids.includes(v.id)&&(!v.codeSyntax.WEB||v.scopes.includes('ALL_SCOPES')||!Object.values(v.valuesByMode).every(x=>x&&x.type==='VARIABLE_ALIAS')));
ledger.validation={semanticCount:SOURCE.tokens.length,primitiveCount:primTokens.length,textStyles:SOURCE.text_styles.length,effectStyles:2,badVariableIds:bad.map(v=>v.id)};
ledger.completedSteps.push('tokens-structural-validation');
return {ledger,summary:ledger.validation};
'''
(root/'LIVEPATCH_FigmaFoundations토큰_261016.js').write_text(code,encoding='utf-8')
print('script ready')
