import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute} from '@angular/router';
@Component({
  selector: 'app-regist-success',
  templateUrl: './regist-success.component.html',
  styleUrls: ['./regist-success.component.less']
})
export class RegistSuccessComponent implements OnInit {

  constructor(private router:Router) { }

  ngOnInit(): void {
  }
  jumpLogin(){
    this.router.navigate(['/login']);
  }
}
