import { NgModule, Component } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MainComponent} from  './main.component'
import { CriticalPatientsComponent } from './components/critical-patients/critical-patients.component';
import { GainWebInfoComponent } from './components/gain-web-info/gain-web-info.component';
import { ImportDataComponent } from './components/import-data/import-data.component';
import { RegionalWarningComponent } from './components/regional-warning/regional-warning.component';
import { StatisticsComponent } from './components/statistics/statistics.component';
import { WelcomeComponent} from './components/welcome/welcome.component';
import {CustomWebinfoComponent} from './components/custom-webinfo/custom-webinfo.component'
import { from } from 'rxjs';

const routes: Routes = [

  {
    path:'',component:MainComponent,
    children:[
      {path:'criticalPatients',component: CriticalPatientsComponent},
      {path:'gainWebInfo',component:GainWebInfoComponent},
      {path:'customWebinfo',component:CustomWebinfoComponent},
      {path:'importData',component:ImportDataComponent},
      {path:'regionalWarning',component:RegionalWarningComponent},
      {path:'statistics',component:StatisticsComponent},
      {path:'welcome',component:WelcomeComponent},
      {path: '**', redirectTo:'/main/welcome' }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
  
})
export class MainRoutingModule { }
