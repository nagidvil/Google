import { Component, OnInit } from '@angular/core';
import {DomSanitizer} from '@angular/platform-browser';  
import {DataService} from '../../../../services/data/data.service';
import {DataInfo} from '../../../../entity/dataInfo';
import {ForJava} from '../../../../entity/forJava';
@Component({
  selector: 'app-custom-webinfo',
  templateUrl: './custom-webinfo.component.html',
  styleUrls: ['./custom-webinfo.component.less']
})
export class CustomWebinfoComponent implements OnInit {

  constructor(
    private sanitizer: DomSanitizer,
    private dataService:DataService
  ) { }
  public webUrl:string='';
  public iframeSrc:any='';
  public nameList:string[]=null;
  public diseaseList:string[]=null;
  ngOnInit(): void {
    this.webUrl=sessionStorage.getItem("webUrl");
    if(this.webUrl.search("http://")==-1)
      this.iframeSrc = this.sanitizer.bypassSecurityTrustResourceUrl("http://"+this.webUrl);
    else
      this.iframeSrc = this.sanitizer.bypassSecurityTrustResourceUrl(this.webUrl);
    var forJava:ForJava={function:"getWebData",infoValue:this.webUrl};
    this.getData(forJava);
  }
  getData(forJava:ForJava){
    console.log(forJava.infoValue);
    this.dataService.getData<DataInfo>('client','getWebData',forJava).subscribe(dataInfo=>{
      if(dataInfo.name){
        this.nameList=dataInfo.name;
      }
      if(dataInfo.disease){
        this.diseaseList=dataInfo.disease;
      }
    });
  }
}
