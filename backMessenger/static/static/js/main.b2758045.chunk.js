(this["webpackJsonptrack-mail-2019-kichyr"]=this["webpackJsonptrack-mail-2019-kichyr"]||[]).push([[0],{11:function(e,t,a){e.exports={attachmentType:"styles_attachmentType__3eIKC",message_form:"styles_message_form__1Sm1a",input_panel:"styles_input_panel__1ju52",sendMessForm:"styles_sendMessForm__3A8xD",result:"styles_result__3ivTG",messageText:"styles_messageText__3PziE"}},12:function(e,t,a){e.exports={profileImg:"styles_profileImg__2xgSU",profile_form:"styles_profile_form__3nryD",topLineContainer:"styles_topLineContainer__-JsNv",profileTopic:"styles_profileTopic__1KL6U",name:"styles_name__1J8hG",status:"styles_status__344Hm"}},15:function(e,t,a){e.exports={modal:"createNewChatForm_modal__2X5FK",modal_content:"createNewChatForm_modal_content__VsNJG",close:"createNewChatForm_close__3DTMr"}},16:function(e,t,a){e.exports={dateTime:"singleMessage_dateTime__2etYS",singleMessContainer:"singleMessage_singleMessContainer__3QHsN",singleMess:"singleMessage_singleMess__2Tm8v",msg:"singleMessage_msg__1XUX_"}},17:function(e,t,a){e.exports={plusbut:"plusButtonStyles_plusbut__ICY__",horizontal_plus:"plusButtonStyles_horizontal_plus__HIBYs",vertical_plus:"plusButtonStyles_vertical_plus__3Wy4d"}},18:function(e,t,a){e.exports={container:"topLine_container__1R9Zm",chatImg:"topLine_chatImg__1A5Li",topic:"topLine_topic__1fCyY"}},19:function(e,t,a){e.exports={arrow:"backArrow_arrow__ANJaT",arrowTop:"backArrow_arrowTop__291_W",arrowBottom:"backArrow_arrowBottom__2hX51"}},38:function(e,t,a){e.exports=a(71)},56:function(e,t,a){},57:function(e,t,a){},7:function(e,t,a){e.exports={dialog_list_wrap:"DialogList_dialog_list_wrap__8jDdH",translating:"DialogList_translating__2VsUs",modal:"DialogList_modal__2jYn0","modal-content":"DialogList_modal-content__2sQCj",close:"DialogList_close__mj83R",plusbut:"DialogList_plusbut__5xaUS","horizontal-plus":"DialogList_horizontal-plus__2hIb5","vertical-plus":"DialogList_vertical-plus__2al7V",container:"DialogList_container__TgqVT",dialogsListContainer:"DialogList_dialogsListContainer__rSctl",chatwrap:"DialogList_chatwrap__3ibf_",wrap:"DialogList_wrap__2BclI",meta:"DialogList_meta__3QcWi",addinfo:"DialogList_addinfo__39jLj",chatImg:"DialogList_chatImg__3neQO",preview:"DialogList_preview__1B4wF",topic:"DialogList_topic__30BO-",dot:"DialogList_dot__3C_N6"}},70:function(e,t,a){},71:function(e,t,a){"use strict";a.r(t);var n=a(0),s=a.n(n),c=a(29),l=a.n(c),r=a(6),i=a(9),o=a(13),p=a(3),g=a(30);a(56);var m=function(){return s.a.createElement("div",{className:"burgerButt"},s.a.createElement("div",null),s.a.createElement("div",null),s.a.createElement("div",null))};a(57);function u(){return s.a.createElement("input",{type:"text",placeholder:"Search.."})}var d=function(){return s.a.createElement("div",{className:"container"},s.a.createElement(m,null),s.a.createElement(u,null))},_=a(7),h=a.n(_),v=a(14),f=a(17),E=a(15),S=a(34),w=a.n(S),b=a(35),y=a.n(b),C={userId:1},x="http://127.0.0.1:8000/";var L=function(e){return s.a.createElement("div",null,e.name)};var N=function(){var e=Object(n.useState)({value:"",suggestions:[]}),t=Object(i.a)(e,2),a=t[0],c=t[1];console.log(a);var l={placeholder:"Type a some part of user name",value:a.value,onChange:function(e,t){var n=t.newValue;c(Object(r.a)({},a,{value:n}))}.bind(this)};return s.a.createElement(y.a,{suggestions:a.suggestions,onSuggestionsFetchRequested:function(e){!function(e,t){w.a.async((function(a){for(;;)switch(a.prev=a.next){case 0:fetch(x+"users/profile/"+e,{crossDomain:!0,mode:"cors",method:"GET",credentials:"include"}).then((function(e){return console.log(e),e.text()})).then((function(e){console.log(e),Promise.resolve(e?JSON.parse(e):{})})).catch((function(e){Promise.reject(e)})).then((function(a){t({value:e,renderSuggestion:a})}));case 1:case"end":return a.stop()}}))}(e.value,c)},onSuggestionsClearRequested:function(){c(Object(r.a)({},a,{suggestions:[]}))},getSuggestionValue:function(e){return e.name},renderSuggestion:L,inputProps:l})};function I(e){var t=e.setHiding;return s.a.createElement("div",{role:"button",id:"isActiveForSetHiding",tabIndex:0,className:f.plusbut,onClick:t},s.a.createElement("div",{className:f.horizontal_plus,id:"isActiveForSetHiding"}),s.a.createElement("div",{className:f.vertical_plus,id:"isActiveForSetHiding"}))}function O(e){var t=e.isHide,a=e.setHiding,n=e.setChats,c=e.chats,l=null;return s.a.createElement("div",{className:E.modal,id:"isActiveForSetHiding",style:t?{display:"block"}:{display:"none"},role:"button",tabIndex:0,onClick:a},s.a.createElement("div",{className:E.modal_content},s.a.createElement("span",{className:E.close,id:"isActiveForSetHiding",role:"button",tabIndex:0,onClick:a},"\xd7"),s.a.createElement("h2",null,"Create new chat"),s.a.createElement("br",null),s.a.createElement("input",{className:E.topic,ref:function(e){l=e},type:"text",name:"topic",placeholder:"Chat Topic"}),s.a.createElement(N,null),s.a.createElement("button",{onClick:function(e){e.preventDefault(),n(function(){var e=function(e){var t;null==localStorage.getItem("DialogList")?(localStorage.setItem("DialogList","[]"),t=[]):t=JSON.parse(localStorage.getItem("DialogList"));var a,n=t.length;return t.push({chat_id:n,topic:e,lastmessage:""}),localStorage.setItem("DialogList",JSON.stringify(t)),null==localStorage.getItem("messages")?(localStorage.setItem("messages","{}"),a={}):a=JSON.parse(localStorage.getItem("messages")),a[n]=[],localStorage.setItem("messages",JSON.stringify(a)),t[t.length-1]}(l.value);return[].concat(Object(v.a)(c),[e])}()),a(e)}},s.a.createElement("span",{id:"isActiveForSetHiding"},"Create new chat"))))}var A=function(e){var t=e.setChats,a=e.chats,c=Object(n.useState)(!1),l=Object(i.a)(c,2),r=l[0],o=l[1],p=function(e){e.preventDefault(),e.stopPropagation(),console.log(e.target),"isActiveForSetHiding"===e.target.id&&o(!r)};return s.a.createElement(s.a.Fragment,null,s.a.createElement(I,{setHiding:p}),s.a.createElement(O,{isHide:r,setHiding:p,setChats:t,chats:a}))};function j(e){var t=JSON.parse(localStorage.getItem("messages"));return{chatId:e,topic:JSON.parse(localStorage.getItem("DialogList"))[e].topic,messages:t[e]}}var T=function(e,t){var a=Object(p.f)();return e.map((function(e,n){return s.a.createElement("div",{className:h.a.chatwrap,key:n.toString()},s.a.createElement("div",{onClick:function(n){a.push("".concat(window.publicUrl,"/chat")),function(e,t){t({appPage:"Chat",openedChat:j(e),prevAppPage:"ChatList"})}(e.chat_id,t)},role:"button",tabIndex:0,className:h.a.wrap,id:e.chat_id},s.a.createElement("img",{className:h.a.chatImg,src:"http://emilcarlsson.se/assets/rachelzane.png",alt:""}),s.a.createElement("div",{className:h.a.meta},s.a.createElement("div",{className:h.a.topic},"".concat(e.topic)," "),s.a.createElement("div",{className:h.a.preview},e.lastmessage," ")),s.a.createElement("div",{className:h.a.addinfo},s.a.createElement("span",{className:h.a.dot}),s.a.createElement("p",null,"21:23"))))}))};function D(e){var t=e.chats,a=e.setAppState;return s.a.createElement("div",{className:h.a.dialogsListContainer},null!==t&&T(t,a))}var k=function(e){e.appState;var t=e.setAppState,a=Object(n.useState)([]),c=Object(i.a)(a,2),l=c[0],r=c[1];return Object(n.useEffect)((function(){r(function(){var e=JSON.parse(localStorage.getItem("DialogList"));return null==e?[]:e}())}),[]),s.a.createElement("div",{className:h.a.dialog_list_wrap},s.a.createElement(d,null),s.a.createElement(D,{chats:l,setChats:r,setAppState:t}),s.a.createElement(A,{setChats:r,chats:l}))},M=a(36),P=a(16),H=a.n(P),z=a(18),F=a.n(z),J=a(11),B=a.n(J),U=a(19),V=a.n(U);var R=function(){return s.a.createElement("div",{className:V.a.arrow,style:{transform:"scale(-1, 1) scale(0.3)"}},s.a.createElement("div",{className:V.a.arrowTop}),s.a.createElement("div",{className:V.a.arrowBottom}))},Y='\n<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"\n\t viewBox="0 0 512 512" style="max-width: 100%; max-height: 100%;" style="enable-background:new 0 0 512 512;" xml:space="preserve" fill="blue">\n<g>\n\t<g>\n\t\t<path d="M506.955,1.314c-3.119-1.78-6.955-1.75-10.045,0.078L313.656,109.756c-4.754,2.811-6.329,8.943-3.518,13.697\n\t\t\tc2.81,4.753,8.942,6.328,13.697,3.518l131.482-77.749L210.411,303.335L88.603,266.069l158.965-94\n\t\t\tc4.754-2.812,6.329-8.944,3.518-13.698c-2.81-4.753-8.943-6.33-13.697-3.518L58.91,260.392c-3.41,2.017-5.309,5.856-4.84,9.791\n\t\t\ts3.216,7.221,7.004,8.38l145.469,44.504L270.72,439.88c0.067,0.121,0.136,0.223,0.207,0.314c1.071,1.786,2.676,3.245,4.678,4.087\n\t\t\tc1.253,0.527,2.57,0.784,3.878,0.784c2.563,0,5.086-0.986,6.991-2.849l73.794-72.12l138.806,42.466\n\t\t\tc0.96,0.293,1.945,0.438,2.925,0.438c2.116,0,4.206-0.672,5.948-1.961C510.496,409.153,512,406.17,512,403V10\n\t\t\tC512,6.409,510.074,3.093,506.955,1.314z M271.265,329.23c-1.158,1.673-1.779,3.659-1.779,5.694v61.171l-43.823-79.765\n\t\t\tl193.921-201.21L271.265,329.23z M289.486,411.309v-62.867l48.99,14.988L289.486,411.309z M492,389.483l-196.499-60.116\n\t\t\tL492,45.704V389.483z"/>\n\t</g>\n</g>\n<g>\n\t<g>\n\t\t<path d="M164.423,347.577c-3.906-3.905-10.236-3.905-14.143,0l-93.352,93.352c-3.905,3.905-3.905,10.237,0,14.143\n\t\t\tC58.882,457.024,61.441,458,64,458s5.118-0.976,7.071-2.929l93.352-93.352C168.328,357.815,168.328,351.483,164.423,347.577z"/>\n\t</g>\n</g>\n<g>\n\t<g>\n\t\t<path d="M40.071,471.928c-3.906-3.903-10.236-3.903-14.142,0.001l-23,23c-3.905,3.905-3.905,10.237,0,14.143\n\t\t\tC4.882,511.024,7.441,512,10,512s5.118-0.977,7.071-2.929l23-23C43.976,482.166,43.976,475.834,40.071,471.928z"/>\n\t</g>\n</g>\n<g>\n\t<g>\n\t\t<path d="M142.649,494.34c-1.859-1.86-4.439-2.93-7.069-2.93c-2.641,0-5.21,1.07-7.07,2.93c-1.86,1.86-2.93,4.43-2.93,7.07\n\t\t\tc0,2.63,1.069,5.21,2.93,7.07c1.86,1.86,4.44,2.93,7.07,2.93s5.21-1.07,7.069-2.93c1.86-1.86,2.931-4.44,2.931-7.07\n\t\t\tC145.58,498.77,144.51,496.2,142.649,494.34z"/>\n\t</g>\n</g>\n<g>\n\t<g>\n\t\t<path d="M217.051,419.935c-3.903-3.905-10.233-3.905-14.142,0l-49.446,49.445c-3.905,3.905-3.905,10.237,0,14.142\n\t\t\tc1.953,1.953,4.512,2.929,7.071,2.929s5.118-0.977,7.071-2.929l49.446-49.445C220.956,430.172,220.956,423.84,217.051,419.935z"/>\n\t</g>\n</g>\n<g>\n\t<g>\n\t\t<path d="M387.704,416.139c-3.906-3.904-10.236-3.904-14.142,0l-49.58,49.58c-3.905,3.905-3.905,10.237,0,14.143\n\t\t\tc1.953,1.952,4.512,2.929,7.071,2.929s5.118-0.977,7.071-2.929l49.58-49.58C391.609,426.377,391.609,420.045,387.704,416.139z"/>\n\t</g>\n</g>\n<g>\n\t<g>\n\t\t<path d="M283.5,136.31c-1.86-1.86-4.44-2.93-7.07-2.93s-5.21,1.07-7.07,2.93c-1.859,1.86-2.93,4.44-2.93,7.08\n\t\t\tc0,2.63,1.07,5.2,2.93,7.06c1.86,1.87,4.44,2.93,7.07,2.93s5.21-1.06,7.07-2.93c1.859-1.86,2.93-4.43,2.93-7.06\n\t\t\tC286.43,140.75,285.36,138.17,283.5,136.31z"/>\n\t</g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n<g>\n</g>\n</svg>\n',G='\n<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"\n\tposition="relative" style="max-width: 100%; max-height: 100%;" viewBox="0 0 512 512" enable-background="new 0 0 512 512" xml:space="preserve" fill="blue">\n<g>\n\t<path d="M97.344,482.17c-23.311,0-45.215-9.084-61.689-25.555c-34.01-34.014-34.01-89.361,0-123.371L305.343,63.543\n\t\tc21.727-21.75,50.645-33.713,81.39-33.713c30.75,0,59.667,11.963,81.395,33.713c21.748,21.744,33.726,50.645,33.726,81.389\n\t\tc0,30.75-11.964,59.65-33.708,81.381L255.843,438.596c-6.374,6.371-16.696,6.371-23.067,0c-6.374-6.373-6.374-16.695,0-23.07\n\t\tl212.298-212.283c15.583-15.58,24.153-36.291,24.153-58.311c0-22.016-8.588-42.74-24.167-58.322\n\t\tc-15.583-15.58-36.294-24.154-58.327-24.154c-22.029,0-42.74,8.574-58.323,24.154L58.725,356.311\n\t\tc-21.283,21.301-21.283,55.938,0,77.234c20.645,20.617,56.589,20.617,77.233,0l181.091-181.105\n\t\tc4.924-4.924,7.745-11.74,7.745-18.688c0-7.045-2.755-13.686-7.759-18.689c-10.291-10.291-27.067-10.322-37.358,0L156,338.754\n\t\tc-6.37,6.375-16.697,6.375-23.067,0c-6.374-6.371-6.374-16.697,0-23.066l123.673-123.691c23.005-23.004,60.461-23.004,83.497,0\n\t\tc11.169,11.166,17.317,26,17.317,41.756c0,15.547-6.308,30.762-17.3,41.754L159.029,456.615\n\t\tC142.555,473.086,120.65,482.17,97.344,482.17z"/>\n</g>\n</svg>\n',Q=a(37);function X(e){var t=JSON.parse(localStorage.getItem("messages"));t[e.chatId].push(e),localStorage.setItem("messages",JSON.stringify(t))}var q=function e(t,a,n,s){Object(M.a)(this,e),this.messageText=n,this.userId=a,this.time=function(){var e=new Date,t="".concat(e.getFullYear(),"-").concat(e.getMonth()+1,"-").concat(e.getDate()),a="".concat(e.getHours(),":").concat(e.getMinutes(),":").concat(e.getSeconds());return"".concat(t," ").concat(a)}(),this.chatId=t,this.contentType=s};function K(e){var t=e.topic,a=e.appState,n=e.setAppState,c=Object(p.f)();return s.a.createElement("div",{id:"chatTopLine",className:F.a.container},s.a.createElement("div",{id:"chatBack",onClick:function(e){n(Object(r.a)({},a,{appPage:"ChatList",prevAppPage:c.location})),c.push("".concat(window.publicUrl,"/"))},style:{flex:"0.2"},role:"button",tabIndex:0},s.a.createElement(R,null)),s.a.createElement("div",{className:F.a.topic}," ",t," "))}function W(e){var t,a=e.messages,c=e.appState,l=(e.setAppState,Object(p.f)());return Object(n.useEffect)((function(){t.scrollTop=t.scrollHeight}),[a]),s.a.createElement("div",{className:B.a.result,style:{scrollTop:"scrollHeight"},ref:function(e){t=e}},a.map((function(e,t){return s.a.createElement("div",{key:t.toString(),className:H.a.singleMessContainer},s.a.createElement("input",{type:"image",onClick:function(e){l.push("".concat(window.publicUrl,"/profile"),c)},className:F.a.chatImg,src:"http://emilcarlsson.se/assets/rachelzane.png",alt:"Avatar"}),s.a.createElement("div",{className:H.a.singleMess,sender:e.userId===C.userId?"me":"him"},s.a.createElement("div",{className:H.a.singleMessText},"link"===e.contentType?s.a.createElement("a",{href:e.messageText}," ",e.messageText," "):s.a.createElement("div",null," ",e.messageText," ")),s.a.createElement("p",{className:H.a.dateTime}," ",e.time," ")))})))}function Z(e){var t=e.appState,a=e.setAppState,n=s.a.createRef(),c=s.a.createRef(),l=Object(Q.usePosition)(),i=l.latitude,o=l.longitude;return s.a.createElement("div",{className:B.a.input_panel},s.a.createElement("form",{className:B.a.sendMessForm,onSubmit:function(e){e.preventDefault();var n=e.target[0].value;if(""!==n.replace(/\s/gi,"")){var s=new q(t.openedChat.chatId,C.userId,n,"text");X(s),a(Object(r.a)({},t,{},Object.assign(t.openedChat,{messages:[].concat(Object(v.a)(t.openedChat.messages),[s])}))),e.target[0].value=""}}},s.a.createElement("input",{ref:n,type:"text",className:B.a.messageText,maxLength:"512",placeholder:"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0438\u043d\u0435"}),s.a.createElement("div",{style:{margin:"5px",flex:"0.3",maxHeight:"100%"}},s.a.createElement("div",{ref:c,className:B.a.attachmentType},s.a.createElement("div",null,"\u0424\u0430\u0439\u043b"),s.a.createElement("div",{onClick:function(e){e.preventDefault();var n=new q(t.openedChat.chatId,C.userId,"https://www.openstreetmap.org/#map=18/".concat(i,"/").concat(o),"link");X(n),a(Object(r.a)({},t,{},Object.assign(t.openedChat,{messages:[].concat(Object(v.a)(t.openedChat.messages),[n])}))),c.current.style.transform="scale(0)"}},"\u041c\u043e\u044f \u0433\u0435\u043e\u043b\u043e\u043a\u0430\u0446\u0438\u044f"),s.a.createElement("div",null,"\u0410\u0443\u0434\u0438\u043e\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0435")),s.a.createElement("div",{dangerouslySetInnerHTML:{__html:G},style:{height:"100%"},onClick:function(e){c.current.style.transform="scale(1)"!==c.current.style.transform?"scale(1)":"scale(0)"}})),s.a.createElement("label",{style:{flex:"0.3",display:"flex",maxHeight:"100%"}},s.a.createElement("input",{style:{display:"none"},type:"submit",value:""}),s.a.createElement("div",{dangerouslySetInnerHTML:{__html:Y},style:{flex:"1",margin:"5px"}}))))}var $=function(e){var t=e.appState,a=e.setAppState;return s.a.createElement("div",{className:B.a.message_form},s.a.createElement(K,{topic:t.openedChat.topic,appState:t,setAppState:a}),s.a.createElement(W,{messages:t.openedChat.messages,appState:t,setAppState:a}),s.a.createElement(Z,{appState:t,setAppState:a}))},ee=a(12),te=a.n(ee);function ae(e){var t=e.appState,a=(e.setAppState,Object(p.f)());return s.a.createElement("div",{id:"profileTopLine",className:te.a.topLineContainer},s.a.createElement("div",{id:"profileBack",onClick:function(e){a.push("".concat(window.publicUrl,"/").concat(t.prevAppPage))},style:{flex:"0.2"},role:"button",tabIndex:0},s.a.createElement(R,null)),s.a.createElement("div",{className:te.a.profileTopic}," Profile Page "))}var ne=function(e){var t=e.appState,a=e.setAppState;return s.a.createElement("div",{className:te.a.profile_form},s.a.createElement(ae,{appState:t,setAppState:a}),s.a.createElement("img",{className:te.a.profileImg,src:"http://emilcarlsson.se/assets/rachelzane.png",alt:"Avatar"}),s.a.createElement("div",{className:te.a.name},"\u041a\u0438\u0440\u0438\u043b\u043b \u0427\u0435\u043a\u0430\u043d\u043e\u0432"),s.a.createElement("div",{className:te.a.status},"Status: no pain no gain"))},se=(a(70),function(e){var t=Object(n.useState)({appPage:"",prevAppPage:"ChatList",openedChat:{chatId:-1,topic:"",messages:[]}}),a=Object(i.a)(t,2),c=a[0],l=a[1];return Object(n.useEffect)((function(){Array.isArray(JSON.parse(localStorage.getItem("DialogList")))||localStorage.clear()}),[]),window.publicUrl="/static",console.log("kek"+window.publicUrl),s.a.createElement(o.a,null,s.a.createElement(g.a,{atEnter:{opacity:0},atLeave:{opacity:0},atActive:{opacity:1},className:"switch-wrapper"},s.a.createElement(p.a,{path:"".concat(window.publicUrl,"/chat/")},(function(e){return"Chat"!==c.appPage&&l(Object(r.a)({},c,{appPage:"Chat"})),s.a.createElement($,{appState:c,setAppState:l})})),s.a.createElement(p.a,{path:"".concat(window.publicUrl,"/")},(function(e){return"ChatList"!==c.appPage&&l(Object(r.a)({},c,{appPage:"ChatList",prevAppPage:c.appPage})),s.a.createElement(k,{appState:c,setAppState:l})})),s.a.createElement(p.a,{path:"".concat(window.publicUrl,"/profile/")},(function(e){return"ProfilePage"!==c.appPage&&l(Object(r.a)({},c,{appPage:"ProfilePage",prevAppPage:c.appPage})),s.a.createElement(ne,{appState:c,setAppState:l})}))))});l.a.render(s.a.createElement(se,null),document.getElementById("root"))}},[[38,1,2]]]);
//# sourceMappingURL=main.b2758045.chunk.js.map