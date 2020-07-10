import { Component, OnInit } from '@angular/core';
import {ForJava} from '../../../../entity/forJava';
import {DataService} from '../../../../services/data/data.service'
import {Allpicture,ShowProvince,ShowCity} from '../../../../entity/statistic';

@Component({
  selector: 'app-regional-warning',
  templateUrl: './regional-warning.component.html',
  styleUrls: ['./regional-warning.component.less']
})
export class RegionalWarningComponent implements OnInit {

  constructor(
    private dataService:DataService
  ) { }

  test(t:any){
    console.log(t);
  }
  public t=1;
  public highgradelist:string[]=null;
  public midgradelist:string[]=null;
  public allPic:string[]=null;
  public recommend=["1.要充分发挥全国一盘棋的新型举国体制的制度优势，坚持全国动员、全民参与，联防联控、群防群治，实现高层领导与基层自治相协调，政府部门和民间力量相配合，构筑纵向到底、横向到边的疫情防线",
        "2.坚持科学治理和民主决策，积极听取和采纳专家专业意见，采取科学的防控策略，加强疫情信息公开。",
        "3.坚持统筹防疫和复工复产的底线思维，筑牢检测、追踪、隔离和治疗防线，做到早发现、早报告、早处置，对重点人群“应检尽检”,实现“应隔尽隔”,确保及时发现、快速处置、精准管控和有效救治的常态化机制有效运转。",
        "4.需要充分运用5G、大数据、人工智能、云计算等新一代信息技术助力科学防治、精准施策。",
        "5.推进公共卫生体系“软件”和“硬件”建设，推动“预防—控制—治疗”全链条的有机衔接，完善公共卫生应急管理，深入持续开展爱国卫生运动，弥补疫情暴露的公共卫生治理“赤字“，坚持“平战结合”，提升常态化防控形势下的治理能力。",
        "6.提高依法防控、依法治理能力，完善公共卫生领域法律法规体系,强化法治思维，从立法、执法、司法、守法各环节发力，为保障常态化疫情防控、提高公共卫生治理效能提供法治保障。",
        "7.深化抗疫全球合作，支持各国科学家开展多方面的科学研究，推动开展疫苗和药物的联合研发,加强全球公共卫生治理合作，依法抵制一些国家“借疫滥诉”行为，共建人类卫生健康共同体。"];
  public cur_pointer:any=0;
  ngOnInit(): void {
    this.getHighGradeProvince();
    this.getMidGradeProvince();
  }
  ngAfterViewInit():void{
    this.getHighGradeProvince();
    this.getMidGradeProvince();
    this.commonSetoiinter();
  }
  commonSetoiinter(){
    // var a=sessionStorage.getItem('allPic');
    var allPointer:any=document.getElementsByClassName("active");

    // 设置初始按钮
    var index=this.cur_pointer;
    allPointer[index].style.backgroundColor="black";
    allPointer[index].style.borderColor="rgba(0,0,0,.6)";
    
    // 执行点击事件
    for(var i=0;i<allPointer.length;i++)
    {
       
        allPointer[i].num=i;

        allPointer[i].onclick=function(){
            index=this.num;
            this.cur_pointer=index;
            console.log(this.cur_pointer);
            setPointer();
        }
    }

    function setPointer(){
        // // 
        // if(index>=3)
        // {
        //     index=0;
        // }
        // 修改点击后的按钮样式
        for(var i=0;i<allPointer.length;i++)
        {
            allPointer[i].style.backgroundColor="";
            allPointer[i].style.borderColor="";
        }
        allPointer[index].style.backgroundColor="#000";
        allPointer[index].style.borderColor="rgba(0,0,0,.6)";
    }
  }
  getAllPic(province){
    console.log(province)
    var forJava:ForJava={function:"get_area_pic",infoValue:province};
    forJava.infoValue=province;
    console.log(forJava);
    this.dataService.getData<Allpicture>('client','getAllPic',forJava).subscribe(allPic=>{
      console.log(allPic);
      if(allPic.picture.length!=0)
      {
        this.allPic=allPic.picture;
        console.log(this.allPic);
        sessionStorage.setItem('allPic',allPic.picture.toString());
      }
    });
  }
  getHighGradeProvince(){
    var forJava:ForJava={function:"get_area_highgrade",infoValue:""}
    this.dataService.getData<ShowProvince>('client','getShowProvince',forJava).subscribe(allProvince=>{
      if(allProvince.province)
      {
        this.highgradelist=allProvince.province;
      }
    });
  }
  getMidGradeProvince(){
    var forJava:ForJava={function:"get_area_midgrade",infoValue:""}
    this.dataService.getData<ShowProvince>('client','getShowProvince',forJava).subscribe(allProvince=>{
      if(allProvince.province)
      {
        this.midgradelist=allProvince.province;
      }
    });
  }
}
