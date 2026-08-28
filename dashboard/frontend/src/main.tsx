import React, {useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';
import './styles.css';

type Risk = {risk_score:number; risk_level:string; simulation_only:boolean};
function App(){
 const [risk,setRisk]=useState<Risk>({risk_score:0,risk_level:'NORMAL',simulation_only:true});
 useEffect(()=>{ fetch('http://localhost:8000/risk/current').then(r=>r.json()).then(setRisk).catch(()=>{}); },[]);
 return <main>
   <div className="banner">EDUCATIONAL SIMULATION — NOT FOR OPERATIONAL USE</div>
   <h1>MountainGuard-AI</h1><p>Observe → Understand → Detect → Warn → Prepare</p>
   <section><h2>Current simulated risk</h2><div className="risk">{risk.risk_level}</div><p>Score: {risk.risk_score}</p></section>
   <section><h2>Starter dashboard</h2><p>Extend this with sensor charts, a fictional GIS map, evidence explanations and TEST alert history.</p></section>
 </main>
}
createRoot(document.getElementById('root')!).render(<App/>);
