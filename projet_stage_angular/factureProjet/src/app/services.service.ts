import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Service } from './service.model';

@Injectable({
  providedIn: 'root'
})
export class ServicesService {

  constructor(private _http : HttpClient ) { }


  onSearch() : Observable<Service[]> {
  let url = `http://127.0.0.1:8000/api/servicelist/`
    return this._http.get<any>(url) ; 
    
  } 

  onSearch2(id) : Observable<Service[]> {
    let url = "http://127.0.0.1:8000/api/servicedetail/"+id+"/"
    return this._http.get<any>(url)

   }     


}
