import { Component, OnInit } from '@angular/core';
import { DataService} from '../../../../services/data/data.service';
import { Patient } from 'src/app/entity/patient';
import {ForJava} from '../../../../entity/forJava';
@Component({
  selector: 'app-critical-patients',
  templateUrl: './critical-patients.component.html',
  styleUrls: ['./critical-patients.component.less']
})
export class CriticalPatientsComponent implements OnInit {

  constructor(
    private dataService:DataService
  ) { }
  public user_ID_list:string[]=null;
	public release_time_list:string[]=null;
	public name_list:string[]=null;
	public age_list:string[]=null;
	public location_list:string[]=null;
	public ill_time_list:string[]=null;
	public phone_num1_list:string[]=null;
	public phone_num2_list:string[]=null;
  public original_content_list:string[]=null;
  public flag:number=0;
  
  ngOnInit(): void {
    // this.getCriticalPatient();
  }
  ngAfterViewInit():void{
    this.getCriticalPatient();
  }
  ngAfterViewChecked():void{
    this.flag=1;
  }
  closeTip(){
    this.flag=0;
  }
  getCriticalPatient(){
    console.log("getCriticalPatient");
    var forJava:ForJava={function:"get_dan_patient",infoValue:""};
    this.dataService.getData<Patient>('client','getCriticalPatient',forJava).subscribe(patient=>{
      if(patient.user_ID){
        console.log(this.user_ID_list);
        this.user_ID_list=patient.user_ID;
      }
      if(patient.release_time){
        this.release_time_list=patient.release_time;
      }
      if(patient.name){
        this.name_list=patient.name;
      }
      if(patient.age){
        this.age_list=patient.age;
      }
      if(patient.location){
        this.location_list=patient.location;
      }
      if(patient.ill_time){
        this.ill_time_list=patient.ill_time;
      }
      if(patient.phone_num1){
        this.phone_num1_list=patient.phone_num1;
      }
      if(patient.phone_num2){
        this.phone_num2_list=patient.phone_num2;
      }
      if(patient.original_content){
        this.original_content_list=patient.original_content;
      }
    });
  }
  getSimilarPatient(index:any){

    var forJava:ForJava={function:"get_similar_patient",infoValue:String(index)};
    this.dataService.getData<Patient>('client','getCriticalPatient',forJava).subscribe(patient=>{
      if(patient.name){
        this.name_list=patient.name;
        console.log(this.name_list)
      }
      if(patient.release_time){
        this.release_time_list=patient.release_time;
      }
      if(patient.name){
        this.name_list=patient.name;
      }
      if(patient.age){
        this.age_list=patient.age;
      }
      if(patient.location){
        this.location_list=patient.location;
      }
      if(patient.ill_time){
        this.ill_time_list=patient.ill_time;
      }
      if(patient.phone_num1){
        this.phone_num1_list=patient.phone_num1;
      }
      if(patient.phone_num2){
        this.phone_num2_list=patient.phone_num2;
      }
      if(patient.original_content){
        this.original_content_list=patient.original_content;
      }
    });
  }
}
