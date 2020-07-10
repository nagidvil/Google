import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {FormsModule} from'@angular/Forms';
import {MainModule} from './module/main/main.module'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import{ToolsService} from '../app/services/tools.service';
import { LoginComponent } from './components/login/login.component';
import { RegistComponent } from './components/regist/regist.component';
import { RegistSuccessComponent } from './components/regist-success/regist-success.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegistComponent,
    RegistSuccessComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    MainModule
  ],
  providers: [ToolsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
