import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';

import { Observable} from 'rxjs';

import { User } from '../../entity/user';
import { Content } from  '../../entity/content';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json'}),
};

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  checkUser (user: User): Observable<Content> {
    return this.http.post<Content>('/api/userServlet?action=login', user, httpOptions);
  }
  regist(user:User):Observable<Content>{
    return this.http.post<Content>('/api/userServlet?action=regist',user,httpOptions);
  }
  logOff(){
    sessionStorage.removeItem("user");
  }
}
