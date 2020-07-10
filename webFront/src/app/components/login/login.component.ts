import { Component, OnInit } from '@angular/core';

//使用jquery的时候需要引入这个
import * as $ from 'jquery';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Router, ActivatedRoute} from '@angular/router';
import {UserService} from '../../services/user/user.service';

import { User } from '../../entity/User';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.less']
})
export class LoginComponent implements OnInit {

  constructor(
    private userService: UserService,
    private router: Router) {
   }

  public user:User={id:null,username:'',password:'',email:''};
  public username:string;
  public password:string;
  public msg:string="请输入用户名和密码";
  

 
  ngOnInit(): void {
  }

  ngAfterViewInit():void{
    
  }
  checkUser(){

    let username:string=this.username;
    let password:string=this.password;

    //提交表单的验证
    var usernamePatt=/^\w{5,12}$/;
    if(!usernamePatt.test(username)){
        this.msg="用户名不合法";
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

    this.user.username=username;
    this.user.password=password;
    this.login();
    
  }
  login(){
    this.userService.checkUser(this.user).subscribe(content => {
      console.log(content);
      if(content.state){
        
        this.user.id=content.id;
        this.user.email=content.email;

        const userStr:string=JSON.stringify(this.user);
        sessionStorage.setItem('user',userStr);
        console.log("登录成功");
        this.router.navigate(['/main']);
        // return;
      }
      else{
        this.msg="用户名或密码错误";
        return;
      }
    });
  }
}
