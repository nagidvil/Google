//在所有统计页面里的总患病人数和较昨日增加
export class Allnumber{
    number:number
  }
  
//所有图片
export class Allpicture{
  picture:string[]
}

//除月份的数据显示那一块外其他所有的数据显示
export class BasicResults{
  results_name:string[];
  results_num:number[]
}


//月份的数据显示
export class MonthResults{
  results_year:string[];
  results_month:string[];
  results_num:number[]
}

//省份选栏中的省份名字
export class ShowProvince{
  province:string[];
}

//地区选栏中的地区名字
export class ShowCity{
  province:string[];
  city:string[][];
}