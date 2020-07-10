import { Component, OnInit } from '@angular/core';
import {DataService} from '../../../../services/data/data.service'
import {Allnumber,Allpicture,BasicResults,MonthResults,ShowProvince,ShowCity} from '../../../../entity/statistic';
import {ForJava} from '../../../../entity/forJava';
// import {MapComponent}from  './map/map.component';
//使用jquery的时候需要引入这个
import * as $ from 'jquery';
@Component({
  selector: 'app-statistics',
  templateUrl: './statistics.component.html',
  styleUrls: ['./statistics.component.less']
})
export class StatisticsComponent implements OnInit {

  
  constructor(
    private dataService:DataService
  ) { }
 
  public allNumber:number;
  public increaseNumber:number;
  public allPic:string[]=null;
  public basic_results_name:string[]=null;
  public basic_results_num:number[];
  public yearlist:string[]=null;
  public monthlist:string[]=null;
  public num_month:number[];
  public cur_province:string;
  public province_p:string[]=null;
  public city_p:string[]=null;
  public city_c:string[][]=null;
  public nav_plist:string[]=null;
  public nav_clist:string[]=null;
  public date:any;
  public m_flag=0;

  ngOnInit(): void {
  }

  ngAfterViewInit():void{
    this.getCountry();


    var myDate = new Date;
    var year = myDate.getFullYear(); //获取当前年
    var mon = myDate.getMonth() + 1; //获取当前月
    var date = myDate.getDate(); //获取当前日
    // var h = myDate.getHours();//获取当前小时数(0-23)
    // var m = myDate.getMinutes();//获取当前分钟数(0-59)
    // var s = myDate.getSeconds();//获取当前秒
    var week = myDate.getDay();
    var weeks = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
    console.log(date, mon, date, weeks[week])
    this.date=year+"年"+mon+"月"+date+"日"+" "+weeks[week];

    //获取点击事件的对象
    $(".nav li").click(function(){
      //获取要显示或隐藏的对象
      var divShow = $(".content").children('.list');
      //判断当前对象是否被选中，如果没选中的话进入if循环
      if (!$(this).hasClass('selected')) {
        //获取当前对象的索引
        var index = $(this).index();
        //当前对象添加选中样式并且其同胞移除选中样式；
        $(this).addClass('selected').siblings('li').removeClass('selected');
        //索引对应的div块显示
        
        $(divShow[index]).show();
        
        //索引对应的div块的同胞隐藏
        
        $(divShow[index]).siblings('.list').hide();
        
      }
    });


    //获取点击事件的对象
    $(".nav1 li").click(function(){
      //获取要显示或隐藏的对象
      var divShow = $(".list").children('.list1');
      //判断当前对象是否被选中，如果没选中的话进入if循环
      if (!$(this).hasClass('selected')) {
        //获取当前对象的索引
        var index = $(this).index();
        //当前对象添加选中样式并且其同胞移除选中样式；
        $(this).addClass('selected').siblings('li').removeClass('selected');
        //索引对应的div块显示
        $(divShow[index]).show();
        //索引对应的div块的同胞隐藏
        $(divShow[index]).siblings('.list1').hide();
      }
    });

    //获取点击事件的对象
    $(".nav3 li").click(function(){
      //获取要显示或隐藏的对象
      var divShow = $(".datechange").children('.list3');
      //判断当前对象是否被选中，如果没选中的话进入if循环
      if (!$(this).hasClass('selected')) {
        //获取当前对象的索引
        var index = $(this).index();
        //当前对象添加选中样式并且其同胞移除选中样式；
        $(this).addClass('selected').siblings('li').removeClass('selected');
        //索引对应的div块显示
        $(divShow[index]).show();
        //索引对应的div块的同胞隐藏
        $(divShow[index]).siblings('.list3').hide();
      }
    });

    //获取点击事件的对象
    $(".plat li").click(function(){
      //获取要显示或隐藏的对象
      var divShow = $(".datechange").children('.list4');
      //判断当前对象是否被选中，如果没选中的话进入if循环
      if (!$(this).hasClass('selected')) {
        //获取当前对象的索引
        var index = $(this).index();
        //当前对象添加选中样式并且其同胞移除选中样式；
        $(this).addClass('selected').siblings('li').removeClass('selected');
        //索引对应的div块显示
        $(divShow[index]).show();
        //索引对应的div块的同胞隐藏
        $(divShow[index]).siblings('.list4').hide();
      }
    });
    
  }

  getCountry1(){
    this.getCountry();
    this.getCountry();
  }
  getProvince1(){
    this.getProvince();
    this.getProvince();
  }

  //全国页面
  getCountry(){
    this.getData("get_country_allnumber","","get_country_addnumber","","get_country_picture","","get_country_results","");
  }
  //各省页面
  getProvince(){
    //获取省的下拉菜单
    this.getShowProvince("get_province_allnamelist","");
    if(this.province_p.length!=0)
      {
        this.getData("get_province_allnumber",this.province_p[0],"get_province_addnumber",this.province_p[0],"get_province_picture",this.province_p[0],"get_province_results",this.province_p[0]);
        this.cur_province=this.province_p[0];
      }
    
  }
  //各特定当省页面
  getProvinceSpec(province:string){
    //获取省的下拉菜单
    this.cur_province=province;
    this.getShowProvince("get_province_allnamelist","");
    this.getData("get_province_allnumber",province,"get_province_addnumber",province,"get_province_picture",province,"get_province_results",province);
    
  }
  //获取省的下拉菜单
  getAllProvinceList(){
    this.getShowProvince("get_province_allnamelist","");
  }

