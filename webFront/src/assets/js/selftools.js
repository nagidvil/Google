//判断obj时否含有cn类
function hasClass(obj,cn){
    var reg=new RegExp("\\b"+cn+"\\b");
    return reg.test(obj.className);
}
//向obj中添加cn类
function addClass(obj,cn){
    if(!hasClass(obj,cn)){
        obj.className+=" "+cn;
    }
}
//移除obj中的cn类
function removeClass(obj,cn){
    var reg=new RegExp("\\b"+cn+"\\b");
    obj.className=obj.className.replace(reg,"");
}
/*
*在obj中切换类
*有删除，无添加
 */
function toggleClass(obj,cn){
    if(hasClass(obj,cn)){
        removeClass(obj,cn);
    }else{
        addClass(obj,cn);
    }

}
