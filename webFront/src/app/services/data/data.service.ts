import { Injectable, Type } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import {ForJava} from '../../entity/forJava';

import { Observable} from 'rxjs';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json'}),
};

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(
    private http: HttpClient
  ) { }
  getData<T>(servlet:string,action:string,forJava:ForJava):Observable<T>{
    console.log('/api/'+servlet+'Servlet'+'?action='+action);
    return this.http.post<T>('/api/'+servlet+'Servlet'+'?action='+action,forJava,httpOptions);
  }
}
