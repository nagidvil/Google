import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {FormsModule} from'@angular/Forms';

import { MainRoutingModule } from './main-routing.module';
import { MainComponent } from './main.component';
import { NavComponent } from '../main/components/nav/nav.component';
import { GainWebInfoComponent } from '../main/components/gain-web-info/gain-web-info.component';
import { ImportDataComponent } from '../main/components/import-data/import-data.component';
import { StatisticsComponent } from '../main/components/statistics/statistics.component';
import { RegionalWarningComponent } from '../main/components/regional-warning/regional-warning.component';
import { CriticalPatientsComponent } from '../main/components/critical-patients/critical-patients.component';
import { WelcomeComponent } from './components/welcome/welcome.component';
import { CustomWebinfoComponent } from './components/custom-webinfo/custom-webinfo.component';
import {MapComponent} from './components/statistics/map/map.component';

@NgModule({
  declarations: [
    MainComponent, NavComponent,GainWebInfoComponent,
    ImportDataComponent,StatisticsComponent,RegionalWarningComponent,CriticalPatientsComponent, WelcomeComponent, CustomWebinfoComponent, MapComponent
  ],
  exports:[
    MainComponent, NavComponent,GainWebInfoComponent,
    ImportDataComponent,StatisticsComponent,RegionalWarningComponent,CriticalPatientsComponent
  ],
  imports: [
    CommonModule,
    MainRoutingModule,
    FormsModule
  ]
})
export class MainModule { }
