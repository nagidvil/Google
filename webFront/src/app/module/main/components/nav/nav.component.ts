import { Component, OnInit } from '@angular/core';
import {ToolsService} from '../../../../services/tools.service';
import {UserService} from '../../../../services/user/user.service';
import { Router, ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.less'],  
})
export class NavComponent implements OnInit {

  public username:string='';
  constructor(
    public toolsService:ToolsService,
    public userService:UserService,
    private router: Router
    ) { }

  ngOnInit(): void {
    var userStr:string=sessionStorage.getItem("user");
    this.getCurrentUser(userStr);
  }



  ngAfterViewInit():void{

    var toolsService:ToolsService=this.toolsService;

    var menuSpan:any = document.querySelectorAll(".menuSpan");		
    //定义一个变量，来保存当前打开的菜单
    var openDiv:any = menuSpan[0].parentNode;
    
    for(var i:any=0 ; i<menuSpan.length ; i++){
      menuSpan[i].onclick = function(){
        
        var parentDiv = this.parentNode;
        //切换菜单的显示状态
        toolsService.toggleClass(parentDiv , "collapsed");       
      };
    }
    
    //设置选中后高亮
    var subNav:any=document.getElementsByClassName("subNav");
    var i,j;
    var length=subNav.length;
    for(i=0;i<length;i++){
      subNav[i].onclick=function(){
        for(j=0;j<length;j++){
          subNav[j].className="subNav";
        }
        this.className+=" clickNav";

      }
    }
  }
  getCurrentUser(str:string){
      var userJson:any=JSON.parse(str);
      this.username=userJson.username;
  }
  logOff(){
    this.userService.logOff();
    this.router.navigate(['/login']);
  }
}
