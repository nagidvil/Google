import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './components/login/login.component';
import { RegistComponent } from './components/regist/regist.component';
import { RegistSuccessComponent } from './components/regist-success/regist-success.component';

const routes: Routes = [

  {path:'login',component:LoginComponent},
  {path:'regist',component:RegistComponent},
  {path:'registSuccess',component:RegistSuccessComponent},
  {
    path:'main',loadChildren:'./module/main/main.module#MainModule'
  },
  //默认路由
  {path: '**', redirectTo:'/login' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
