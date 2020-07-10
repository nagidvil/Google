import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-gain-web-info',
  templateUrl: './gain-web-info.component.html',
  styleUrls: ['./gain-web-info.component.less']
})
export class GainWebInfoComponent implements OnInit {

  constructor(
    private router:Router
  ) { }

  public webUrl:string='';
  ngOnInit(): void {
  }
  getWebInfo(){
    sessionStorage.setItem("webUrl",this.webUrl);
    this.router.navigate(['/main/customWebinfo']);
  }
}
