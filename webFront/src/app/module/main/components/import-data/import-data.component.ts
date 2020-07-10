import { Component, OnInit } from '@angular/core';
import {DomSanitizer} from '@angular/platform-browser'

@Component({
  selector: 'app-import-data',
  templateUrl: './import-data.component.html',
  styleUrls: ['./import-data.component.less']
})
export class ImportDataComponent implements OnInit {

  constructor(
    private sanitizer:DomSanitizer
  ) { }

  ngOnInit(): void {
  }
  getFile(){
   ;
  }
}