  //特定省求助地图
  getProvinceSpecMap(p:string){
    this.getAllPicSpec("get_province_picture",p);
  }
  //各市页面
  getCity(){
    //获得市的下拉菜单
    this.getAllPCList();
    var index
    for(var i=0;i<this.city_c.length;i++)
    {
        if(this.city_c[i].length!=0)
        {
          index=i;
          break;
        }
    }
    this.getData("get_city_allnumber",this.city_c[index][0],"get_city_addnumber",this.city_c[index][0],"get_city_picture",this.city_c[index][0],"get_city_results",this.city_c[index][0]);
  }
  //特定市页面
  getCitySpec(city:string){
    //获得市的下拉菜单
    this.getAllPCList();
    this.getData("get_city_allnumber",city,"get_city_addnumber",city,"get_city_picture",city,"get_city_results",city);
  }
  //获得市的下拉菜单
  getAllPCList(){
    this.getShowCity("get_city_allnamelist","")
  }
  //特定市求助地图
  getCitySpecMap(c:string){
    this.getAllPicSpec("get_city_picture",c);
  }
  //年龄页面
  getAge(){
    this.getData("get_age_allnumber","","get_age_addnumber","","get_age_picture","","get_age_results","");
  }
  //时间页面默认年
  getTime(){
    this.getData("get_time_allnumber","","get_time_addnumber","","get_year_picture","","get_year_results","");
  }
  //获得年
  getYear(){
    this.m_flag=0;
    this.getData("get_time_allnumber","","get_time_addnumber","","get_year_picture","","get_year_results","");
  }
  //获得月
  getMonth(){
    this.m_flag=1;
    this.getMonthData("get_time_allnumber","","get_time_addnumber","","get_month_picture","","get_month2020_results","");
  }
  //获得日
  getDay(){
    this.m_flag=0;
    this.getData("get_time_allnumber","","get_time_addnumber","","get_day_picture","","get_day_results","");
  }

  //通用获取页面所有数据的函数
  getData(a_str:string,a_info:string,i_str:string,i_info:string,pic_str:string,p_info:string,re_str:string,re_info:string){
    if(a_str!="")
      this.getAllnumberData(a_str,a_info);
    if(i_str!="")
      this.getIncreaseNumber(i_str,i_info);
    if(pic_str!="")
      this.getAllPic(pic_str,p_info);

    if(re_str!="")
    {
        this.getBasicResults(re_str,re_info);
    }
  }
  getMonthData(a_str:string,a_info:string,i_str:string,i_info:string,pic_str:string,p_info:string,re_str:string,re_info:string){
    if(a_str!="")
      this.getAllnumberData(a_str,a_info);
    if(i_str!="")
      this.getIncreaseNumber(i_str,i_info);
    if(pic_str!="")
      this.getAllPic(pic_str,p_info);

    if(re_str!="")
    {
        this.getMonthResults(re_str,re_info);
    }
  }
  getAllnumberData(func:string,info:string){
    var forJava:ForJava={function:func,infoValue:info};
    this.dataService.getData<Allnumber>('client','getAllnumber',forJava).subscribe(allnumber=>{
      this.allNumber=allnumber.number
      console.log(this.allNumber);
    });
  }
  getIncreaseNumber(func:string,info:string){
    var forJava:ForJava={function:func,infoValue:info};
    this.dataService.getData<Allnumber>('client','getAllnumber',forJava).subscribe(increseNumber=>{
      this.increaseNumber=increseNumber.number
      console.log(this.increaseNumber);
    });
  }
  getAllPic(func:string,info:string){
    var forJava:ForJava={function:func,infoValue:info};
    this.dataService.getData<Allpicture>('client','getAllPic',forJava).subscribe(allPic=>{
      if(allPic.picture)
      {
        this.allPic=allPic.picture;
        // console.log(this.allPic);
        // sessionStorage.setItem('pic',this.allPic.toString());
      }
    });
  }
  getAllPicSpec(func:string,info:string){
    var forJava:ForJava={function:func,infoValue:info};
    this.dataService.getData<Allpicture>('client','getAllPic',forJava).subscribe(allPic=>{
      if(allPic.picture)
      {
        this.allPic=allPic.picture;
      }
    });
  }
  getBasicResults(func:string,info:string){
    var forJava:ForJava={function:func,infoValue:info};
    this.dataService.getData<BasicResults>('client','getBasicResults',forJava).subscribe(basicResults=>{
      if(basicResults.results_name)
      {
        this.basic_results_name=basicResults.results_name;
      }
      
      this.basic_results_num=basicResults.results_num;
    });
  }
  getMonthResults(func:string,info:string){
    console.log("月");
    var forJava:ForJava={function:func,infoValue:info};
    this.dataService.getData<MonthResults>('client','getMonthResults',forJava).subscribe(monthResults=>{
      if(monthResults.results_year)
      {
        this.yearlist=monthResults.results_year;
      }
      if(monthResults.results_month)
      {
        this.monthlist=monthResults.results_month;
      }
      if(monthResults.results_num)
      {
        this.num_month=monthResults.results_num;
      }
    });
  }
  getShowProvince(func:string,info:string){
    var forJava:ForJava={function:func,infoValue:info};
    this.dataService.getData<ShowProvince>('client','getShowProvince',forJava).subscribe(showProvince=>{
      if(showProvince.province)
      {
        this.province_p=showProvince.province;
      }
    });
  }
  getShowCity(func:string,info:string){
    var forJava:ForJava={function:func,infoValue:info};
    this.dataService.getData<ShowCity>('client','getShowCity',forJava).subscribe(showCity=>{
      if(showCity.province)
      {
        this.city_p=showCity.province;
      }
      if(showCity.city)
      {
        this.city_c=showCity.city;
        console.log(this.city_c);
      }
    });
  }
}
