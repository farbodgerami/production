(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[7],{108:function(e,t,n){"use strict";n.r(t);var a=n(1),c=n(7),r=n(2),i=n(84),l=n(83),s=n(0);t.default=function(e){var t=Object(r.b)();Object(a.useEffect)((function(){t({type:"arraygir",payload:o})}),[t]);var n=Object(r.c)((function(e){return e.userlogin})),o=[{array:[{to:"/le800/",name:"All"},{to:"/le800/page1",name:"Level 1"},{to:"/le800/page2",name:"Level 2"},{to:"/le800/page3",name:"Level 3"},{to:"/le800/page4",name:"Level 4"},{to:"/le800/page5",name:"Level 5"}]},{className:"leitner"}];return Object(s.jsx)(r.a,{store:i.a,children:Object(s.jsx)(c.a,{render:function(){return Object(s.jsx)(l.a,{appname:"le800",userlogin:n})},path:"/le800"})})}},78:function(e,t,n){"use strict";n.d(t,"b",(function(){return a})),n.d(t,"c",(function(){return c})),n.d(t,"a",(function(){return r})),n.d(t,"e",(function(){return i})),n.d(t,"f",(function(){return l})),n.d(t,"d",(function(){return s}));var a="leitnerdatarequest",c="leitnerdatasuccess",r="leitnerdatafail",i="leitnersavechangedatarequest",l="leitnersavechangedatasuccess",s="leitnersavechangedatafail"},80:function(e,t,n){e.exports={kollli:"leitnerhome_kollli__2HRVJ",main:"leitnerhome_main__3-0Cw",peigham:"leitnerhome_peigham__eV8cA",peighamchild:"leitnerhome_peighamchild__2cHil"}},81:function(e,t,n){e.exports={itemkol:"pages_itemkol__3344O",pagekol:"pages_pagekol__1DXLZ",textholder:"pages_textholder__1n07a",itemsholder:"pages_itemsholder__fvXiB",textkhli:"pages_textkhli__1MUta",item1:"pages_item1__Okklq",farsi:"pages_farsi__1k2tq",button:"pages_button__3CTyI",buttoni:"pages_buttoni__34Al4",savechanges:"pages_savechanges__C6-vb",savebutton:"pages_savebutton__2SVID",loadmore:"pages_loadmore__37JfX"}},82:function(e,t,n){e.exports={itemview:"itemview_itemview__3OEnD",overf:"itemview_overf__4DpyZ",jadokme:"itemview_jadokme__2atmx"}},83:function(e,t,n){"use strict";var a=n(79),c=n(5),r=n(7),i=n(1),l=n.n(i),s=n(80),o=n.n(s),u=n(81),d=n.n(u),j=function(e,t){var n=e.split(" ").splice(0,t),a="";for(var c in n)a=a+n[c]+" ";return a=a.substring(0,a.length-1),"".concat(a)},p=n(82),v=n.n(p),f=n(0),b=function(e){var t=Object(i.useState)(!1),n=Object(c.a)(t,2),a=n[0],r=n[1];return Object(f.jsxs)("div",{className:v.a.itemview,onClick:e.clickkol,children:[Object(f.jsx)("div",{className:v.a.overf,onClick:function(){return r((function(e){return!e}))},children:a?"..."+j(e.iteem.maani,3):j(e.iteem.kalame,3)+"..."}),Object(f.jsxs)("div",{className:v.a.jadokme,children:[1!==e.iteem.level&&Object(f.jsx)("button",{onClick:function(){return e.changelevel(e.iteem.id,!1)},children:"\u0628\u0644\u062f \u0646\u06cc\u0633\u062a\u0645"}),5!==e.iteem.level&&Object(f.jsx)("button",{onClick:function(){return e.changelevel(e.iteem.id,!0)},children:"\u0628\u0644\u062f\u0645"}),e.description]})]})},m=l.a.memo(b),h=function(e){return Object(f.jsx)("div",{onClick:e.onClick,className:e.className,children:Object(f.jsxs)("svg",{xmlns:"http://www.w3.org/2000/svg",height:"24px",viewBox:"0 0 24 24",width:"24px",fill:"#fff",children:[Object(f.jsx)("path",{d:"M0 0h24v24H0z",fill:"none"}),Object(f.jsx)("path",{d:"M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"})]})})},O=n(85),g=function(e){e.level.sort((function(e,t){var n=e.lesson,a=t.lesson;return n>a?1:n<a?-1:0}));var t=Object(i.useState)(""),n=Object(c.a)(t,2),r=n[0],l=n[1],s=Object(i.useState)(null),o=Object(c.a)(s,2),u=o[0],j=o[1],p=Object(i.useState)(null),v=Object(c.a)(p,2),b=v[0],g=v[1],x=Object(i.useState)(null),_=Object(c.a)(x,2),k=_[0],y=_[1],w=Object(i.useState)(null),N=Object(c.a)(w,2),C=N[0],S=N[1],M=Object(i.useState)(50),L=Object(c.a)(M,2),z=L[0],A=L[1],D=Object(i.useState)(!1),E=Object(c.a)(D,2),q=E[0],B=E[1],H=function(){A(z+50)},I=function(e){l(e.description),j("/media/"+e.audiofile),S(e.maani);var t=e.kalame.split(" ");g(t[0]),t.shift();var n=t.join(" ");y(n)},J=[],V=e.level;V=V.sort((function(e,t){var n=e.lesson,a=t.lesson;return n>a?1:n<a?-1:0}));var T=Math.max.apply(Math,Object(a.a)(V.map((function(e){return e.lesson}))));if(V=V.slice(0,z),!0===q){if(e.level.length>0)for(var X=function(e){var t=V.filter((function(t){return t.lesson===e}));J=[].concat(Object(a.a)(J),[t])},F=1;F<=T;F++)X(F)}else V=V.sort((function(e,t){var n=e.number,a=t.number;return a>n?-1:a<n?1:0})),J=[].concat(Object(a.a)(J),[V]);return Object(f.jsxs)(f.Fragment,{children:[e.message,Object(f.jsxs)("div",{className:d.a.savechanges,children:[Object(f.jsxs)("div",{style:{color:"white",display:"inline-block"},children:[Object(f.jsx)("h2",{style:{margin:0},children:e.appname}),"Level".concat(e.pagenum)]}),Object(f.jsx)("button",{className:d.a.buttoni,onClick:function(){return B(!q)},children:!0===q?"changes":"lessons"}),Object(f.jsx)("button",{onClick:e.savetchanges,className:d.a.savebutton,children:"save changes"})]}),Object(f.jsxs)("div",{className:d.a.pagekol,children:[Object(f.jsx)("div",{className:d.a.textholder,children:Object(f.jsxs)("div",{className:d.a.textkhli,children:[b&&Object(f.jsxs)(f.Fragment,{children:[Object(f.jsxs)("p",{style:{display:"inline-block"},children:[Object(f.jsx)("strong",{children:b}),Object(f.jsx)(h,{onClick:function(){new Audio(u).play()},className:d.a.button}),k]}),Object(f.jsx)("br",{}),Object(f.jsx)("p",{style:{direction:"rtl"},children:C})]}),function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=Object(O.a)(e);return t}(r)]})}),Object(f.jsxs)("div",{className:d.a.itemsholder,children:[!0===q&&J&&Object(f.jsxs)("div",{className:d.a.item1,children:[J.map((function(t,n){return Object(f.jsxs)("div",{children:[Object(f.jsx)("h3",{children:t[0]&&"lesson ".concat(t[0].lesson)}),t.map((function(t,n){return Object(f.jsx)(m,{changelevel:e.changelevel,iteem:t,clickkol:function(){return I(t)}},n)}))]},n)})),e.level.length>z&&Object(f.jsx)("button",{className:d.a.loadmore,onClick:function(){return H()},children:"load more"})]}),!1===q&&J&&Object(f.jsxs)("div",{className:d.a.item1,children:[J[0].map((function(t,n){return Object(f.jsx)("div",{children:Object(f.jsx)(m,{changelevel:e.changelevel,iteem:t,clickkol:function(){return I(t)}},n)},n)})),e.level.length>z&&Object(f.jsx)("button",{className:d.a.loadmore,onClick:function(){return H()},children:"load more"})]})]})]})]})},x=l.a.memo(g),_=n(2),k=n(8),y=n.n(k),w=n(16),N=n(78),C=n(17),S=n.n(C);t.a=function(e){var t=Object(i.useState)([]),n=Object(c.a)(t,2),l=n[0],s=n[1],u=Object(i.useState)([]),d=Object(c.a)(u,2),j=d[0],p=d[1],v=Object(i.useState)(),b=Object(c.a)(v,2),m=b[0],h=b[1],O=Object(i.useState)(0),g=Object(c.a)(O,2),k=g[0],C=g[1],M=Object(_.b)(),L=Object(_.c)((function(e){return e.larray})),z=L.loading,A=L.data,D=L.error,E=Object(_.c)((function(e){return e.leitnesavechangesrreducer})).data;E&&setTimeout((function(){h("")}),1e3),Object(i.useEffect)((function(){E&&h(E)}),[E]),Object(i.useEffect)((function(){var t,n;M((t=e.userlogin,n=e.appname,function(){var e=Object(w.a)(y.a.mark((function e(a){var c,r,i;return y.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,a({type:N.b}),c={headers:{"Content-type":"application/json",Authorization:"Bearer ".concat(t.userinfo.token)}},e.next=5,S.a.get("/api/".concat(n,"/userlevels/"),c);case 5:r=e.sent,i=r.data,a({type:N.c,payload:i}),e.next=13;break;case 10:e.prev=10,e.t0=e.catch(0),a({type:N.a,payload:e.t0.response&&e.t0.response.data.detail?e.t0.response.data.detail:e.t0.message});case 13:case"end":return e.stop()}}),e,null,[[0,10]])})));return function(t){return e.apply(this,arguments)}}()))}),[M,e.userlogin]),Object(i.useEffect)((function(){L.data&&(s(L.data),C(Math.max.apply(Math,Object(a.a)(L.data.map((function(e){return e.number}))))))}),[L.data]);var q,B=function(){var t,n,a;M((t=e.userlogin,n=j,a=e.appname,function(){var e=Object(w.a)(y.a.mark((function e(c){var r,i,l;return y.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,c({type:N.e}),r={headers:{"Content-type":"application/json",Authorization:"Bearer ".concat(t.userinfo.token)}},e.next=5,S.a.put("/api/".concat(a,"/userlevels/"),n,r);case 5:i=e.sent,l=i.data,c({type:N.f,payload:l}),e.next=13;break;case 10:e.prev=10,e.t0=e.catch(0),c({type:N.d,payload:e.t0.response&&e.t0.response.data.detail?e.t0.response.data.detail:e.t0.message});case 13:case"end":return e.stop()}}),e,null,[[0,10]])})));return function(t){return e.apply(this,arguments)}}()))},H=null;L.data&&(q=[(H=l).filter((function(e){return 1===e.level})),H.filter((function(e){return 2===e.level})),H.filter((function(e){return 3===e.level})),H.filter((function(e){return 4===e.level})),H.filter((function(e){return 5===e.level}))]);var I=function(e,t){C(k+1);var n=H.filter((function(t){return t.id===e}));!function(e){var t=e;if(0!==j.filter((function(t){return t.id===e.id})).length){var n=j,c=n.findIndex((function(t){return t.id===e.id}));n[c]=t,p(Object(a.a)(n))}else p([].concat(Object(a.a)(j),[t]))}({id:n[0].id,level:!0===t?n[0].level+1:n[0].level-1,number:k+1});var c={id:n[0].id,kalame:n[0].kalame,maani:n[0].maani,level:!0===t?n[0].level+1:n[0].level-1,description:n[0].description,audiofile:n[0].audiofile,lesson:n[0].lesson,number:k+1},r=Object(a.a)(H),i=r.findIndex((function(e){return e.id===c.id}));r[i]=c,s(r),H=r},J=null;return z&&(J="loading..."),D&&(J=D),!1===e.userlogin.userinfo.haspaid&&(J="\u0645\u0647\u0644\u062a \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u0628\u0647 \u0627\u062a\u0645\u0627\u0645 \u0631\u0633\u06cc\u062f\u0647 \u0627\u0633\u062a  \u0644\u0637\u0641\u0627 \u0633\u0631\u0648\u06cc\u0633 \u062e\u0648\u062f\u0631\u0627 \u062a\u0645\u06cc\u062f\u06cc\u062f \u06a9\u0646\u06cc\u062f"),Object(f.jsxs)("div",{className:o.a.kollli,children:[J&&Object(f.jsx)("div",{className:o.a.peigham,children:Object(f.jsx)("div",{className:o.a.peighamchild,children:Object(f.jsx)("h2",{children:J})})}),A&&e.userlogin.userinfo.haspaid&&Object(f.jsx)("main",{className:o.a.main,children:Object(f.jsx)(r.c,{children:q.map((function(t,n){return Object(f.jsx)(r.a,{exact:!0,path:"/".concat(e.appname,"/page").concat(n+1),render:function(){return Object(f.jsx)(x,{appname:e.appname,savetchanges:B,changelevel:I,level:t,pagenum:n+1,message:m})}},n)}))})})]})}},84:function(e,t,n){"use strict";var a=n(20),c=n(31),r=n(30),i=n(78),l=Object(a.combineReducers)({larray:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case i.b:return{loading:!0};case i.c:return{loading:!1,data:t.payload};case i.a:return{loading:!1,error:t.payload};default:return e}},leitnesavechangesrreducer:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=arguments.length>1?arguments[1]:void 0;switch(t.type){case i.e:return{loading:!0};case i.f:return{loading:!1,success:!0,data:t.payload};case i.d:return{loading:!1,error:t.payload};default:return e}}}),s=[c.a],o=Object(a.createStore)(l,Object(r.composeWithDevTools)(a.applyMiddleware.apply(void 0,s)));t.a=o}}]);
//# sourceMappingURL=7.c6202ef8.chunk.js.map