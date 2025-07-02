// 登录页js逻辑
logBlog = {
    // 项目基本信息描述
    stDa: "2025/1/22",
    edDa: "2025/1/22",
    upDa: "2025/1/22",
    anchor: "Nalicost"
}
logBlog.eles = {
    $use: $("#log>.wid>.info>form>div:nth-child(2)>input"),
    $pas: $("#log>.wid>.info>form>div:nth-child(4)>input"),
    $errs: $("#log>.wid>.info>form>.err"),
    $form: $("#log>.wid>.info>form")
}
logBlog.isEmp = function (v){
        return (v === "");
}
logBlog.errSH = function (ele){
    $(ele).show();
    setTimeout(function(){
        $(ele).hide()
    }, 2000);
}
logBlog.eles.$form.on("submit", function (){
    if(!logBlog.isEmp(logBlog.eles.$use.val()) && !logBlog.isEmp(logBlog.eles.$pas.val())){
        return true;
    }else{
        if (logBlog.isEmp(logBlog.eles.$use.val())){
            logBlog.errSH(logBlog.eles.$errs[0]);
        }
        if (logBlog.isEmp(logBlog.eles.$pas.val())){
            logBlog.errSH(logBlog.eles.$errs[1]);
        }
    }
    return false;
})
// 文章列表页逻辑
newsBlog = {
    stDa: "2025/1/22",
    edDa: "2025/1/22",
    upDa: "2025/1/22",
    anchor: "Nalicost"
}
newsBlog.eles = {
    $lCon: $("#news>.box>.con>.lCon"),
    $rCon: $("#news>.box>.con>.rCon>ul")
}
newsBlog.conA = [
    {
        tit: "曼联新闻：滕哈赫或将迅速回归执教，接手多特蒙德",
        imgUrl: "imgs/AA1xEFuz.jpg",
        paraA: "前曼联主教练埃里克·滕哈赫可能很快就会回归执教，接替被解雇的努里·沙欣。这位前利物浦中场球员在多特蒙德遭遇糟糕的战绩后下课...",
        paraB: "神秘人&nbsp;&nbsp;&nbsp;&nbsp;学无止境&nbsp;&nbsp;&nbsp;&nbsp;2018-5-13&nbsp;&nbsp;&nbsp;&nbsp;34567人已阅读&nbsp;&nbsp;&nbsp;&nbsp;9999人喜欢",
    },
    {
        tit: "曼联新闻：滕哈赫或将迅速回归执教，接手多特蒙德",
        imgUrl: "imgs/AA1xEFuz.jpg",
        paraA: "前曼联主教练埃里克·滕哈赫可能很快就会回归执教，接替被解雇的努里·沙欣。这位前利物浦中场球员在多特蒙德遭遇糟糕的战绩后下课...",
        paraB: "神秘人&nbsp;&nbsp;&nbsp;&nbsp;学无止境&nbsp;&nbsp;&nbsp;&nbsp;2018-5-13&nbsp;&nbsp;&nbsp;&nbsp;34567人已阅读&nbsp;&nbsp;&nbsp;&nbsp;9999人喜欢",
    },
    {
        tit: "曼联新闻：滕哈赫或将迅速回归执教，接手多特蒙德",
        imgUrl: "imgs/AA1xEFuz.jpg",
        paraA: "前曼联主教练埃里克·滕哈赫可能很快就会回归执教，接替被解雇的努里·沙欣。这位前利物浦中场球员在多特蒙德遭遇糟糕的战绩后下课...",
        paraB: "神秘人&nbsp;&nbsp;&nbsp;&nbsp;学无止境&nbsp;&nbsp;&nbsp;&nbsp;2018-5-13&nbsp;&nbsp;&nbsp;&nbsp;34567人已阅读&nbsp;&nbsp;&nbsp;&nbsp;9999人喜欢",
    },
    {
        tit: "曼联新闻：滕哈赫或将迅速回归执教，接手多特蒙德",
        imgUrl: "imgs/AA1xEFuz.jpg",
        paraA: "前曼联主教练埃里克·滕哈赫可能很快就会回归执教，接替被解雇的努里·沙欣。这位前利物浦中场球员在多特蒙德遭遇糟糕的战绩后下课...",
        paraB: "神秘人&nbsp;&nbsp;&nbsp;&nbsp;学无止境&nbsp;&nbsp;&nbsp;&nbsp;2018-5-13&nbsp;&nbsp;&nbsp;&nbsp;34567人已阅读&nbsp;&nbsp;&nbsp;&nbsp;9999人喜欢",
    },
    {
        tit: "曼联新闻：滕哈赫或将迅速回归执教，接手多特蒙德",
        imgUrl: "imgs/AA1xEFuz.jpg",
        paraA: "前曼联主教练埃里克·滕哈赫可能很快就会回归执教，接替被解雇的努里·沙欣。这位前利物浦中场球员在多特蒙德遭遇糟糕的战绩后下课...",
        paraB: "神秘人&nbsp;&nbsp;&nbsp;&nbsp;学无止境&nbsp;&nbsp;&nbsp;&nbsp;2018-5-13&nbsp;&nbsp;&nbsp;&nbsp;34567人已阅读&nbsp;&nbsp;&nbsp;&nbsp;9999人喜欢",
    },
    {
        tit: "曼联新闻：滕哈赫或将迅速回归执教，接手多特蒙德",
        imgUrl: "imgs/AA1xEFuz.jpg",
        paraA: "前曼联主教练埃里克·滕哈赫可能很快就会回归执教，接替被解雇的努里·沙欣。这位前利物浦中场球员在多特蒙德遭遇糟糕的战绩后下课...",
        paraB: "神秘人&nbsp;&nbsp;&nbsp;&nbsp;学无止境&nbsp;&nbsp;&nbsp;&nbsp;2018-5-13&nbsp;&nbsp;&nbsp;&nbsp;34567人已阅读&nbsp;&nbsp;&nbsp;&nbsp;9999人喜欢",
    },
]
newsBlog.conB = [
    {
        imgUrl: "imgs/th.jpg",
        tit: "炎国xxx对外交发布若干讲话",
    },
    {
        imgUrl: "imgs/th%20(1).jpg",
        tit: "米国xxx对外交发布若干讲话",
    },
    {
        imgUrl: "imgs/th.jpg",
        tit: "炎国xxx对外交发布若干讲话",
    },
    {
        imgUrl: "imgs/th%20(1).jpg",
        tit: "米国xxx对外交发布若干讲话",
    },
    {
        imgUrl: "imgs/th.jpg",
        tit: "炎国xxx对外交发布若干讲话",
    },
    {
        imgUrl: "imgs/th%20(1).jpg",
        tit: "米国xxx对外交发布若干讲话",
    },
    {
        imgUrl: "imgs/th.jpg",
        tit: "炎国xxx对外交发布若干讲话",
    },
    {
        imgUrl: "imgs/th%20(1).jpg",
        tit: "米国xxx对外交发布若干讲话",
    },
    {
        imgUrl: "imgs/th.jpg",
        tit: "炎国xxx对外交发布若干讲话",
    },
    {
        imgUrl: "imgs/th%20(1).jpg",
        tit: "米国xxx对外交发布若干讲话",
    },
]
// 撰写模板
newsBlog.modelA = function (tit, img, parA, parB){
    var html = ""
    html += '<div class="li"><div class="tit">'
    html += tit
    html += '</div><div class="img"><img src="'
    html += img
    html += '" alt=""></div> <div class="passage"><div class="paraA">'
    html += parA
    html += '</div><div class="paraB">'
    html += parB
    html += '</div></div></div>'
    return html
}
newsBlog.modelB = function (img, tit){
    var html = "";
    html += '<li><div class="img"><img src="';
    html += img;
    html += '" alt=""><div class="introShow"><div class="box"><div>';
    html += tit;
    html += '</div><div><a href="#">阅读</a></div></div> </div></div></li>';
    return html;
}
// 遍历填充模板
// 文章列表A
for (var i=0;i<newsBlog.conA.length;i++){
    var item = newsBlog.conA[i];
    var HTML = newsBlog.modelA(item.tit, item.imgUrl, item.paraA, item.paraB)
    newsBlog.eles.$lCon.append($(HTML))
}
// 文章列表B
for (var i=0;i<newsBlog.conB.length;i++){
    var item = newsBlog.conB[i];
    var HTML = newsBlog.modelB(item.imgUrl, item.tit)
    newsBlog.eles.$rCon.append($(HTML))
}
newsBlog.eles.$img = $("#news>.box>.con>.rCon>ul>li>.img")
newsBlog.eles.$intro = $("#news>.box>.con>.rCon>ul>li>.img>.introShow")
newsBlog.showIntro = function(elem, index){
    $(elem).show();
}
newsBlog.hideIntro = function(elem, index){
    $(elem).hide();
}
newsBlog.eles.$img.each(function (index, elem){
    $(elem).on("mouseover", function (){
        newsBlog.showIntro(newsBlog.eles.$intro[index]);
    })
})
newsBlog.eles.$img.each(function (index, elem){
    $(elem).on("mouseout", function (){
        newsBlog.hideIntro(newsBlog.eles.$intro[index]);
    })
})
// 我的相册页逻辑
albumBlog = {
    stDa: "2025/1/22",
    edDa: "2025/1/22",
    upDa: "2025/1/22",
    anchor: "Nalicost"
}
albumBlog.eles = {
    $ul: $("#album>.box>ul"),
}
albumBlog.con = [
    {
        imgUrl: "imgs/u=70037574,4009030994&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 336",
        desc: "赏心悦目的家具！",
    },
     {
        imgUrl: "imgs/u=2248739465,764058244&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 497",
        desc: "简约风格！",
    },
     {
        imgUrl: "imgs/u=3239297818,1075818153&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 999",
        desc: "非常创新的设计，令人眼前一亮！",
    },
     {
        imgUrl: "imgs/u=3976255384,2860268000&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 128",
        desc: "大胆前卫，房间设计的新典范！",
    },
    {
        imgUrl: "imgs/u=70037574,4009030994&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 336",
        desc: "赏心悦目的家具！",
    },
     {
        imgUrl: "imgs/u=2248739465,764058244&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 497",
        desc: "简约风格！",
    },
     {
        imgUrl: "imgs/u=3239297818,1075818153&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 999",
        desc: "非常创新的设计，令人眼前一亮！",
    },
     {
        imgUrl: "imgs/u=3976255384,2860268000&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 128",
        desc: "大胆前卫，房间设计的新典范！",
    },
    {
        imgUrl: "imgs/u=70037574,4009030994&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 336",
        desc: "赏心悦目的家具！",
    },
     {
        imgUrl: "imgs/u=2248739465,764058244&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 497",
        desc: "简约风格！",
    },
     {
        imgUrl: "imgs/u=3239297818,1075818153&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 999",
        desc: "非常创新的设计，令人眼前一亮！",
    },
     {
        imgUrl: "imgs/u=3976255384,2860268000&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 128",
        desc: "大胆前卫，房间设计的新典范！",
    },
    {
        imgUrl: "imgs/u=70037574,4009030994&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 336",
        desc: "赏心悦目的家具！",
    },
     {
        imgUrl: "imgs/u=2248739465,764058244&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 497",
        desc: "简约风格！",
    },
     {
        imgUrl: "imgs/u=3239297818,1075818153&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 999",
        desc: "非常创新的设计，令人眼前一亮！",
    },
     {
        imgUrl: "imgs/u=3976255384,2860268000&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 128",
        desc: "大胆前卫，房间设计的新典范！",
    },
    {
        imgUrl: "imgs/u=70037574,4009030994&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 336",
        desc: "赏心悦目的家具！",
    },
     {
        imgUrl: "imgs/u=2248739465,764058244&fm=253&fmt=auto&app=120&f=JPEG.webp",
        tag: "喜欢 | 497",
        desc: "简约风格！",
    },
     {
        imgUrl: "imgs/u=3239297818,1075818153&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 999",
        desc: "非常创新的设计，令人眼前一亮！",
    },
     {
        imgUrl: "imgs/u=3976255384,2860268000&fm=253&fmt=auto&app=138&f=JPEG.webp",
        tag: "喜欢 | 128",
        desc: "大胆前卫，房间设计的新典范！",
    },
]
albumBlog.modelA = function (img, tag, tit){
    var html = ""
    html += '<li><img src="'
    html += img
    html += '" alt=""><div class="tag">'
    html += tag
    html += '</div><div class="tit">'
    html += tit
    html += '</div></li>'
    return html
}
for (var i=0;i<albumBlog.con.length;i++){
    var item = albumBlog.con[i];
    var HTML = albumBlog.modelA(item.imgUrl, item.tag, item.desc)
    albumBlog.eles.$ul.append($(HTML))
}

