import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Login } from './login.model';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private _http : HttpClient) { }


  Check(nom,passwo) : Observable<Login[]> {
    let url = "http://127.0.0.1:8000/api/checkuser/"
      return this._http.post<any>(url,{ "userName" : nom ,"password" : passwo}) ; 
      
    } 
  
}
