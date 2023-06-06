import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Offers } from './offers.model';

@Injectable({
  providedIn: 'root'
})
export class OffersService {

  constructor(private _http : HttpClient ) { }


  onSearch() : Observable<Offers[]> {
  let url = `http://127.0.0.1:8000/api/offrelist/`
    return this._http.get<any>(url) ; 
    
  } 

  onSearch2(id) : Observable<Offers[]> {
    let url = "http://127.0.0.1:8000/api/offredetail/"+id+"/"
    return this._http.get<any>(url)

   }     


}
