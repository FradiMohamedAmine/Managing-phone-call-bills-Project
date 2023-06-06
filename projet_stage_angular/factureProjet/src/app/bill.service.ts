import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Bills } from './bills.model';

@Injectable({
  providedIn: 'root'
})
export class BillService {

  constructor(private _http : HttpClient ) { }


  onSearch() : Observable<Bills[]> {
  let url = `http://127.0.0.1:8000/api/facturelist/`
    return this._http.get<any>(url) ; 
    
  } 

  onSearch2(id) : Observable<Bills[]> {
    let url = "http://127.0.0.1:8000/api/facturedetail/"+id+"/"
    return this._http.get<any>(url)

   }     


    
   pay_bill(id){
    const body = { title: 'Angular PUT Request  pay' };
    let url =`http://127.0.0.1:8000/api/checkpaidfacturebyID/${id}/`
    return this._http.put(url ,body)
  
   }
   calcul_bill(id){
    const body = { title: 'Angular PUT Request  calcul' };
    let url =`http://127.0.0.1:8000/api/sommefacturebyfactureID/${id}/`
    return this._http.put(url ,body)
  
   }


}
