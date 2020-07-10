import { Component, OnInit } from '@angular/core';
//使用jquery的时候需要引入这个
import * as $ from 'jquery';
import { Router, ActivatedRoute} from '@angular/router';
import {UserService} from '../../services/user/user.service';
import {User} from '../../entity/user';



@Component({
  selector: 'app-regist',
  templateUrl: './regist.component.html',
  styleUrls: ['./regist.component.less']
})
export class RegistComponent implements OnInit {

  constructor(
    private userService:UserService,
    private router:Router
  ) { }

  public username:string='';
  public password:string='';
  public repwd:string='';
  public email:string='';
  public code:string;
  public msg:string;
  public codeSrc:string;

  public user:User={id:null,username:'',password:'',email:''}

  ngOnInit(): void {
    
  }
  ngAfterViewInit():void{
    this. getRandomCode();      
  }
  Regist(){
      let username:string=this.username;
      let password:string=this.password;
      let repwd:string=this.repwd;
      let email:string=this.email;
      let code:string=this.code;

      var usernamePatt=/^\w{5,12}$/;
      if(!usernamePatt.test(username)){
          this.msg="用户名不合法"
          return;
      }
      this.msg="";

      var passwordPatt=/^\w{5,12}$/;
      if(!passwordPatt.test(password))
      {
          this.msg="密码不合法";
          return;
      }
      this.msg="";

      if(repwd!=password)
      {
          this.msg="确认密码不一致";
          return;
      }
      this.msg="";

      var emailPatt=/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
      // var emailPatt=/^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$/;
      if(!emailPatt.test(email))
      {
          this.msg="邮箱格式不正确";
          return;
      }
      this.msg="";

      if(code.toLowerCase()!=this.codeSrc.toLowerCase())
      {
          // console.log(code.toLowerCase())
          // console.log(this.codeSrc.toLowerCase())
          this.msg="验证码不正确";
          this.getRandomCode();
          return;
      }
      this.msg="";

      this.setInfo();
      this.regist();
      

    }
  setInfo(){
    this.user.username=this.username;
    this.user.password=this.password;
    this.user.email=this.email;
  }
  regist(){
    this.userService.regist(this.user).subscribe(content=>{
      if(content.state){
        console.log("注册成功");
        this.router.navigate(['/registSuccess']);
      }
      else{
        console.log("注册失败");
      }
    });
  }
  getRandomCode(){
    var randomCode="";
    var codeLength=4;//取几个随机数字
    var randomArray=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R', 'S','T','U','V','W','X','Y','Z'];
    for(var i=0;i<codeLength;i++){
        var index=Math.floor(Math.random()*52);//随机取一位数
        randomCode +=randomArray[index];//取四位数，并+相连
    }
    this.codeSrc=randomCode;
  }
}
