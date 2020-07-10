import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ToolsService {

  //尝试创建一个可以执行简单动画的函数
/*
 * 参数：
 * 	obj:要执行动画的对象
 * 	attr:要执行动画的样式，比如：left top width height
 * 	target:执行动画的目标位置
 * 	speed:移动的速度(正数向右移动，负数向左移动)
 *  callback:回调函数，这个函数将会在动画执行完毕以后执行
 */
move(obj, attr, target, speed, callback) {
	clearInterval(obj.timer);
	var current = parseInt(this.getStyle(obj, attr));
	if(current > target) {
		speed = -speed;
	}
	obj.timer = setInterval(function() {
		var oldValue = parseInt(this.getStyle(obj, attr));
		var newValue = oldValue + speed;
		if((speed < 0 && newValue < target) || (speed > 0 && newValue > target)) {
			newValue = target;
		}
		obj.style[attr] = newValue + "px";
		if(newValue == target) {
			clearInterval(obj.timer);
			//动画执行完毕，调用回调函数
			callback && callback();
		}

	}, 30);
}

/*
 * 定义一个函数，用来获取指定元素的当前的样式
 * 参数：
 * 		obj 要获取样式的元素
 * 		name 要获取的样式名
 */
getStyle(obj, name) {

	if(window.getComputedStyle) {
		return getComputedStyle(obj, null)[name];
	} else {
		return obj.currentStyle[name];
	}

}

//判断obj时否含有cn类
hasClass(obj,cn){
    var reg=new RegExp("\\b"+cn+"\\b");
    return reg.test(obj.className);
}
//向obj中添加cn类
addClass(obj,cn){
    if(!this.hasClass(obj,cn)){
        obj.className+=" "+cn;
    }
}
//移除obj中的cn类
removeClass(obj,cn){
    var reg=new RegExp("\\b"+cn+"\\b");
    obj.className=obj.className.replace(reg,"");
}
/*
*在obj中切换类
*有删除，无添加
 */
toggleClass(obj,cn){
    if(this.hasClass(obj,cn)){
        this.removeClass(obj,cn);
    }else{
        this.addClass(obj,cn);
    }

}


  constructor() { }
}


