!function(){"use strict";const e=["client/chunk.cd00467c.js","client/client.d70ab795.js","client/index.5b6e40a5.js","client/bar.3e73b734.js","client/foo.87da593a.js"].concat(["500-128.png","500-256.png","500-512.png","favicon.png","global.css","manifest.json","planet-earth.png"]),t=new Set(e);self.addEventListener("install",t=>{t.waitUntil(caches.open("cache1541803799150").then(t=>t.addAll(e)).then(()=>{self.skipWaiting()}))}),self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(async e=>{for(const t of e)"cache1541803799150"!==t&&await caches.delete(t);self.clients.claim()}))}),self.addEventListener("fetch",e=>{if("GET"!==e.request.method||e.request.headers.has("range"))return;const n=new URL(e.request.url);n.protocol.startsWith("http")&&(n.hostname===self.location.hostname&&n.port!==self.location.port||(n.host===self.location.host&&t.has(n.pathname)?e.respondWith(caches.match(e.request)):"only-if-cached"!==e.request.cache&&e.respondWith(caches.open("offline1541803799150").then(async t=>{try{const n=await fetch(e.request);return t.put(e.request,n.clone()),n}catch(n){const s=await t.match(e.request);if(s)return s;throw n}}))))})}();
