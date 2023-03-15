window.addEventListener('load', (event) => {
  console.log("Page loaded.");
    if(document.getElementById("smenu").checked == true){
      document.getElementById("smenu").checked = false;
    }
});

window.addEventListener("resize", function() {
  if (window.matchMedia("(min-width: 768px)").matches) {
    console.log("Screen width is at least 500px")
    // var header = document.getElementById("topheader");
    var main_c = document.getElementById('main-content');
    var name_ = document.getElementById('my-name');
    if(document.getElementById("smenu").checked == true){
      document.getElementById("smenu").checked = false;
      const navs = document.querySelectorAll('.topnav')
      navs.forEach(nav => nav.classList.toggle('topnav_toggleShow'));
      var rect_ = document.getElementById('rectangle');
      rect_.classList.toggle('toggle_rectangle');
      //Resize color change
      // header.style.backgroundColor='#fff';
      name_.style.opacity=1;
      main_c.classList.remove('overlay');
    }

  } else {
    console.log("Screen less than 500px")
  }

})

function classToggle() {
  const navs = document.querySelectorAll('.topnav')
  navs.forEach(nav => nav.classList.toggle('topnav_toggleShow'));
  var rect_ = document.getElementById('rectangle');
  rect_.classList.toggle('toggle_rectangle');
}

document.querySelector('.icon').addEventListener('click', classToggle);


// Side menu checked color change
function boxChecked() {
 var checkBox = document.getElementById("smenu");
 var header = document.getElementById("topheader");
 var main_c = document.getElementById('main-content');
 var name_ = document.getElementById('my-name');

  if (checkBox.checked == true){
    name_.style.opacity=0.3;
    main_c.classList.add('overlay');
 }
 else if(window.pageYOffset >= header.offsetTop)
 {

    name_.style.opacity=1;
    main_c.classList.remove('overlay');
 }
 else{
    main_c.classList.remove('overlay');
    name_.style.opacity=1;
 }
}

function updateBg(){
  if (document.getElementById("smenu").checked ==true){
    var main_c = document.getElementById('main-content');
    var name_ = document.getElementById('my-name');
    main_c.classList.remove('overlay');
    name_.style.opacity=1;
    document.getElementById("smenu").checked = false;
    classToggle();
  }
}


var bibArray=new Array();

function LoadFile() {
  var oFrame = document.getElementById("bibfile");
  var strRawContents = oFrame.contentWindow.document.body.childNodes[0].innerHTML.replace(/\r/g, '');
  var arrLines = strRawContents.split("@");
  arrLines.forEach(function (line) {
      bibArray.push('@'+line);
  });
  console.log(bibArray);

}

function extractBib(s_id){
  for (var i = 0; i < bibArray.length; i++) {
    if(bibArray[i].includes(s_id)){
      mywindow = window.open("", "",);
      mywindow.document.write("<pre>"+bibArray[i]+"</pre>");
    }
  }
}




// Change Background colour with scroll
// window.addEventListener('scroll',function(){
//     var header = document.getElementById("topheader");
//     var sticky = header.offsetTop;
//     var checkBox = document.getElementById("menu");
//     // console.log(sticky);
//     // console.log(window.pageYOffset);
//     if (checkBox.checked == false){
//       if (window.pageYOffset >= sticky) {
//         header.style.backgroundColor='#ddd';
//         // header.style.width='100%';
//         // header.style.opacity='90%';
//         // console.log("asadadadasda");
//       } else {
//         header.style.backgroundColor='#fff';
//         // header.style.opacity='100%';
//         // header.css('background-color', 'rgba(0,0,255,.75)');
//       }
//     }

//     else{
//         header.style.backgroundColor='#ddd';
//     }
// });
