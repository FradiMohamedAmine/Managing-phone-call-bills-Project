import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Contract } from './contract.model';

@Injectable({
  providedIn: 'root'
})
export class ContractService {

  constructor(public _http : HttpClient ) { }


  onSearch() : Observable<Contract[]> {
  let url = `http://127.0.0.1:8000/api/contratlist/`
    return this._http.get<any>(url) ; 
    
  } 
  
  onSearch2(id) : Observable<Contract[]> {
    let url = "http://127.0.0.1:8000/api/contratdetail/"+id+"/"
    return this._http.get<any>(url)

   }        


}
